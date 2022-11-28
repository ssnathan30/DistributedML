<h3 align="center">Distributed ML Training</h3>
  <p align="center">
    <br />
    <br />
    <br />
    <a href="">Report Bug</a>
    <br/>
    <a href="">Request Feature</a>
  </p>


<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->

## About The Project

In progress

### Built With

* [Docker](https://www.docker.com/)
* [Tensorflow](https://www.tensorflow.org/)


<!-- GETTING STARTED -->

## Getting Started

Nothing to talk about for now. 1st checkin

### Prerequisites

* A working environment 
  ```sh
  ```

### Installation

1. Clone the repo
   ```sh
   git clone 
   ```
2. Build Base Docker Image
   ```sh
   cd BaseImage
   docker build -t learn/basedtf:1.0.0 --progress=plain .
   ```
3. Build and run MultiWorkerMirroredStrategy task
   ```sh
   cd TFDevice/MultiWorkerMirroredStrategy
   docker build -t learn/dtf-multiworker-strategy:1.0.0 --progress=plain .
   docker compose up -d
   ```
4. Build and run MeshTensorflow task
   ```
   CAUTION : 
    1) This task runs in single container.
    2) Its a long running job.
   ```
   ```sh
   cd TFDevice/MeshTensorFlow
   docker build -t learn/dtf-meshtensorflow:1.0.0 --progress=plain .
   docker compose up -d
   ```
5. Build and run Parameterserver task
   1. Build server Image
      ```commandline
      cd TFDevice/ParameterServerStrategy
      cd server
      docker build -t learn/dtf-tfserver:1.0.0 --progress=plain .
      ```
   2. Build Parameter server strategy Image
      ```
      cd ..
      docker build -t learn/dtf-psstrategy:1.0.0 --progress=plain .
      ```
   3. Start docker compose
      ```commandline
      docker compose up -d
      ```
6. Build and run Distributed Pytorch task - Model Parallelism
   ```commandline
   cd TFDevice/DistributedPytorch
   docker build -t learn/pytorch-rpc:1.0.0 --progress=plain .
   docker compose up -d
   ```
    
<!-- USAGE EXAMPLES -->

## Usage

```sh
TBD
```

<!-- ROADMAP -->

## Roadmap

1. initial skeleton --- IN PROGRESS




<!-- CONTRIBUTING -->

## Contributing

If you really want to...

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- LICENSE -->

## License



<!-- CONTACT -->

## Contact

Swaminathan Sriram - [ssnathan3097](mailto:swsr1249@colorado.edu) - swaminathan[-dot-]sriram[-at-]colorado[-dot-]edu

Project Link:


<!-- ACKNOWLEDGEMENTS -->

## Acknowledgements

* [google](www.google.com)
* [stackoverflow](www.stackoverflow.com)


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
