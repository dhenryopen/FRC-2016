library(shiny)
library(datasets)
library(jsonlite)
library(ggplot2)
library(scales)
library(RCurl)

# Motor 0 ( plus or minus, forward or backwards )
# Current 12 (up to 40A, 3.5A observed)
# number of switches will vary
# Encoder 1 distance
# Limit switch
# 3-axis gyro with accelerometer
# 256MB 
# Jade


# LEGACY CODE

# f <- "sample-fix.json"
# robotlog <- fromJSON(f)

# JSON URL

urlfile <- 'http://frc-robolog.org:5000/dataset/435ff9a7-27e7-4cc3-b67d-eb6b15ade7ee/resource/5cd07f17-6655-45ef-87ca-2c8edeab9150/download/4918.test.t1.json'
robotlog <- fromJSON(urlfile)

# CSV URL

# urlfile <- 'http://frc-robolog.org:5000/dataset/435ff9a7-27e7-4cc3-b67d-eb6b15ade7ee/resource/76cff02c-29e6-4a15-9bd7-16f2c0fd4bcb/download/4918.test.t1.csv'
# robotlog <- read.csv(url(urlfile))

# Concatenate date & time

t <- paste(robotlog$Date,robotlog$Time)

# convert to datetime and append to data frame

robotlog[,'datetime'] <- as.POSIXct(strptime(t, "%m/%d/%Y %H:%M:%OS"))  
robotlog[,'pct_bus_utilization'] <- as.numeric(robotlog$"% Bus Utilization")
robotlog[,'pct_cpu_low'] <- as.numeric(robotlog$"CPU % Low")
robotlog[,'pct_cpu_time_critical'] <- as.numeric(robotlog$"CPU % Time Crit")
robotlog[,'ram_free'] <- as.numeric(robotlog$"RAM Free")
robotlog[,'motor_0'] <- as.numeric(robotlog$"Motor 0")
robotlog[,'current_12'] <- as.numeric(robotlog$"Current 12")
robotlog[,'encoder_1_distance'] <- as.numeric(robotlog$"Encoder 1 Distance")
robotlog[,'limit_1_value'] <- robotlog$"Limit 1 Value"
