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
robotlog[,'pct_cpu_time_critical'] <- as.numeric(robotlog$"CPU % Time Crit")
robotlog[,'pct_cpu_low'] <- as.numeric(robotlog$"CPU % Low")
robotlog[,'pct_bus_utilization'] <- as.numeric(robotlog$"% Bus Utilization")
robotlog[,'ram_free'] <- as.numeric(robotlog$"RAM Free")

ggplot(robotlog, aes(datetime, pct_cpu_time_critical, colour=Mode)) + 
    geom_line(size = 1) +
    xlab("Time (ms)") + ylab("CPU % Time Critical") +
    theme_bw() +
    scale_x_datetime(breaks=date_breaks("10 sec")) + 
  stat_smooth(method="loess")

ggplot(robotlog, aes(datetime, pct_cpu_low, colour=Mode)) + 
    geom_line(size = 1) +
    xlab("Time (ms)") + ylab("CPU % Low") +
    theme_bw() +
    scale_x_datetime(breaks=date_breaks("10 sec")) + 
  stat_smooth(method="loess")

ggplot(robotlog, aes(datetime, pct_bus_utilization, colour=Mode)) + 
    geom_line(size = 1) +
    xlab("Time (ms)") + ylab("% Bus Utilization") +
    theme_bw() +
    scale_x_datetime(breaks=date_breaks("10 sec")) + 
    stat_smooth(method="loess")

ggplot(robotlog, aes(datetime, ram_free, colour=Mode)) + 
    geom_line(size = 1) +
    xlab("Time (ms)") + ylab("RAM Free") +
    theme_bw() +
    scale_x_datetime(breaks=date_breaks("10 sec")) + 
  stat_smooth(method="loess")
