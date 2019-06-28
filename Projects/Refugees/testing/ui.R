

library(shiny)
library(plotly)
library(ggiraph)

# Define UI for application that draws a histogram
shinyUI(fluidPage(
  
  # Application title
  titlePanel("Old Faithful Geyser Data"),
  
  # Sidebar with a slider input for number of bins 
  
    # Show a plot of the generated distribution
    mainPanel(
       ggiraphOutput("distPlot")
    )
  )
)
