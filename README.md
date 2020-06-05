#W276 Autonome Systeme Labor Group 1

In this project we were tasked with comparing the performance of two different ways of overlaying/recognizing skeletons in a video.
One way was to extract the skeleton keypoints to a json file via OpenPose which were then overlayed on the video at runtime.
The other way was to use trt_pose ...
Below you'll find a video demonstrating the two ways.

<p align="center">
  Screenshot / GIF <br />
  Link to Demo Video
</p>

> This work was done by Jingye Zhang, Janika Finken, Ga Young Volk and M. Bielawski during the IWI276 Autonome Systeme Labor at the Karlsruhe University of Applied Sciences (Hochschule Karlruhe - Technik und Wirtschaft) in SS 2020.

## Table of Contents

* [Requirements](#requirements)
* [Prerequisites](#prerequisites)
* [Pre-trained model](#pre-trained-model)
* [Running](#running)
* [Acknowledgments](#acknowledgments)

## Requirements
* Python 3.7 (or above)
* OpenCV 4.0 (or above)
* Jetson Nano
* [OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose)
* [trt_pose](https://github.com/NVIDIA-AI-IOT/trt_pose)
* [PyTorch](https://pytorch.org)
* [torchvision](https://pypi.org/project/torchvision/0.1.8)
> [Optional] ...

## Prerequisites
1. Install requirements:
```
pip install -r requirements.txt
```

## Running

To run the demo, convert the MPII Dataset to csv via MATConverter.py, download the Youtube videos via YoutubeDownloader.py and then extract skeleton keypoints via OpenPose.
Afterwards, you can run json_to_video.py:
```
python src/demo.py --model model/student-jetson-model.pth --video 0
```
> Make sure the .py files are using correct paths.

## Acknowledgments

This repo is based on
  - [MPII Dataset](http://human-pose.mpi-inf.mpg.de/)
  - [OpenCV](https://github.com/opencv/opencv/)  
  - [OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose)

Thanks to the original authors for their work!

## Contact
Please email `mickael.cormier AT iosb.fraunhofer.de` for further questions.
