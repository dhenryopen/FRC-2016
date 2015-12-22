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

shinyServer(function(input, output) {
    
    output$metricPlot <- renderPlot(function() {

      if(input$variable == "pct_bus_utilization"){
        plotData <- data.frame(var1 = robotlog$datetime, var2 = robotlog$pct_bus_utilization, Mode = robotlog$Mode)
        ylabel = "Bus Utilization (%)"
      } else if(input$variable == "pct_cpu_low"){
        plotData <- data.frame(var1 = robotlog$datetime, var2 = robotlog$pct_cpu_low, Mode = robotlog$Mode)
        ylabel = "CPU Low (%)"      
      } else if(input$variable == "pct_cpu_time_critical"){
        plotData <- data.frame(var1 = robotlog$datetime, var2 = robotlog$pct_cpu_time_critical, Mode = robotlog$Mode)
        ylabel = "CPU Time Critical (%)"
      } else {
        plotData <- data.frame(var1 = robotlog$datetime, var2 = robotlog$ram_free, Mode = robotlog$Mode)
        ylabel = "Free RAM"      
      }

      p <- ggplot(plotData, aes(var1, var2, colour=Mode)) + 
          geom_line(size = 1) +
          xlab("Time (ms)") + 
          ylab(ylabel) +
          theme_bw() +
          scale_x_datetime(breaks=date_breaks("10 sec")) + 
          stat_smooth(method="loess") 
      print(p)
      })
})

