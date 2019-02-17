# FORECASTING

library(tidyverse)
library(lubridate)
library(forecast)
library(fpp2)

## LOADING DATA
sales.raw <- read_csv("https://byuistats.github.io/M335/data/sales.csv") %>%
    filter(!is.na(Name), Name != "Missing")
tz(sales.raw$Time) <- "MST"   # Making sure it's in the correct time zone


# DATA WRANGLING
sales <- sales.raw %>%
    mutate(Year = year(Time)
          ,Month = month(Time)
          ,Week = week(Time)
          ,Day = day(Time)
          ,Hour = hour(Time)) %>%
    # SALES PER MONTH, WEEK, AND DAY
    group_by(Name, Month) %>%
    mutate(Amount.month = round(sum(Amount), 2)) %>%
    group_by(Name, Month, Week) %>%
    mutate(Amount.week = round(sum(Amount), 2)) %>%
    group_by(Name, Month, Day) %>%
    mutate(Amount.day = round(sum(Amount), 2)) %>%
    group_by(Name, Hour) %>%
    mutate(AVG.amount.hour = round(mean(Amount), 2)) %>%
    select(-Time, -Type, -Amount) %>%
    unique() %>%
    # RANGE OF HOURS WORKED
    group_by(Name, Month, Day) %>%
    mutate(Total.hours = max(as.numeric(Hour)) - min(as.numeric(Hour))) %>%
    ungroup()


sales.day <- sales %>%
    group_by(Name) %>%
    mutate(AVG.hours.day = mean(Total.hours)
          ,AVG.amount.day = mean(Amount.day)) %>%
    ungroup() %>%
    select(Name, AVG.hours.day, AVG.amount.day) %>%
    unique()
    


sales.week <- sales %>%
    select(Name, Month, Week, Day, Total.hours, Amount.day) %>%
    unique() %>%
    group_by(Name, Month, Week) %>%
    mutate(Total.hours.week = sum(Total.hours)
          ,Total.amount.week = sum(Amount.day)) %>%
    ungroup() %>%
    select(-Total.hours, -Amount.day, -Day) %>%
    unique() %>%
    group_by(Name) %>%
    mutate(AVG.hours.week = sum(Total.hours.week) / n()
          ,AVG.amount.week = sum(Total.amount.week) / n()) %>%
    ungroup() %>%
    select(Name, AVG.hours.week, AVG.amount.week) %>%
    unique()


sales.month <- sales %>%
    select(Name, Month, Day, Total.hours, Amount.day) %>%
    unique() %>%
    group_by(Name, Month) %>%
    mutate(Total.hours.month = sum(Total.hours)
          ,Total.amount.month = sum(Amount.day)) %>%
    select(-Total.hours, Amount.day, -Day) %>%
    unique() %>%
    group_by(Name) %>%
    mutate(AVG.hours.month = sum(Total.hours.month) / n()
          ,AVG.amount.month = sum(Total.amount.month) / n()) %>%
    ungroup() %>%
    select(Name, AVG.hours.month, AVG.amount.month) %>%
    unique()
   
  

# TABLE AVG HOURS
sales.table <- sales.day %>%
    left_join(sales.week, by = "Name") %>%
    left_join(sales.month, by = "Name") %>%
    rename()


xxx
    group_by(Name) %>%
    mutate(`Average hours/day` = round(mean(AVG.hours.day), 1)
          ,`Average amount/day` = round(mean(Amount.day), 2)

          ,`Average hours/week` = round(mean(AVG.hours.week),1)
          ,`Average amount/week` = round(mean(Amount.week), 2)

          ,`Average hours/month` = round(mean(AVG.hours.month), 1)
          ,`Average amount/month` = round(mean(Amount.month), 2)) %>%
    select(Name, `Average hours/day`:`Average amount/month`) %>%
    unique() %>% View()
