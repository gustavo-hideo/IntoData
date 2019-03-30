# Leaflet basics - R

#devtools::install_github("rstudio/sparklyr")


library(tidyverse)
library(leaflet)
library(lubridate)

#devtools::install_github("rstudio/leaflet")
#chicago.raw <- readr::read_csv("https://query.data.world/s/gkcnmkzxw5xsr6xez4l2r4ufnld23g")



##########################################################
## Leaflet map with green and red data points (arrsted or not)
# Leaflet with percent of arrestment by coloring the map
# Higher type of crime by region
# Leaflet animation of changes over the years
# Arrest level by Crime type
# Arrestment level and crime type by Location Description
# Criminality over time
# Christmas/Thanksgiving decrease arrestment or criminality percent?
##########################################################



#chicago.r <- read_csv("C:/DataScience/Datasets/Chicago crimes/Crimes_-_2001_to_present.csv") %>%
 #     filter(Year == 2018, !is.na(Latitude))

chicago.r <- read_csv("C:/DataScience/Datasets/Chicago crimes/Crimes-2018.csv")

#chicago.r %>% write.csv("C:/DataScience/Datasets/Chicago crimes/Crimes-2018.csv", row.names=F)




chicago <- chicago.r %>%
      select(ID, `Case Number`, Date, `Primary Type`, Description, `Location Description`, Arrest
          ,`X Coordinate`, `Y Coordinate`, Year, Latitude, Longitude, Location, Block) %>%
      mutate(DateTime = mdy_hms(Date, tz = "America/Chicago")) %>%
      mutate(Month = month(DateTime)
          ,Date = ymd(as.Date(DateTime))
          ,Hour = hour(DateTime))






chicago.location <- chicago %>%
      select(Year, Block, Arrest, Longitude, Latitude) %>%
      group_by(Block, Arrest) %>%
      mutate(total = n()) %>%
      ungroup() %>%
      unique()




# Crimes in Chicago | March/2019

chicago %>%
      filter(`Primary Type` %in% c("ASSAULT", "CRIM SEXUAL ASSAULT", "KIDNAPPING", "HUMAN TRAFFICKING"
                                  ,"NARCOTICS", "WEAPONS VIOLATION", "SEX OFFENSE", "PROSTITUTION"
                                  ,"LIQUOR LAW VIOLATION", "OFFENSE INVOLVING CHILDREN", "MOTOR VEHICLE THEFT")) %>% 
      leaflet() %>%
      addProviderTiles(providers$Stamen.Toner) %>% 
      addCircleMarkers(Long = ~Longitude, Lat = ~Latitude
                      ,color =  ~ifelse(Arrest == T, "blue", "red")
                      ,radius = ~4, label = ~`Location Description`
                      ,group = ~`Primary Type`) %>% 
      addLayersControl(overlayGroups = ~`Primary Type`
                      ,options = layersControlOptions(collapsed = FALSE))

chicago %>%
      select(`Primary Type`, Arrest) %>%
      filter(`Primary Type` %in% c("ASSAULT", "CRIM SEXUAL ASSAULT", "KIDNAPPING", "HUMAN TRAFFICKING"
                                  ,"NARCOTICS", "WEAPONS VIOLATION", "SEX OFFENSE", "PROSTITUTION"
                                  ,"LIQUOR LAW VIOLATION", "OFFENSE INVOLVING CHILDREN", "MOTOR VEHICLE THEFT")) %>%
      group_by(`Primary Type`) %>%
      mutate(total.type = n()) %>%
      group_by(`Primary Type`, Arrest) %>%
      mutate(perc.arrest = n() / total.type) %>%
      ungroup() %>%
      unique() %>%
      arrange(`Primary Type`, Arrest)


      




chicago %>%
      leaflet() %>%
      addTiles() %>%
      addCircleMarkers(lng = ~Longitude, lat = ~Latitude, ~10^total/5
                   ,color = ~ifelse(Arrest == T, "blue", "red"))


chicago.location %>%
      leaflet() %>%
      addTiles() %>%
      leaflet.extras::addHeatmap(lng = ~Longitude, lat = ~Latitude, intensity = ~total,
             blur = 15, max = .1, radius = 15)
   