# Development Tutorial for FRC - Part 1 (the VM)

## Overview

Top-level FRC teams use a variety of programming languages to integrate useful 3rd-party libraries such as [OpenCV](http://opencv.org). While these languages have a steep learning curve, a number of useful working examples are available on [GitHub](http://www.github.com). The challenge many teams face is developing the skills to download, configure and test all of the moving parts. The purpose of this tutorial is to help teams mentor beginning developers so they can assist experienced developers with the build / deploy / test lifecycle. The tutorial is not meant to be a replacement for the [FRC Programming Guides](http://wpilib.screenstepslive.com/s/4485), but instead to provide a simpler starting point that is independent of [LabVIEW](http://www.ni.com/labview/) and [WPILib](https://usfirst.collab.net/sf/projects/wpilib/).  The skill developed in this tutorial can be applied to programming external "sidecar" boards such as the [Beaglebone](http://beagleboard.org/bone) and [NVIDIA Jetson TK1](https://developer.nvidia.com/embedded/develop/hardware).

All of the software used in the tutorial is available for free through open source licenses.

## Learning Objectives

At the end of this tutorial you will understand how to:

1. Download and install a VM hypervisor ([Oracle VM VirtuaBox](https://www.virtualbox.org/)) to host an [Ubuntu Desktop](http://www.ubuntu.com/desktop) guest operating system
1. Use an ISO DVD image to install and configure [Ubuntu Desktop 14.04.3 LTS](http://www.ubuntu.com/download/desktop) (Trusty Tahr)
1. Install the [Oracle VM VirtualBox Extensions Pack](https://www.virtualbox.org/manual/ch01.html#intro-installing) to support USB devices and webcam pass-through 
1. Search the Ubuntu software catalog to find the `terminal` program, then pin it to the start bar
1. Run administrative commands as the root user using `sudo`
1. Use `apt-get` to refresh the package repository and install the latest Ubuntu software updates
1. Install a USB video camera and test its operation using the [Video for Linux](http://www.linuxtv.org/) utilities and the [Cheese Webcam Booth](https://wiki.gnome.org/Apps/Cheese)
1. Install `git`, clone a GitHub repository and compile a basic C++ program to capture frames from the USB camera
1. Install OpenCV and the OpenCV sample applications, then compile and run the [facedetect](http://docs.opencv.org/master/d7/d8b/tutorial_py_face_detection.html#gsc.tab=0) example

## Prerequisites

Before you begin you should have a working knowledge of the bash shell and common Linux commands such as `ls` and `cd`, and a text editor such as `vi`, `nano` or `gedit`. 

## Tasks

(WORK IN PROGRESS FROM HERE)

### Setup:

(Unless otherwise noted, execute as root (via su)

	Optional:
		Download and install Oracle VirtualBox (5.0.10 or higher) - http://www.oracle.com/technetwork/server-storage/virtualbox/downloads/index.html
		Download Ubuntu ISO (ubuntu-14.04.3-desktop-amd64.iso) 14.04.3 or higher (http://releases.ubuntu.com/14.04/)
			Note: if using an older 64-bit computer that doesn't support Intel virtualization technology (VT), you'll need to use the 32-bit ISO instead (ubuntu-14.04.3-desktop-i386.iso)
			The Intel Processor Identification Utility can be used to determine if your CPU supports VT
			https://downloadcenter.intel.com/downloads/eula/7838/Intel-Processor-Identification-Utility-Windows-Version?httpDown=https%3A%2F%2Fdownloadmirror.intel.com%2F7838%2Feng%2Fpidenu42.msi
		Create a VirtualBox VM called "Ubuntu 14.04 (64-bit) - FRC development VM"
			Virtual hardware: 2GB RAM (minimum), 15GB disk, 2 cpus (if on a quad-core host, otherwise 1 cpu)
			Make sure to reference the Ubunto ISO file that you downloaded
			Check "Download updates will installing" and "install this third-party software (Fluendo MP3)"
			Select your TZ (Pacific - Los Angeles)
			In the "who are you?" prompt, use the following values:
				Your name: frc
				Your computer's name: frc-VirtualBox
				Pick a username: frc
				Choose a password:  frc2016
				Check "Log in automatically"
		Add VirtualBox extensions to increase screen resolution and support USB devices
        	Mount the Guest Additions CD
            When prompted to run VBOXADDITIONS_5.0.10_104061", press OK
            After the kernel has been rebuilt, reboot
        (http://download.virtualbox.org/virtualbox/5.0.10/Oracle_VM_VirtualBox_Extension_Pack-5.0.10-104061.vbox-extpack)

### Uprade to the latest Ubuntu packages:

	Execute:
		sudo apt-get update	
		sudo apt-get upgrade

### Install git, build-essentials

	Links:
		https://help.ubuntu.com/community/CompilingEasyHowTo

	Execute:
		sudo apt-get install build-essential checkinstall
		sudo apt-get install git-core
		sudo chown $USER /usr/local/src
		sudo chmod u+rwx /usr/local/src

	Note:
		At this point version of 4.8.4 of gcc will be installed

### Test connectivity to your USB camera using v4l

		Execute:
			apt-get install v4l-utils
			
		http://derekmolloy.ie/beaglebone-images-video-and-opencv/

		
### Install OpenCV and apps

		Links
			https://help.ubuntu.com/community/OpenCV
			https://github.com/jayrambhia/Install-OpenCV/blob/master/Ubuntu/opencv_install.sh

		Execute:
			cd $HOME/software
			git https://github.com/jayrambhia/Install-OpenCV.git
			cd Install-OpenCV/Ubuntu
			./opencv_latest.sh

			(Notes: 
				1. The build process will run for a long time
				2. When done, make the software more accessible)

			cd $HOME/software
			mv Install-OpenCV/Ubuntu/OpenCV/ .
		
### Build the OpenCV sample

		Execute
			cd OpenCV/opencv-3.0.0/samples/cpp/example_cmake/
			make
			./opencv_example

			(Note: this should launch an OpenGL application that interacts with your webcam (i.e. /dev/video0))

		Execute:
			
### Clone Derek Molloy's BoneCV repository

		Links:
			http://derekmolloy.ie/beaglebone/beaglebone-video-capture-and-image-processing-on-embedded-linux-using-opencv/

		Execute: (from $HOME, as a normal user)
			mkdir software
			cd software
			git clone https://github.com/derekmolloy/boneCV.git
			cd boneCV
			rm boneCV boneCVtiming capture grabber
			gcc capture.c
			gcc grabberlc -lv4l2
			
