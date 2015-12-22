library(shiny)
library(datasets)
library(jsonlite)
library(ggplot2)
library(scales)

f <- "sample.json"

# parse the log and create a data frame

robotlog <- fromJSON(f)

# Concatenate date & time

t <- paste(robotlog$Date,robotlog$Time)

# convert to datetime and append to data frame

robotlog[,'datetime'] <- as.POSIXct(strptime(t, "%m/%d/%Y %H:%M:%OS"))  
robotlog[,'pct_bus_utilization'] <- as.numeric(robotlog$"% Bus Utilization")
robotlog[,'pct_cpu_low'] <- as.numeric(robotlog$"CPU % Low")
robotlog[,'pct_cpu_time_critical'] <- as.numeric(robotlog$"CPU % Time Crit")
robotlog[,'ram_free'] <- as.numeric(robotlog$"RAM Free")

