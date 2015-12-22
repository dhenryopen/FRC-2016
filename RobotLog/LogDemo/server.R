library(shiny)
library(datasets)
library(jsonlite)
library(ggplot2)
library(scales)

shinyServer(function(input, output) {
    
    output$metricPlot <- renderPlot({

      # setup the plot based on the input variable
      
      if(input$variable == "pct_bus_utilization"){
        plotData <- data.frame(var1 = robotlog$datetime, var2 = robotlog$pct_bus_utilization, Mode = robotlog$Mode)
        ylabel = "Bus Utilization (%)\n"
      } else if(input$variable == "pct_cpu_low"){
        plotData <- data.frame(var1 = robotlog$datetime, var2 = robotlog$pct_cpu_low, Mode = robotlog$Mode)
        ylabel = "CPU Low (%)\n"      
      } else if(input$variable == "pct_cpu_time_critical"){
        plotData <- data.frame(var1 = robotlog$datetime, var2 = robotlog$pct_cpu_time_critical, Mode = robotlog$Mode)
        ylabel = "CPU Time Critical (%)\n"
      } else {
        plotData <- data.frame(var1 = robotlog$datetime, var2 = robotlog$ram_free, Mode = robotlog$Mode)
        ylabel = "Free RAM\n"      
      }
      
      # trim plotData by the input slider parameters
      
      num_obs <- nrow(plotData)  # should correspond to nrecords variable in ui.R
      lower_bound <- input$slider[1]
      upper_bound <- input$slider[2]
      plotData <- plotData[lower_bound:upper_bound,]

      # plot the data
      
      p <- ggplot(plotData, aes(var1, var2, colour=Mode)) + 
          geom_line(size = 1) +
          xlab("Time (ms)") + 
          ylab(ylabel) +
          theme_bw() +
          scale_x_datetime(breaks=date_breaks("15 sec")) + 
          stat_smooth(method="loess") 
    
      print(p)
      })
})
