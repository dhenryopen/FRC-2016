//
// ADXL345_server.cpp
// ~~~~~~~~~~
//
// Copyright (c) 2003-2015 Christopher M. Kohlhoff (chris at kohlhoff dot com)
//
// Distributed under the Boost Software License, Version 1.0. (See accompanying
// file LICENSE_1_0.txt or copy at http://www.boost.org/LICENSE_1_0.txt)
//

#include "ADXL345Accelerometer.h"
#include <iostream>
#include <string>
#include <sstream>
#include <boost/array.hpp>
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
    cout<<"Device ID : "<< hex << Accelerometer_Test.getAccelerometer_ID()<<endl;
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

// X Data :374 Y Data :-331 Z Data :-42    Pitch : 48      Roll : -41

      usleep(250000);
      Accelerometer_Test.getAccelerationData();
      std::stringstream ss;
      ss << "X:" << dec <<Accelerometer_Test.getAcceleration_X() << " Y:" << dec <<Accelerometer_Test.getAcceleration_Y() << " Z:" << dec <<Accelerometer_Test.getAcceleration_Z() << " Pitch: " << dec << Accelerometer_Test.getPitch() << " Roll: " << dec << Accelerometer_Test.getRoll()<<endl;
//      cout << ss.str() ;

      std::string stdstr = ss.str();
      cout << stdstr;

//      std::string message = "Message\n";

      std::string message = stdstr;

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

/*
// swapping ostringstream objects

#include <string>       // std::string

#include <iostream>     // std::cout

#include <sstream>      // std::stringstream



int main () {



  std::stringstream ss;
  ss << 100 << ' ' << 200;



  int foo,bar;

  ss >> foo >> bar;



  std::cout << "foo: " << foo << '\n';

  std::cout << "bar: " << bar << '\n';



  return 0;

}*/

