library(shiny)

# Need to tie this variable to an API call:

nrecords = as.integer(597)

shinyUI(pageWithSidebar(

    # Application title
  
    headerPanel("Robot Log Metrics"),
    
    # Sidebar with controls to select the variable to plot against time

    sidebarPanel(
        selectInput("variable", "Metric:",
                    list("Bus Utilization (%)" = "pct_bus_utilization", 
                         "CPU Low (%)" = "pct_cpu_low", 
                         "CPU Time Critical (%)" = "pct_cpu_time_critical", 
                         "Free RAM" = "ram_free")),
   
        sliderInput("slider", label = "Record Range:", min = 1, 
                    max = nrecords, value = c(1,nrecords))    
    ),
    
    # Show the caption and plot of the requested variable against time
    
    mainPanel(
        h3(textOutput("caption")),
        plotOutput("metricPlot")
    )
))
