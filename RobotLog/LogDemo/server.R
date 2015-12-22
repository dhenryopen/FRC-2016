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
    
    # Render the table on the page
    
    output$tableData = renderDataTable({
        lower_bound <- input$slider[1]
        upper_bound <- input$slider[2]
        tableData <- robotlog[lower_bound:upper_bound,c("datetime","pct_bus_utilization","pct_cpu_low","pct_cpu_time_critical","ram_free")]
        colnames(tableData) <- c("Date / Time","Bus Utilization (%)","CPU Low (%)", "CPU Time Critical (%)","Free Ram")
        options(digits.secs=3)
        tableData
    })
    
    # Download the table (full data set bounded by slider)
    
    output$downloadData <- downloadHandler(
        filename = function() { 
           paste('robotlog', '.csv', sep='') },
        content = function(file) {
            lower_bound <- input$slider[1]
            upper_bound <- input$slider[2]
            tableData <- robotlog[lower_bound:upper_bound,c("Date","Time","FMS Present","E-Stop","Team Station","Countdown","Code Start","Brownout","Mode","Code?","Contoller Type","Error Strings","Robot IP","DB Mode","Event Name","Event Type","Event Number","Event Replay","Camera IP","Disk Free","RM Block","RAM Free","CPU % ISR","CPU % Time Crit","CPU % Time Str","CPU % High","CPU % Above","CPU % Normal","CPU % Low","% Bus Utilization","Bus off Cnt","TX_FIFO Full Count","Receive Error Cnt","Transmit Error Cnt","HID Outputs","Rumble Low","Rumble High")
]
            write.csv(tableData, file, row.names = FALSE)
        }
    )
})

