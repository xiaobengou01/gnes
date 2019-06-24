<p align="center">
    <img src=".github/gnes-logo-tight.png?raw=true" width="300" alt="GNES Generic Neural Elastic Search, logo made by Han Xiao">
</p>

<p align="center">GNES [<i>jee-nes</i>] is Generic Neural Elastic Search, a cloud-native semantic search system based on deep neural network. <br>It enables indexing and searching similar texts, images, videos in large scale on the cloud infrastructure.</p>

<p align="center">
<a href="#">
    <img src="http://badge.orange-ci.oa.com/ai-innersource/nes.svg" alt="building status">
</a>
<a href="https://github.com/hanxiao/bert-as-service/blob/master/LICENSE">
    <img src="https://img.shields.io/github/license/tensorflow/tensorflow.svg"
         alt="GitHub license">
</a>
</p>

<p align="center">
  <a href="#highlights">Highlights</a> •
  <a href="#what-is-it">What is it</a> •
  <a href="#install">Install</a> •
  <a href="#getting-started">Getting Started</a> •
  <a href="#server-and-client-api">API</a> •
  <a href="#book-tutorial">Tutorials</a> •
  <a href="#speech_balloon-faq">FAQ</a>  
</p>



<h2 align="center">Highlights</h2>

- :cloud: **Cloud-native**: GNES is *all-in-microservice*: encoder, indexer, preprocessor and router are all running statelessly and independently in their own containers.  They communicate via versioned APIs and collaborate under the orchestration of Docker Swarm/Kubernetes etc. Scaling, load-balancing, automated recovering, they come off-the-shelf in GNES.
- :hatching_chick: **Easy-to-use on every level**: How long would it take to deploy a change that involves just changing the encoder from BERT to ELMO or switching a layer in VGG? In GNES, this is just one line change in a YAML file. We abstract the encoding and indexing logic from the code to a YAML config, so that you can combine or stack encoders and indexers without even touching the codebase.
- :rocket: **State-of-the-art**: Taking advantage of  fast-growing research AI/ML/NLP/CV communities, we learn from best-of-breed deep learning models and plug them into GNES, making sure you always enjoy the state-of-the-art performance.
- :nut_and_bolt: **Generic and compatible**: Searching for texts, image or even short-videos? Using Python/C/Java/Go/HTTP as the client? Doesn't matter which content form you have or which language do you use, GNES can handle them all. 
- :100: **Best practice**: We love to learn the best practice from the community, helping our GNES to achieve the next level of availability, resiliency, performance, and durability. If you have any ideas or suggestions, feel free to contribute.


<h2 align="center">Getting Started</h2>

### Using GNES with Docker Swarm

The easiest and the recommended way to use GNES is via Docker, which uses containers to create virtual environments that isolate a GNES installation from the rest of the system. You don't need to worry about dependencies, they are self-contained in the GNES docker image. Moreover, GNES relies on the Docker Swarm for managing, scaling and conducting orchestration tasks over multiple micro-services. 

#### 1. Prerequisites

- [Docker Engine>=1.13](https://docs.docker.com/install/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Docker Machine](https://docs.docker.com/machine/install-machine/)


#### 2. Start GNES with the wizard

If you are new to GNES, it is recommended to use the wizard to config and start GNES.

```bash
bash <(curl -s https://transfer.sh/yVeBa/gnes-wizard.sh)
```

At the last step, the wizard will generate a random name for the service, say `my-gnes-0531`. Keep that name in mind. If you miss that name, you can always use `docker stack ls` to checkout the name of your service.

<details>
 <summary>How do I know if GNES is running succesfully? (click to expand...)</summary>

To tell whether the service is running successfully or not, you can use `docker stack ps my-gnes-0531`. It should give you results as follows:
```bash
ID                  NAME                         IMAGE                                           NODE                DESIRED STATE       CURRENT STATE                ERROR               PORTS
zku2zm9deli9        my-gnes-0531_encoder.1      ccr.ccs.tencentyun.com/gnes/aipd-gnes:86c0a3a   VM-0-3-ubuntu       Running             Running about an hour ago
yc09pst6s7yt        my-gnes-0531_grpc_serve.1   ccr.ccs.tencentyun.com/gnes/aipd-gnes:86c0a3a   VM-0-3-ubuntu       Running             Running about an hour ago
```

Note, the running status under `CURRENT STATE` suggests everything is fine.

</details>

<details>
<summary>How can I terminate GNES? (click to expand...)</summary>

To stop a running GNES service, you can use `docker stack rm my-gnes-0531`.

- Having troubles to start GNES? Checkout our [troubleshooting guide](#).
- For pro-users/developers, you may want to use our `gnes-yaml.sh` tools to [generate a YAML config via CLI](#); or simply [handcraft your own `docker-compose.yml`](#).

</details>

#### 3. Train mode: training encoders and indexers

#### 4. Index mode: adding new documents

#### 5. Query mode: searching relevant documents of a given query  


<h2 align="center">:book: Documentation</h2>

The official documentation of GNES is hosted on Read the Docs. It is automatically built, updated and archived on every new release. 

### Building the documentation from scratch

To build the documentation by yourself, you need to first [install sphinx](http://www.sphinx-doc.org/en/master/usage/installation.html).

```bash
git clone https://github.com/tencent/gnes.git && cd gnes
sphinx-apidoc -o ./docs/ ./gnes
cd docs && make html
```

<h2 align="center">Tutorial</h2>

TBA

<h2 align="center">Contributing</h2>

Thanks for your interest in contributing! There are many ways to get involved; start with our [contributor guidelines](#) and then check these [open issues](/issues) for specific tasks.

For contributors looking to get deeper into the API we suggest cloning the repository and checking out the unit tests for examples of how to call methods.

<h2 align="center">Release Notes</h2>

TBA

<h2 align="center">Citing GNES</h2>
```latex
@misc{tencent2019GNES,
  title={GNES: Generic Neural Elastic Search},
  author={Xiao, Han and Yan, Jianfeng and Wang, Feng},
  howpublished={\url{https://github.com/tencent/gnes}},
  year={2019}
}
```

<h2 align="center">License</h2>

[Apache License 2.0](./LICENSE)