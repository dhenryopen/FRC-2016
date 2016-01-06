//
// ADXL345_server and ADXL345_client
// ~~~~~~~~~~~~~~~~~~
// These two programs "fuse" two different open source samples to create a UDP-based server (ADXL345_server) that broadcasts ADXL345 accelerometer data (X,Y,Z,Pitch,Roll) to a UDP client (ADXL345_client)
// The goal is to support testing with the Labview UDP VI (http:zone.ni.com/reference/en-XX/help/371361M-01/lvcomm/udp_vi_descriptions/) on a closed network (i.e., it is not secure)
//
// The server was developed and tested using a Beaglebone Green board with a Grove 3-Axis Digital Accelerometer on an I2C port: (http:www.seeedstudio.com/wiki/Grove_-_3-Axis_Digital_Accelerometer(%C2%B116g))
// The client was developed and tested on Ubuntu 14.04
//
// To-dos:
// 1.Port to NVIDIA Tegra TK1
// 2.Add command-line options (-p for port, -h for help, -l for logging)
// 3.Modify to use coordinates from an OpenCV image detection routine (to support automated tracking)
// 4.Add UDP client timeout
//
//
// Uses the following tutorial as a starting point for the UDP server: http://www.boost.org/doc/libs/1_59_0/doc/html/boost_asio/tutorial/tutdaytime5.html
// 
// Copyright (c) 2003-2015 Christopher M. Kohlhoff (chris at kohlhoff dot com)
//
// Distributed under the Boost Software License, Version 1.0. (See accompanying file LICENSE_1_0.txt or copy at http://www.boost.org/LICENSE_1_0.txt)
//

#include "ADXL345Accelerometer.h" // source: https://github.com/mahengunawardena/BeagleboneBlack_I2C_ADXL345.git
#include <iostream>
#include <string>
#include <sstream>
#include <boost/array.hpp>  // requires linking with boost_system and pthreads
#include <boost/asio.hpp>

using namespace std;
using boost::asio::ip::udp;

int main()
{
  try
  {
    boost::asio::io_service io_service;
    udp::socket socket(io_service, udp::endpoint(udp::v4(), 8081));

    ADXL345Accelerometer Accelerometer_Test(1, 0x53);
    cout<<"Sending data for device ID: "<< hex << Accelerometer_Test.getAccelerometer_ID()<<endl;
    Accelerometer_Test.SetPowerMode(0x01);
    Accelerometer_Test.getAccelerationData();

    for (;;)
    {
      boost::array<char, 1> recv_buf;
      udp::endpoint remote_endpoint;
      boost::system::error_code error;
      socket.receive_from(boost::asio::buffer(recv_buf),
          remote_endpoint, 0, error);

      if (error && error != boost::asio::error::message_size)
        throw boost::system::system_error(error);

      usleep(250000);
      Accelerometer_Test.getAccelerationData();

      std::stringstream readings;
      readings << "X:" << dec <<Accelerometer_Test.getAcceleration_X() << " Y:" << dec <<Accelerometer_Test.getAcceleration_Y() << " Z:" << dec <<Accelerometer_Test.getAcceleration_Z() << " Pitch: " << dec << Accelerometer_Test.getPitch() << " Roll: " << dec << Accelerometer_Test.getRoll()<<endl;

      std::string message = readings.str();

      boost::system::error_code ignored_error;
      socket.send_to(boost::asio::buffer(message),
          remote_endpoint, 0, ignored_error);
    }
  }
  catch (std::exception& e)
  {
    std::cerr << e.what() << std::endl;
  }

  return 0;
}

