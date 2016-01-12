# Team 4918 - Self-Paced Tutorials - Week 1

## Learning Objectives

At the end of this tutorial you'll understand how to:

1. Use a VM Hypervisor ([Oracle VM VirtualBox](https://www.virtualbox.org/)) to host [Ubuntu](http://www.ubuntu.com/desktop) as a guest operating system


2. Use a DVD image (.iso) to install and configure [Ubuntu Desktop](http://www.ubuntu.com/download/desktop)


3. Install the [Oracle VM VirtualBox Extensions Pack](https://www.virtualbox.org/manual/ch01.html#intro-installing) to support USB devices and webcam pass-through from host to guest


4. Search the Ubuntu software catalog to find the `terminal` program, then pin it to the start bar for easy access


5. Run administrative commands as the root user using `sudo`


6. Use `apt-get` to refresh the package repository and install the latest Ubuntu updates


## Prerequisites

### Knowledge
Before you begin you should have a basic working knowledge of the `bash` shell and Linux commands such as `ls` and `cd`, and a text editor such as `gedit`, `nano` or `vi`. 

Note:  you can practice this from the command-line after installing Ubuntu.

**Documentation:** 
* [linuxcommand.org](http://linuxcommand.org/)
* William Schott's [_The Linux Command Line_](http://sourceforge.net/projects/linuxcommand/files/TLCL/13.07/TLCL-13.07.pdf/download) (free download)

### Software

**Oracle VirtualBox**

Oracle VirtualBox supports a variety of host operating systems including Windows, Linux and MacOS. Check the Oracle [support site](http://www.oracle.com/technetwork/server-storage/virtualbox/support/index.html) for the latest list. The tutorial was tested on Windows 10 Home (64-bit) with Oracle VirtualBox 5.0.10.

**Tip:** if you have an older 64-bit personal computer, check to see if the CPU supports Intel's virtualization technology (VT), as this is required to run a 64-bit guest operating system in VirtualBox. Intel's [Processor Identification Utility](https://downloadcenter.intel.com/downloads/eula/7838/Intel-Processor-Identification-Utility-Windows-Version?httpDown=https%3A%2F%2Fdownloadmirror.intel.com%2F7838%2Feng%2Fpidenu42.msi) can be used to determine if your CPU supports VT.   <u>If your computer's CPU does not support VT you'll need to install the 32-bit version of Ubuntu.</u>
			
**Ubuntu**

At the time of writing (November 2015), the most commonly used version of Ubuntu is [Ubuntu 14.04.03 LTS](http://releases.ubuntu.com/14.04/) ("Long Term Support"), also known as "Trusty Tahr". DVD images (.iso files) are available for both 64-bit ([ubuntu-14.04.3-desktop-amd64.iso](http://releases.ubuntu.com/14.04/ubuntu-14.04.3-server-amd64.iso)) and 32-bit ([ubuntu-14.04.3-desktop-i386.iso](http://releases.ubuntu.com/14.04/ubuntu-14.04.3-desktop-i386.iso)) versions of Ubuntu. There's no need to burn these to a physical DVD as VirtualBox can read the .iso file directly from disk.

### Hardware

**Host Machine**

A laptop, PC or Mac with 2GB of *available* RAM should be enough for the tutorial. Disk space requirements as flexible.  The base Ubuntu Desktop installation consumes about 5.5GB of disk space (including swap space); plan to allocate several GB more for applications and temporary files. At the end of the tutorial you'll have approximately 3GB of free space available.

**USB Webcam**

Modern Linux distributions have built-in support for USB-based webcams. The [Ubuntu Webcam wiki](https://help.ubuntu.com/community/Webcam) provides a good overview.  The tutorial was tested with a Logitech [HD Pro Webcam C920 HD](http://www.logitech.com/en-us/product/hd-pro-webcam-c920) which is available for under $80 USD. Other USB cameras should work, including webcams that are built into laptops. 

### Internet Access

You'll need to be connected to the Internet to perform software updates and package installations.

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


4. At the _Who are you?_ prompt, enter the following values.  Substitute the first initial of your first name and your last name for "yourname":

* **Your name:** frc-yourname
* **Your computer's name:**  frc-yourname-VirtualBox
* **Pick a username:**  frc
* **Choose a password:**   frc2016

Check the _Log in automatically_ box, then click _Continue_.  The Ubuntu installer takes over at this point. When the installation is complete, reboot the VM. [Note: it may be necessary to press _Enter_ within the VM window to get Ubuntu to restart.]

**Add the VirtualBox Extensions**

The VirtualBox Extensions must be installed to support higher screen resolution, USB devices and the webcam.

1. From the VirtualBox main menu, select _Devices_, _Optical Drives_, and make sure that VBoxGuestAdditions.iso is checked.


2. Log into the Ubuntu VM as the user _frc_. When prompted to run "VBOXADDITIONS_5.0.10_104061", click _Run_, then enter the password for the user _frc_. After the kernel has been rebuilt, press the _Enter_ key, then reboot Ubuntu.


3. After rebooting, log into Ubuntu. Resize the virtual machine's window to ensure that high-resolution display modes are now supported.

### Add the `terminal` application to the [Unity](https://unity.ubuntu.com/) desktop launcher

The desktop launcher is the vertical menu of program icons on the left side of the screen.  The uppermost program lets you search your computer and online sources.  Click the icon, then type "terminal".  Click and drag the `Terminal` application to the bottom of the desktop launcher, then double-click it to open a new terminal. You should see the following prompt:

```
    frc@frc-VirtualBox:~$
```

### Uprade to the latest Ubuntu 14.04 packages:

You now have access to the _Bash_ shell. Type the following two commands to update the system repository and upgrade to the latest  packages.  You'll be prompted to enter the _frc_ user's password to authenticate:

```
    sudo apt-get update
    sudo apt-get upgrade
```
**Tip:** at any point you can create a recovery checkpoint of your VM.  From the VirtualBox menu, select _Machine_, then _Take Snaphost_ and provide the snapshot with a name. This gives you the ability to "roll back" the VM to a known state.

### Install the `build-essential`, `cmake` and `v4l-utils` packages

* The [`build-essential`](http://packages.ubuntu.com/trusty/build-essential) package provides the GNU C and C++ compilers and core libraries


* The [`cmake`](https://cmake.org/) package contains the cross-platform build system used by OpenCV and other libraries


* The [`v4l-utils`](http://packages.ubuntu.com/trusty/v4l-utils) package provides utilities for inspecting and controlling video devices 

```
    sudo apt-get install build-essential checkinstall
    sudo apt-get install cmake
    sudo apt-get install v4l-utils
```

