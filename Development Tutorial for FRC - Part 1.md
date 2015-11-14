# Development Tutorial for FRC - Part 1 (the Basics)


## Overview

Top-level FRC teams use a variety of programming languages to integrate useful 3rd-party libraries such as [OpenCV](http://opencv.org). While these languages have a steep learning curve, a number of useful working examples are available on [GitHub](http://www.github.com). The challenge many teams face is developing the skills to download, configure and test all of the moving parts. The purpose of this tutorial is to help teams mentor beginning developers so they can assist experienced developers with the build / deploy / test lifecycle. The tutorial is not meant to be a replacement for the [FRC Programming Guides](http://wpilib.screenstepslive.com/s/4485), but instead to provide a simpler starting point that is independent of [LabVIEW](http://www.ni.com/labview/) and [WPILib](https://usfirst.collab.net/sf/projects/wpilib/).  The skill developed in this tutorial can be applied to programming external "sidecar" boards such as the [Beaglebone](http://beagleboard.org/bone) and [NVIDIA Jetson TK1](https://developer.nvidia.com/embedded/develop/hardware).

All of the software used in the tutorial is available for free through open source licenses.

## Learning Objectives

At the end of this tutorial yyou'll understand how to:

1. Download and install a VM hypervisor ([Oracle VM VirtuaBox](https://www.virtualbox.org/)) to host [Ubuntu](http://www.ubuntu.com/desktop) as a guest operating system


2. Use a DVD image (.iso) to install and configure [Ubuntu Desktop](http://www.ubuntu.com/download/desktop)


3. Install the [Oracle VM VirtualBox Extensions Pack](https://www.virtualbox.org/manual/ch01.html#intro-installing) to support USB devices and webcam pass-through 


4. Search the Ubuntu software catalog to find the `terminal` program, then pin it to the start bar


5. Run administrative commands as the root user using `sudo`


6. Use `apt-get` to refresh the package repository and install the latest Ubuntu software updates


7. Install a USB video camera and test its operation using the [Video for Linux](http://www.linuxtv.org/) utilities and the [Cheese Webcam Booth](https://wiki.gnome.org/Apps/Cheese)


8. Install the OpenCV sample applications, then compile and run the [facedetect](http://docs.opencv.org/master/d7/d8b/tutorial_py_face_detection.html#gsc.tab=0) example

## Prerequisites

### Knowledge
Before you begin you should have a working knowledge of the bash shell and common Linux commands such as `ls` and `cd`, and a text editor such as `gedit`, `nano` or `vi`. 

**References:** 
* [linuxcommand.org](http://linuxcommand.org/)
* William Schott's [_The Linux Command Line_](http://sourceforge.net/projects/linuxcommand/files/TLCL/13.07/TLCL-13.07.pdf/download) (free download)

### Software

**Oracle VirtualBox**

Oracle VirtualBox supports a variety of host operating systems including Windows, Linux and MacOS. Check the Oracle [support site](http://www.oracle.com/technetwork/server-storage/virtualbox/support/index.html) for the latest list. The tutorial was tested on Windows 10 Home (64-bit) with Oracle VirtualBox 5.0.10.

**Tip:** if you have an older 64-bit personal computer, check to see if the CPU supports Intel's virtualization technology (VT), as this is required to run a 64-bit guest operating system. Intel's [Processor Identification Utility](https://downloadcenter.intel.com/downloads/eula/7838/Intel-Processor-Identification-Utility-Windows-Version?httpDown=https%3A%2F%2Fdownloadmirror.intel.com%2F7838%2Feng%2Fpidenu42.msi) can be used to determine if your CPU supports VT.  If your computer's CPU does not support VT you'll need to install the 32-bit version of Ubuntu.
			
**Ubuntu**

At the time of writing (November 2015), the most commonly used version of Ubuntu is [Ubuntu 14.04.03 LTS](http://releases.ubuntu.com/14.04/) ("Long Term Support"), also known as "Trusty Tahr". DVD images (.iso files) are available for both 64-bit ([ubuntu-14.04.3-desktop-amd64.iso](http://releases.ubuntu.com/14.04/ubuntu-14.04.3-server-amd64.iso)) and 32-bit ([ubuntu-14.04.3-desktop-i386.iso](http://releases.ubuntu.com/14.04/ubuntu-14.04.3-desktop-i386.iso)) versions of Ubuntu. There is no need to burn these to a physical DVD as VirtualBox can read the .iso file directly from disk.

### Hardware

**Host Machine**

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


3. When asked _Where are you?_, type in your location and choose an appropriate timezone.  Select the keyboard layout (the default is _English (US)_) and click _Continue_.


4. At the _Who are you?_ prompt, enter the following values:

* **Your name:** frc
* **Your computer's name:**  frc-VirtualBox
* **Pick a username:**  frc
* **Choose a password:**   frc2016

Check the _Log in automatically_ box, then click _Continue_.  The Ubuntu installer takes over at this point. When the installation is complete, reboot the VM. [Note: it may be necessary to press _Enter_ within the VM window to get Ubuntu to restart.]

**Add the VirtualBox Extensions**

The VirtualBox Extensions must be installed to support higher screen resolution and to support USB devices and the webcam.

1. From the VirtualBox main menu, select _Devices_, _Optical Drives_, and make sure that VBoxGuestAdditions.iso is checked.


2. Log into the Ubuntu VM as the user _frc_. When prompted to run "VBOXADDITIONS_5.0.10_104061", click _Run_, then enter the password for the user _frc_. After the kernel has been rebuilt, press the _Enter_ key, then reboot Ubuntu

### Add the `terminal` application to the [Unity](https://unity.ubuntu.com/) desktop launcher

The desktop launcher is the svertical list of program icons on the left side of the screen.  The uppermost program lets you search your computer and online sources.  Click the icon, then type "terminal".  Click and drag the `Terminal` application to the bottom of the desktop launcher, then double-click it to open a new terminal. You should see the following prompt:

```
frc@frc-VirtualBox:~$
```

### Uprade to the latest Ubuntu 14.04 packages:

You now have access to the _Bash_ shell. Type the following two commands to update the system repository and upgrade to the latest  packages.  You'll be prompted to enter the _frc_ user's password to authenticate:

```
sudo apt-get update
sudo apt-get upgrade
```
**Tip:** at any point you can create a recovery checkpoint of your VM.  From the VirtualBox menu, select _Machine_, then _Take Snaphost_ and provide the snapshot with a name.

### Install the `git`, `build-essentials`, `cmake` and `v4l-utils` packages

* The [`git`](http://packages.ubuntu.com/trusty/git) package allows developers to clone source code repositories and post updates


* The [`build-essential`](http://packages.ubuntu.com/trusty/build-essential) package provides the GNU C and C++ compilers and core libraries


* The [`cmake`](https://cmake.org/) package contains the cross-platform build system used by OpenCV and other libraries


* The [`v4l-utils`](http://packages.ubuntu.com/trusty/v4l-utils) package provides utilities for managing the video devices which are visible to Ubuntu


```
sudo apt-get install build-essential checkinstall
sudo apt-get install git-core
sudo apt-get install cmake
sudo apt-get install v4l-utils
```


### Test connectivity to your USB camera using v4l and the Cheese application

Before compiling the _facedetect_ example, configure and test connctivity to your USB camera

1. From the VirtualBox main menu, select _Devices_, then _Webcams_ and make sure that your camera has been selected


2. From the desktop launcher menu, search for "Cheese Webcam Booth".  Run this application -- within a few seconds the camera feed should appear on the screen


3. From the Bash shell, use the `v4l2-ctl` program to get the characteristics of your webcam:

```
v4l2-ctl --all
```
You should see something like this (the details will be specific to your Webcam hardware):

```
Driver Info (not using libv4l2):
	Driver name   : uvcvideo
	Card type     : VirtualBox Webcam - HP Truevisi
	Bus info      : usb-0000:00:06.0-2
	Driver version: 3.19.8
	Capabilities  : 0x84200001
		Video Capture
		Streaming
		Device Capabilities
	Device Caps   : 0x04200001
		Video Capture
		Streaming
Priority: 2
Video input : 0 (Camera 1: ok)
Format Video Capture:
	Width/Height  : 1280/720
	Pixel Format  : 'MJPG'
	Field         : None
	Bytes per Line: 0
	Size Image    : 1228800
	Colorspace    : SRGB
	Custom Info   : feedcafe
Crop Capability Video Capture:
	Bounds      : Left 0, Top 0, Width 1280, Height 720
	Default     : Left 0, Top 0, Width 1280, Height 720
	Pixel Aspect: 1/1
Streaming Parameters Video Capture:
	Capabilities     : timeperframe
	Frames per second: 30.000 (30/1)
	Read buffers     : 0
                     brightness (int)    : min=0 max=100 step=1 default=50 value=50
```

**Tip**: Derek Molloy's website has a lot of useful information on this subject.  Although written for the Beaglebone, the v4l-utils examples can be used on "vanilla" Ubunutu:
		http://derekmolloy.ie/beaglebone-images-video-and-opencv/

		
### Install OpenCV 3.0 and samples

```
Go to opencv.org, download 2.4.11 for Linux/Mac (https://github.com/itseez/opencv/archive/2.4.11.zip)
For OpenCV 2.4.x 
cd /path/to/opencv/samples/c/
For OpenCV 3 
cd /path/to/opencv/samples/cpp/
#Compile
g++ -ggdb `pkg-config --cflags --libs opencv` facedetect.cpp -o facedetect
#run
./facedetect
```
		
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
			