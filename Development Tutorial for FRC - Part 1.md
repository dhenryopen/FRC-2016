# Development Tutorial for FRC - Part 1 (the Basics)


## Overview

Top-level FRC teams use a variety of programming languages to integrate useful 3rd-party libraries such as [OpenCV](http://opencv.org). While these languages have a steep learning curve, a number of useful working examples are available on [GitHub](http://www.github.com). The challenge many teams face is developing the skills to download, configure and test all of the moving parts. The purpose of this tutorial is to help teams mentor beginning developers so they can assist experienced developers with the build / deploy / test lifecycle. The tutorial is not meant to be a replacement for the [FRC Programming Guides](http://wpilib.screenstepslive.com/s/4485), but instead to provide a simpler starting point that is independent of [LabVIEW](http://www.ni.com/labview/) and [WPILib](https://usfirst.collab.net/sf/projects/wpilib/).  The skill developed in this tutorial can be applied to programming external "sidecar" boards such as the [Beaglebone](http://beagleboard.org/bone) and [NVIDIA Jetson TK1](https://developer.nvidia.com/embedded/develop/hardware).

All of the software used in the tutorial is available for free through open source licenses.

## Learning Objectives

At the end of this tutorial you will understand how to:

1. Download and install a VM hypervisor ([Oracle VM VirtuaBox](https://www.virtualbox.org/)) to host an [Ubuntu Desktop](http://www.ubuntu.com/desktop) guest operating system


2. Use an ISO DVD image to install and configure [Ubuntu Desktop](http://www.ubuntu.com/download/desktop)


3. Install the [Oracle VM VirtualBox Extensions Pack](https://www.virtualbox.org/manual/ch01.html#intro-installing) to support USB devices and webcam pass-through 


4. Search the Ubuntu software catalog to find the `terminal` program, then pin it to the start bar


5. Run administrative commands as the root user using `sudo`


6. Use `apt-get` to refresh the package repository and install the latest Ubuntu software updates


7. Install a USB video camera and test its operation using the [Video for Linux](http://www.linuxtv.org/) utilities and the [Cheese Webcam Booth](https://wiki.gnome.org/Apps/Cheese)


8. Install `git`, clone a GitHub repository and compile a basic C++ program to capture frames from the USB camera


9. Install OpenCV and the OpenCV sample applications, then compile and run the [facedetect](http://docs.opencv.org/master/d7/d8b/tutorial_py_face_detection.html#gsc.tab=0) example

## Prerequisites

### Knowledge
Before you begin you should have a working knowledge of the bash shell and common Linux commands such as `ls` and `cd`, and a text editor such as `gedit`, `nano` or `vi`. 

**References:** 
* [linuxcommand.org](http://linuxcommand.org/)
* William Schott's [_The Linux Command Line_](http://sourceforge.net/projects/linuxcommand/files/TLCL/13.07/TLCL-13.07.pdf/download) (free download)

### Software

**Oracle VirtualBox**

Oracle VirtualBox supports a variety of host operating systems including Windows, Linux and MacOS. Check the Oracle [support site](http://www.oracle.com/technetwork/server-storage/virtualbox/support/index.html) for the latest list. The tutorial was tested on Windows 10 Home (64-bit) with Oracle VirtualBox 5.0.10.

Tip: if you have an older 64-bit personal computer, check to see if the CPU supports Intel's virtualization technology (VT), as this is required to run a 64-bit guest operating system. Intel's [Processor Identification Utility](https://downloadcenter.intel.com/downloads/eula/7838/Intel-Processor-Identification-Utility-Windows-Version?httpDown=https%3A%2F%2Fdownloadmirror.intel.com%2F7838%2Feng%2Fpidenu42.msi) can be used to determine if your CPU supports VT.  If your computer's CPU does not support VT you'll need to install the 32-bit version of Ubuntu.
			
**Ubuntu**

At the time of writing (November 2015), the most commonly used version of Ubuntu is [Ubuntu 14.04.03 LTS](http://releases.ubuntu.com/14.04/) ("Long Term Support"), also known as "Trusty Tahr". DVD images (.iso files) are available for both 64-bit ([ubuntu-14.04.3-desktop-amd64.iso](http://releases.ubuntu.com/14.04/ubuntu-14.04.3-server-amd64.iso)) and 32-bit ([ubuntu-14.04.3-desktop-i386.iso](http://releases.ubuntu.com/14.04/ubuntu-14.04.3-desktop-i386.iso)) versions of Ubuntu. There is no need to burn these to a physical DVD as VirtualBox can read the .iso file directly from disk.

### Hardware

**The Host Machine**

A laptop, PC or Mac with 2GB of *available* RAM should be enough for the tutorial. Disk space requirements as flexible.  The base Ubuntu Desktop installation consumes about 5.5GB of disk space (including swap space); plan to allocate several GB more for applications and temporary files.

**USB Webcam**

Modern Linux distributions have good support for USB-based webcams. The [Ubuntu Webcam wiki](https://help.ubuntu.com/community/Webcam) provides a good overview.  The tutorial was tested with a Logitech [HD Pro Webcam C920 HD](http://www.logitech.com/en-us/product/hd-pro-webcam-c920) which is available for under $80 USD. Other USB cameras should work, including webcams that included with recently-manufactured laptops. 

## Tasks

**Install Oracle VirtualBox**

1. [Download](https://www.virtualbox.org/wiki/Downloads) the VirtualBox installer for your operating system, then follow the instructions in Chapter 2 of the [_Oracle VirtualBox User Guide_](http://download.virtualbox.org/virtualbox/5.0.10/UserManual.pdf) to install the software


2. After starting VirtualBox, click on the _New_ icon to start the _Create Virtual Machine_ wizard. Use the following parameters to create the VM:

* **Name:** Ubuntu 14.04 Development VM for FRC
* **Type:** Linux
* **Version:** Ubuntu (64-bit) or (32-bit)
* **Memory Size:** 2048MB
* **Create a virtual hard disk now:** yes
* **Hard disk file type:** VDI (default)
* **Storage on physical hard disk:** dynamically allocated (default)
* **File location and size:** default location, 10GB

Click _Create_ and the VM will be ready to power on. 

**Install Ubuntu**


1. Right click on the new VM and select *Start --> Normal Start*. When prompted to *Select a Startup Disk*, open the folder and navigate to the location where you downloaded the Ubuntu .iso file, then click *Start*.


2. When you get to the Ubuntu _Welcome_ screen, choose your language, then select _Install Ubuntu_. Select both the _Download Updates While Installing_ and the _Install this third-party software_ option (for MP3 support). Click _Continue_, then confirm that you want to _Erase disk and install Ubuntu_.  This will not erase the host operating system's drive, only the space that has been allocated to Ubuntu.  Click _Install Now_, then _Continue_ to write the changes to the disk.

(Unless otherwise noted, execute as root (via su)


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
			
