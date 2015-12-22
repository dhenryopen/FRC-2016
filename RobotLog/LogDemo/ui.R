library(shiny)

shinyUI(pageWithSidebar(
    
    # Application title
    headerPanel("RoboRio Internal Metrics"),
    
    # Sidebar with controls to select the variable to plot against time
    # and to specify whether outliers should be included
    sidebarPanel(
        selectInput("variable", "Metric:",
                    list("Bus Utilization (%)" = "pct_bus_utilization", 
                         "CPU Low (%)" = "pct_cpu_low", 
                         "CPU Time Critical (%)" = "pct_cpu_time_critical", 
                         "Free RAM" = "ram_free"))
    ),
    
    # Show the caption and plot of the requested variable against time
    mainPanel(
        h3(textOutput("caption")),
        plotOutput("metricPlot")
    )
))
