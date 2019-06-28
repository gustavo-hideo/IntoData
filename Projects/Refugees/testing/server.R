library(shiny)
library(plotly)
library(ggiraph)

# Define server logic required to draw a histogram
shinyServer(function(input, output) {
   
  output$distPlot <- renderggiraph({
    
    p <- mtcars %>% 
      ggplot(aes(wt, mpg)) +
      geom_point_interactive(aes(tooltip = gear))
    
    girafe(code = print(p))
    
  })
  
})
