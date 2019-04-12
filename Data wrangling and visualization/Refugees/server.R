#
# Refugees
#




library(shiny)
library(shinyWidgets)
library(leaflet)




############
#  SERVER  #
############

server <- function(input, output) {

  
  
  ###
  #  Reactives | Refugees
  ###
  
  ref.selected <- reactive({
    req(input$year, input$continent, input$country)
    ref %>%
      filter(Year == input$year, Origin %in% input$country, Continent %in% input$continent)
  })
  
  
  
  
  
  map.ref <- reactive({
    tigris::geo_join(shp, ref.selected(), "NAME", "Origin")
    
    
  })
  
  
  totals.vector.ref <- reactive({
    ref.selected() %>%
      select(Value) %>%
      unique() %>%
      as.vector()
  })
  
  
  
  mypal.ref <- reactive({
    mypal.ref <- colorQuantile(c("#ffffcc", "#e60000"), na.color = "#FFFFEE", n = 10, domain = totals.vector.ref()$Value)
  })
  
  
  
  
  
  
  
  ###
  #  Outputs | Refugees
  ###
  
  
  # Refugees | Map
  output$origin.map <- renderLeaflet({
    
    map.ref() %>%  
      leaflet() %>%
      addProviderTiles("CartoDB.Positron",
                       options = providerTileOptions(minZoom = 1, maxZoom = 5, noWrap = T)) %>%
      
      addPolygons(
        
        fillColor = ~mypal.ref()(Value),
        stroke = FALSE, smoothFactor = 0.2, fillOpacity = 0.5,
        weight = 1,
        popup = paste0("Country: ", as.character(map.ref()$NAME), "<br>", "Total: ", as.character(map.ref()$Value))) %>% 
      setView(lng = 0,
              lat = 100,
              zoom = 1) %>% 
      setMaxBounds(lng1 = -180,
                   lat1 = 100,
                   lng2 = 180,
                   lat2 = -60)
    
  })
  
 
  
  
  
  
  # Refugees | Scatterplot
  output$origin.scatterplot <- renderPlot({
    ref.fl %>% 
      filter(Continent %in% input$continent, Origin %in% input$country) %>% 
      mutate(Outlier = ifelse(growth >= stats::quantile(growth, 0.8), "Higher", "Lower")) %>%
      mutate(Outlier = factor(Outlier, levels = c("Lower", "Higher"))) %>% 
      ggplot(aes(max.year, growth, color = Continent)) +
      geom_hline(yintercept = 0, linetype = "dashed", alpha = .5) +
      geom_point(aes(alpha = ifelse(Origin %in% input$country, 1, 0.2),
                     size = avg)) +
      rm.legend.alpha +
      rm.legend.size +
      facet_wrap(~Outlier, scales = "free") +
      colors +
      myTheme +
      labs(title = "Percent growth (2001-2016)",
           subtitle = "The size represents the average number of refugees",
           y = "",
           x = "Year of highest number of refugees")
  })
  
  
  
  
  # Refugees | General
  output$origin.general <- renderPlot({
    ref %>%
      filter(Origin %in% input$country, Continent %in% input$continent) %>% 
      group_by(Year) %>%
      summarise(total = sum(Value)) %>% 
      ggplot(aes(Year, total)) +
      geom_smooth(size = 1.3, se = F, color = "black") +
      myTheme +
      labs(y = "Total number of refugees")
    
  })
  
  
  
  
  
  
  # Refugees | Barplot  
  output$origin.barplot <- renderPlot({
    
    ref.selected() %>% 
      arrange(-Value) %>% 
      filter(Origin %in% input$country) %>% 
      head(20) %>% 
      ggplot(aes(x = reorder(Origin, Value), y = Value,
                 fill = Continent)) +
      geom_bar(stat = "identity", width = 0.3) +
      coord_flip() +
      fills +
      myTheme +
      labs(y = "Country of origin",
           x = "Number of refugees")
  })
  
  
  
  
  
  
  
  #####################################################
  
  
  
  
  
  ###
  #  Reactives | Demographics
  ###
  
  
  demo.gender <- reactive({
    req(input$demographic)
    demo %>%
      mutate(Female = case_when(input$demographic == "0-4" ~ demo$`Female 0-4`,
                                input$demographic == "5-11" ~ demo$`Female 5-11`,
                                input$demographic == "12-17" ~ demo$`Female 12-17`,
                                input$demographic == "18-59" ~ demo$`Female 18-59`,
                                input$demographic == "60+" ~ demo$`Female 60+`,
                                input$demographic == "All" ~ demo$`F: Total`),
             Male = case_when(input$demographic == "0-4" ~ demo$`Male 0-4`,
                              input$demographic == "5-11" ~ demo$`Male 5-11`,
                              input$demographic == "12-17" ~ demo$`Male 12-17`,
                              input$demographic == "18-59" ~ demo$`Male 18-59`,
                              input$demographic == "60+" ~ demo$`Male 60+`,
                              input$demographic == "All" ~ demo$`M: Total`))
  })
  
  
  
  demo.selected <- reactive({
    req(input$year, input$continent, input$country)
    demo.gender() %>%
      select(Year, Country, Continent, Female, Male) %>% 
      filter(Year == input$year, Country %in% input$country, Continent %in% input$continent) %>% 
      group_by(Year, Country) %>% 
      mutate(Total = sum(Female, Male, na.rm = T)) %>% 
      ungroup()
  })
  
  
  
  
  map.demo <- reactive({
    tigris::geo_join(shp, demo.selected(), "NAME", "Country")

      
  })
  
  
  totals.vector.demo <- reactive({
    demo.selected() %>%
      select(Total) %>%
      unique() %>%
      as.vector()
  })
  
  
  
  mypal <- reactive({
    mypal <- colorQuantile(c("#ffffcc", "#e60000"), na.color = "#FFFFEE", n = 10, domain = totals.vector.demo()$Total)
  })
  
  
  

  
  
  
  ###
  #  Outputs | Demographics
  ###

  
  # Demographic | Map
  output$country.map <- renderLeaflet({
    
    map.demo() %>%  
      leaflet() %>%
      addProviderTiles("CartoDB.Positron",
                       options = providerTileOptions(minZoom = 1, maxZoom = 5, noWrap = T)) %>%
      
      addPolygons(
        
                  fillColor = ~mypal()(Total),
                  stroke = FALSE, smoothFactor = 0.2, fillOpacity = 0.5,
                  weight = 1,
                  popup = paste0("Country: ", as.character(map.demo()$NAME), "<br>", "Total: ", as.character(map.demo()$Total))) %>% 
      setView(lng = 0,
              lat = 100,
              zoom = 1) %>% 
      setMaxBounds(lng1 = -180,
                   lat1 = 100,
                   lng2 = 180,
                   lat2 = -60)
                  
  })
  
  
  # Demographics | Scatterplot  
  output$country.scatterplot <- renderPlot({
    
    demo.selected() %>% 
      mutate(Outlier = ifelse(Total >= stats::quantile(Total, 0.8), "Higher", "Lower")) %>%
      mutate(Outlier = factor(Outlier, levels = c("Lower", "Higher"))) %>% 
      ggplot(aes(x = Female, y = Male,
                 color = Continent)) +
      geom_point(aes(alpha = ifelse(Country %in% input$country, 1, 0.2),
                     size = Total)) +
      rm.legend.alpha +
      rm.legend.size +
      facet_wrap(~Outlier, scales = "free") +
      colors +
      myTheme 
      
  })
  
  
  
  
  
  # Demographic | General
  output$country.general <- renderPlot({
    demo.gender() %>% 
      select(Year, Country, Continent, Female, Male) %>% 
      filter(Country %in% input$country, Continent %in% input$continent) %>% 
      mutate(Total = sum(Female, Male, na.rm = T)) %>% 
      unique() %>% 
      group_by(Year, Total) %>% 
      mutate(total = sum(Total)) %>% 
      select(Year, total) %>% 
      unique() %>% 
      ggplot(aes(Year, total)) +
      geom_smooth(size = 1.3, se = F, color = "black") +
      myTheme +
      labs(y = "Total number of refugees")
      
      
    
  })
  
  
  
  
  # Demographic | Barplot  
  output$country.barplot <- renderPlot({
    
    demo.selected() %>% 
      arrange(-Total) %>% 
      filter(Country %in% input$country) %>% 
      head(20) %>% 
      ggplot(aes(x = reorder(Country, Total), y = Total,
                 fill = Continent)) +
      geom_bar(stat = "identity", width = 0.3) +
      coord_flip() +
      fills +
      myTheme + 
      labs(y = "Countries receiving refugees",
           x = "Number of refugees")
  })
  
  
  
  
  
  
  
  #  | Totals
  output$total.ref.year <- renderUI({
    
    total.ref.year <- demo.gender() %>% 
      filter(Year == input$year) %>% 
      mutate(total = sum(sum(`F: Total`, na.rm = T), sum(`M: Total`, na.rm = T), na.rm = T)) %>%
      filter(Country %in% input$country, Continent %in% input$continent) %>% 
      mutate(filtered = sum(sum(Female, na.rm = T), sum(Male, na.rm = T), na.rm = T)) %>%
      select(total, filtered) %>%
      distinct(total, filtered)
    
    number <- paste("<strong>", format(as.numeric(total.ref.year$filtered), big.mark = ","), "/", "</strong>", format(as.numeric(total.ref.year$total), big.mark = ","))
    percent <- paste("<strong>", round((total.ref.year$filtered / total.ref.year$total) * 100, 1), "%", "</strong>")
    HTML(paste("Number of refugees:", number, " ", percent, "of all refugees for the period.", sep = '<br/>'))
    
    
  })
  
  

  
  
}




