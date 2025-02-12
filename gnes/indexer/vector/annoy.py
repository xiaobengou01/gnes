#  Tencent is pleased to support the open source community by making GNES available.
#
#  Copyright (C) 2019 THL A29 Limited, a Tencent company. All rights reserved.
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import os
from typing import List, Tuple, Any

import numpy as np

from ..base import BaseVectorIndexer
from ..key_only import ListKeyIndexer


class AnnoyIndexer(BaseVectorIndexer):

    def __init__(self, num_dim: int, data_path: str, metric: str = 'angular', n_trees=10, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.num_dim = num_dim
        self.data_path = data_path
        self.metric = metric
        self.n_trees = n_trees
        self._key_info_indexer = ListKeyIndexer()

    def post_init(self):
        from annoy import AnnoyIndex
        self._index = AnnoyIndex(self.num_dim, self.metric)
        try:
            if not os.path.exists(self.data_path):
                raise FileNotFoundError('"data_path" is not exist')
            if os.path.isdir(self.data_path):
                raise IsADirectoryError('"data_path" must be a file path, not a directory')
            self._index.load(self.data_path)
        except:
            self.logger.warning('fail to load model from %s, will create an empty one' % self.data_path)

    def add(self, keys: List[Tuple[int, Any]], vectors: np.ndarray, weights: List[float], *args, **kwargs):
        last_idx = self._key_info_indexer.size

        if len(vectors) != len(keys):
            raise ValueError('vectors length should be equal to doc_ids')

        if vectors.dtype != np.float32:
            raise ValueError("vectors should be ndarray of float32")

        for idx, vec in enumerate(vectors):
            self._index.add_item(last_idx + idx, vec)

        self._key_info_indexer.add(keys, weights)

    def query(self, keys: 'np.ndarray', top_k: int, *args, **kwargs) -> List[List[Tuple]]:
        self._index.build(self.n_trees)
        if keys.dtype != np.float32:
            raise ValueError('vectors should be ndarray of float32')
        res = []
        for k in keys:
            ret, relevance_score = self._index.get_nns_by_vector(k, top_k, include_distances=True)
            relevance_score = self.normalize_score(relevance_score, self.metric)
            chunk_info = self._key_info_indexer.query(ret)
            res.append([(*r, s) for r, s in zip(chunk_info, relevance_score)])
        return res

    def normalize_score(self, score: List[float], metrics: str, *args, **kwargs) -> List[float]:
        if metrics == 'angular':
            return list(map(lambda x: 1 / (1 + x), score))
        elif metrics == 'euclidean':
            import math
            return list(map(lambda x: 1 / (1 + math.sqrt(x) / self.num_dim), score))
        elif metrics == 'manhattan':
            return list(map(lambda x: 1 / (1 + x / self.num_dim), score))
        elif metrics == 'hamming':
            return list(map(lambda x: 1 / (1 + x), score))
        elif metrics == 'dot':
            raise NotImplementedError

    @property
    def size(self):
        return self._index.get_n_items()

    def __getstate__(self):
        d = super().__getstate__()
        self._index.save(self.data_path)
        return d
