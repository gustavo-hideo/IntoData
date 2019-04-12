# REFUGEES DEMOGRAPHICS

library(tidyverse)





########
# Refugees
########

# DATA WRANGLING
ref.raw <- read_csv("./www/Sample_time_series.csv") %>%
  rename("Year" = year
         ,"Origin" = origin
         ,"Value" = value)




ref <- ref.raw %>%
  mutate(Origin = case_when(grepl("China", Origin) ~ "China"
                             ,grepl("Bolivia", Origin) ~ "Bolivia"
                             ,grepl("Central African Rep.", Origin) ~ "Central African Republic"
                             ,grepl("Serbia and ", Origin) ~ "Serbia"
                             ,Origin == "Cabo Verde" ~ "Cape Verde"
                             ,Origin == "Côte d'Ivoire" ~ "Cote d'Ivoire"
                             ,Origin == "Czech Rep." ~ "Czech Republic"
                             ,Origin == "Dem. People's Rep. of Korea" ~ "Korea, Democratic People's Republic of"
                             ,Origin == "Dem. Rep. of the Congo" ~ "Democratic Republic of the Congo"
                             ,Origin == "Dominican Rep." ~ "Dominican Republic"
                             ,Origin == "Iran (Islamic Rep. of)" ~ "Iran (Islamic Republic of)"
                             ,Origin == "Lao People's Dem. Rep." ~ "Lao People's Democratic Republic"
                             ,Origin == "Libya" ~ "Libyan Arab Jamahiriya"
                             ,Origin == "Micronesia (Federated States of)" ~ "Micronesia, Federated States of"
                             ,Origin == "Rep. of Korea" ~ "Korea, Republic of"
                             ,Origin == "Rep. of Moldova" ~ "Republic of Moldova"
                             ,Origin == "Russian Federation" ~ "Russia"
                             ,Origin == "South Sudan" ~ "Sudan"
                             ,Origin == "State of Palestine" ~ "Palestine"
                             ,Origin == "United Rep. of Tanzania" ~ "United Republic of Tanzania"
                             ,Origin == "Syrian Arab Rep." ~ "Syrian Arab Republic"
                             ,Origin == "United States of America" ~ "United States"
                             ,Origin == "Venezuela (Bolivarian Republic of)" ~ "Venezuela"
                             ,TRUE ~ Origin)) %>%
  group_by(Year, Origin) %>%
  summarise(Value = sum(Value, na.rm = T)) %>%
  ungroup() %>% 
  unique() %>%
  mutate(Continent = countrycode::countrycode(sourcevar = Origin
                                              ,origin = "country.name"
                                              ,destination = "continent"))




ref.a <- ref %>% 
  filter(Value > 0) %>% 
  group_by(Origin, Continent) %>% 
  mutate(year.pos = ifelse(Year == min(Year), "first", ifelse(Year == max(Year), "last", NA))) %>%  
  filter(!is.na(year.pos)) %>% 
  spread(year.pos, Value) %>% 
  select(Origin, Continent, first, last) %>% 
  summarise_each(funs(max = max(., na.rm = TRUE))) %>% 
  ungroup() %>% 
  arrange(Origin, Continent) %>% 
  mutate(growth = round(((last_max / first_max) - 1) * 100, 0)) %>% 
  select(-first_max, -last_max) %>% 
  filter(growth != 0 , !is.infinite(growth))


ref.fl <- ref %>% 
  left_join(ref.a, by = c("Origin" = "Origin", "Continent" = "Continent")) %>% 
  arrange(Origin, Continent) %>% 
  group_by(Origin, Continent) %>% 
  mutate(max.year = ifelse(Value == max(Value), Year, NA),
         avg = round(mean(Value), 0)) %>% 
  ungroup() %>% 
  select(-Year, -Value) %>% 
  filter(!is.na(max.year), !is.na(growth))




# Vectors to be used in dash
years.ref <- min(ref$Year):max(ref$Year)
continents.ref <- as.character(levels(factor(ref$Continent)))
origins.ref <- as.character(levels(factor(ref$Origin)))










########
# Demographics
########

# DATA WRANGLING
demographics.raw <- read_csv("./www/demographics.csv"
                             ,col_types = list(
                               Year = col_integer(),
                               `Country / territory of asylum/residence` = col_character(),
                               `Location Name` = col_character(),
                               `Female 0-4` = col_double(),
                               `Female 5-11` = col_double(),
                               `Female 5-17` = col_double(),
                               `Female 12-17` = col_double(),
                               `Female 18-59` = col_double(),
                               `Female 60+` = col_double(),
                               `F: Unknown` = col_double(),
                               `F: Total` = col_double(),
                               `Male 0-4` = col_double(),
                               `Male 5-11` = col_double(),
                               `Male 5-17` = col_double(),
                               `Male 12-17` = col_double(),
                               `Male 18-59` = col_double(),
                               `Male 60+` = col_double(),
                               `M: Unknown` = col_double(),
                               `M: Total` = col_double() )) %>% 
  rename("Country" = `Country / territory of asylum/residence`)





