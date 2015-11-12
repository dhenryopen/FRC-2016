ADXL345_server and ADXL345_client
~~~~~~~~~~~~~~~~~~
These two programs "fuse" two different open source samples to create a UDP-based server (ADXL345_server) that broadcasts ADXL345 accelerometer data (X,Y,Z,Pitch,Roll) to a UDP client (ADXL345_client)
The goal is to support testing with the Labview UDP VI (http:zone.ni.com/reference/en-XX/help/371361M-01/lvcomm/udp_vi_descriptions/) on a closed network (i.e., it is not secure)

The server was developed and tested using a Beaglebone Green board with a Grove 3-Axis Digital Accelerometer on an I2C port: (http:www.seeedstudio.com/wiki/Grove_-_3-Axis_Digital_Accelerometer(%C2%B116g))
The client was developed and tested on Ubuntu 14.04

To-dos:
1.Port to NVIDIA Tegra TK1
2.Add command-line options (-p for port, -h for help, -l for logging)
3.Modify to use coordinates from an OpenCV image detection routine (to support automated tracking)
4.Add UDP client timeout
