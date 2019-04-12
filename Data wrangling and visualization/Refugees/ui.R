#
# Refugees
#




library(shiny)
library(shinyWidgets)
library(leaflet)


ui <- fluidPage(theme = shinythemes::shinytheme("simplex"),
                
  tags$head(
    tags$style(HTML(".leaflet-container { background: #FFFFFF; }"))
  ),
  
  titlePanel("Refugees", windowTitle = "Refugees"),
  
  sidebarLayout(
    
    sidebarPanel(width = 2,
                 
        #shinythemes::themeSelector(), #simplex
                 
        wellPanel(
     
          
            selectInput(inputId = "year",
                        label = "Year:",
                        choices = years,
                        selected = "2016"),
            
            selectInput(inputId = "demographic",
                        label = "Demographics:",
                        choices = c("0-4", "5-11", "12-17", "18-59", "60+", "All"),
                        selected = "All"),
            
            pickerInput(inputId = "continent",
                        label = "Continent:",
                        choices = continents,
                        options = list(`actions-box` = T),   # pickerInput allows this option that incluse SELECT ALL
                        multiple = T,
                        selected = continents),
            
            pickerInput(inputId = "country",
                        label = "Countries:",
                        choices = countries,
                        multiple = T,
                        selected = countries,
                        options = list(`live-search` = T,
                                       `actions-box` = T))
            ),
        

      h5(htmlOutput(outputId = "total.ref.year")),
            
      br(),
      br(),
      br(),
      br(),
      br(),


      

      h5(img(src = "badge.png", height = "60px"), HTML("<font size = \"2\">Gustavo Hideo</font>"))
      
      
    ),
    
    
    mainPanel(width = 10,
      
      tabsetPanel(type = "tabs",
                  
        tabPanel("Origin",
                 fluidRow(
                     column(5,
                       leafletOutput(outputId = "origin.map", width = "100%")
                       ),
                     column(7,
                       plotOutput(outputId = "origin.scatterplot", width = "100%")
                       )
                 ),
                 fluidRow(
                    column(5,
                           plotOutput(outputId = "origin.general", width = "100%")
                           ),
                    column(7,
                           plotOutput(outputId = "origin.barplot", width = "100%")
                           )
                        )
                ),
              
        tabPanel("Destinations (demographics)",
                 fluidRow(
                   column(5,
                          leafletOutput(outputId = "country.map", width = "100%")
                   ),
                   column(7,
                          plotOutput(outputId = "country.scatterplot", width = "100%")
                   )
                 ),
                 fluidRow(
                   column(6,
                          plotOutput(outputId = "country.general", width = "100%")
                   ),
                   column(6,
                          plotOutput(outputId = "country.barplot", width = "100%")
                   )
                 )
        )
    )
    
  )
  
 )
)