demo <- demographics.raw %>% 
  select(Year, Country
         ,`Female 0-4`, `Female 5-11`, `Female 12-17`, `Female 18-59`, `Female 60+`
         ,`Male 0-4`, `Male 5-11`, `Male 12-17`, `Male 18-59`, `Male 60+`
         ,`F: Total`, `M: Total`) %>%
  mutate(Year = as.integer(Year),
         Country = case_when(grepl("China", Country) ~ "China"
                           ,grepl("Bolivia", Country) ~ "Bolivia"
                           ,grepl("Central African Rep.", Country) ~ "Central African Republic" 
                           ,grepl("Serbia and ", Country) ~ "Serbia"                                                        
                           ,Country == "Cabo Verde" ~ "Cape Verde"
                           #,Country == "C?te d'Ivoire" ~ "Cote d'Ivoire"
                           ,Country == "Czech Rep." ~ "Czech Republic"
                           ,Country == "Dem. People's Rep. of Korea" ~ "Korea, Democratic People's Republic of"
                           ,Country == "Dem. Rep. of the Congo" ~ "Democratic Republic of the Congo"
                           ,Country == "Dominican Rep." ~ "Dominican Republic"
                           ,Country == "Iran (Islamic Rep. of)" ~ "Iran (Islamic Republic of)"
                           ,Country == "Lao People's Dem. Rep." ~ "Lao People's Democratic Republic"
                           ,Country == "Libya" ~ "Libyan Arab Jamahiriya"
                           ,Country == "Micronesia (Federated States of)" ~ "Micronesia, Federated States of"
                           ,Country == "Rep. of Korea" ~ "Korea, Republic of"
                           ,Country == "Rep. of Moldova" ~ "Republic of Moldova"
                           ,Country == "Russian Federation" ~ "Russia"
                           ,Country == "South Sudan" ~ "Sudan"
                           ,Country == "State of Palestine" ~ "Palestine"
                           ,Country == "United Rep. of Tanzania" ~ "United Republic of Tanzania"
                           ,Country == "Syrian Arab Rep." ~ "Syrian Arab Republic"
                           ,Country == "United States of America" ~ "United States"
                           ,Country == "Venezuela (Bolivarian Republic of)" ~ "Venezuela"
                           ,TRUE ~ Country)) %>%
  mutate(Continent = countrycode::countrycode(sourcevar = Country
                                              ,origin = "country.name"
                                              ,destination = "continent")) %>% 
  group_by(Year, Country, Continent) %>% 
  summarise(`Female 0-4` = sum(`Female 0-4`, na.rm = T),
            `Female 5-11` = sum(`Female 5-11`, na.rm = T),
            `Female 12-17` = sum(`Female 12-17`, na.rm = T),
            `Female 18-59` = sum(`Female 18-59`, na.rm = T),
            `Female 60+` = sum(`Female 60+`, na.rm = T),
            `Male 0-4` = sum(`Male 0-4`, na.rm = T),
            `Male 5-11` = sum(`Male 5-11`, na.rm = T),
            `Male 12-17` = sum(`Male 12-17`, na.rm = T),
            `Male 18-59` = sum(`Male 18-59`, na.rm = T),
            `Male 60+` = sum(`Male 60+`, na.rm = T),
            `F: Total` = sum(`F: Total`, na.rm = T),
            `M: Total` = sum(`M: Total`, na.rm = T)) %>% 
  ungroup() %>% 
  unique()




# Vectors to be used in dash
years <- min(demo$Year):max(demo$Year)
continents <- as.character(levels(factor(demo$Continent)))
countries <- as.character(levels(factor(demo$Country)))






# Global for plots

options(scipen = 999)


colors.a <- c("Americas" = "darkseagreen4",
            "Europe" = "steelblue",
            "Africa" = "slateblue1",
            "Asia" = "yellow3",
            "Oceania" = "tomato")
colors <- scale_color_manual(values = colors.a)
fills <-  scale_fill_manual(values = colors.a, guide = F)
#colors <-  scale_color_brewer(palette = "Set1")
#fills <-  scale_fill_brewer(palette = "Set1", guide = F)

myTheme <- theme(panel.background = element_blank(),
                 #plot.background = element_rect(fill = "black", colour = "black"),
                 plot.background = element_blank(),
                 panel.grid = element_blank(),
                 #axis.text = element_text(colour = "white"),
                 legend.background = element_blank(),
                 #legend.key = element_rect(fill = "black", colour = "black"),
                 #legend.text = element_text(colour = "white"),
                 legend.title = element_blank(), 
                 legend.position = "bottom")

rm.legend.alpha <- scale_alpha(guide = 'none')
rm.legend.size <- scale_size(guide = 'none')


# LNG and LAT
#
#shp <- rgdal::readOGR("C:/DataScience/IntoData/Data wrangling and visualization/Refugees/www/TM_WORLD_BORDERS_SIMPL-0.3.shp")
#shp <- rgdal::readOGR("www/TM_WORLD_BORDERS_SIMPL-0.3.shp")
#shp <- rgdal::readOGR(dsn = path.expand("~/shp"), layer = "TM_WORLD_BORDERS_SIMPL-0.3")
#shp <- raster::shapefile("~/shp/TM_WORLD_BORDERS_SIMPL-0.3.shp")
shp <- rgdal::readOGR("./shp/TM_WORLD_BORDERS_SIMPL-0.3.shp")     
#f <- system.file("shp/TM_WORLD_BORDERS_SIMPL-0.3.shp", package="raster")
#file.exists(f)





