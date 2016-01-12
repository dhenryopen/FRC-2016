# Team 4918 - Self-Paced Tutorials - Week 2

## Learning Objectives

At the end of this tutorial you'll understand how to:

1. Install a USB video camera and test its operation using the [Cheese Webcam Booth](https://wiki.gnome.org/Apps/Cheese) and the [Video for Linux](http://www.linuxtv.org/) utilities


2. Install the libraries needed for OpenCV development, download the sample applications, and compile and run the _facedetect_ image detection example


### Test connectivity to your USB camera using the Video 4 Linux utilities and the Cheese Webcam Booth

Before compiling the _facedetect_ example, configure and test connctivity to your USB camera:

1. From the VirtualBox main menu, select _Devices_, then _Webcams_ and make sure your camera has been selected


2. From the desktop launcher menu, search for "Cheese Webcam Booth".  Run this application -- within a few seconds the camera feed should appear on the screen. Close the application to release the connection to the webcam.


3. From the Bash shell, use the `v4l2-ctl` program to inspect the characteristics of your webcam:

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

**Tip**: Derek Molloy's website (http://derekmolloy.ie/beaglebone-images-video-and-opencv/) has a lot of useful information on this subject.  Although written for the Beaglebone, the v4l-utils examples can be used on "vanilla" Ubunutu.
		
		
### Build and test the OpenCV _facedetect_ sample program:

1. Install the prerequisite packages for OpenCV development:
```
    sudo apt-get install synaptic
    sudo apt-get install libopencv-dev
```
2. Use `wget` to get the OpenCV 2.4.11 source code:
```
    cd ~
    wget http://sourceforge.net/projects/opencvlibrary/files/opencv-unix/2.4.11/opencv-2.4.11.zip
    unzip opencv-2.4.11.zip
```
    Note: OpenCV 3.0 is the latest version of OpenCV, but Ubuntu 14.04 comes with OpenCV 2.4 already installed, allowing us to use the pre-built libraries in `/usr/lib/i386-linux-gnu`.

3. Now change to the samples directory and compile `facedetect.cpp`:
```
    cd opencv-2.4.11/samples/c
    g++ facedetect.cpp -o facedetect `pkg-config --cflags --libs opencv`
```
4. And finally, the fruits of your labor! :)
```
    ./facedetect
```
To end the program, type ^C in the terminal window.   If you want to experiment further, remember to take a snaphost of the VM so you can roll-back and return to where you started.
