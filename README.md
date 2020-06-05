#W276 Autonome Systeme Labor Group 1

In this project we were tasked with comparing the performance of two different ways of overlaying/recognizing skeletons in a video.
One way was to extract the skeleton keypoints to a json file via OpenPose which were then overlayed on the video at runtime.
The other way was to use trt_pose ...
Below you'll find a video demonstrating the two ways.

<p align="center">
  Screenshot / GIF <br />
  Link to Demo Video
</p>

> This work was done by Autor 1, Autor2, Autor 3 and M. Bielawski during the IWI276 Autonome Systeme Labor at the Karlsruhe University of Applied Sciences (Hochschule Karlruhe - Technik und Wirtschaft) in SS 2020. 

## Table of Contents

* [Requirements](#requirements)
* [Prerequisites](#prerequisites)
* [Pre-trained model](#pre-trained-model)
* [Running](#running)
* [Acknowledgments](#acknowledgments)

## Requirements
* Python 3.7 (or above)
* OpenCV 4.0 (or above)
* Jetson Nano | Jetson TX2
* Jetpack 4.2
> [Optional] ...

## Prerequisites
1. Install requirements:
```
pip install -r requirements.txt
```

## Pre-trained models <a name="pre-trained-models"/>

Pre-trained model is available at pretrained-models/

## Running

To run the demo, convert the MPII Dataset to csv via MATConverter.py, download the Youtube videos via YoutubeDownloader.py and then extract skeleton keypoints via OpenPose and getJson.py.
Afterwards, you can run json_to_video.py to paint scelettons on video.

> Make sure the .py files are using correct paths.


**trt-pose**
With detect_image.py show pose on images and with detect_video show pose on video.

## Acknowledgments

This repo is based on
  - [MPII Dataset](http://human-pose.mpi-inf.mpg.de/)
  - [OpenCV](https://github.com/opencv/opencv/)  
  - [OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose)

Thanks to the original authors for their work!

## Contact
Please email `mickael.cormier AT iosb.fraunhofer.de` for further questions.
