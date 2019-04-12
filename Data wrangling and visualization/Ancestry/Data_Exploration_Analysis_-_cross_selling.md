---
title: "DNA tests | ACOM - Cross selling"
author: "Gustavo H. H. Correa"
date: "March 19, 2019"
output:
  html_document:  
    keep_md: true
   # toc: true
    #toc_float: true
    code_folding: hide
    fig_height: 6
    fig_width: 12
    fig_align: 'center'
theme: cosmo
editor_options: 
  chunk_output_type: console
---




```r
# Loading libraries
library(tidyverse)
library(kableExtra)
library(formattable)
library(DataExplorer)
library(ggalt)
```






```r
# Loading data
#source_python("./prod analytics - python script.py")
data_raw <- read_csv("C:/DataScience/Others/Ancestry interview/prod analytics data.csv")
```



```r
# Cleaning Data
data <- data_raw %>% 
  filter(xsell_day_exact < 10000 | is.na(xsell_day_exact)) %>%   # Removing few outliers
  mutate(#daystogetresult_grp = parse_number(ifelse(daystogetresult_grp == ">10weeks", "11"
                                      #             ,ifelse(daystogetresult_grp == "-1", NA, daystogetresult_grp))),
         cross.sell = factor(ifelse(xsell_gsa == 1 & xsell_day_exact <= 120, 1, 0))) %>%
  mutate(cross.sell.date = as.Date(ordercreatedate) + xsell_day_exact
         #,weekstogetresult_grp = ifelse(daystogetresult_grp == "11", "10+", daystogetresult_grp))
         ,weekstogetresult_grp = ifelse(daystogetresult_grp == "-1", NA, daystogetresult_grp))

data$weekstogetresult_grp <- factor(data$weekstogetresult_grp, levels = c("1 week", "2 weeks", "3 weeks", "4 weeks", "5 weeks", "6 weeks", "7 weeks", "8 weeks", "9 weeks", "10 weeks", ">10weeks"))
```










```r
# Exploratory Analysis
introduce(data)
plot_missing(data)
plot_bar(data)
plot_histogram(data)
plot_correlation(na.omit(data %>% select(regtenure, customer_type_group, weekstogetresult_grp, dna_visittrafficsubtype, xsell_gsa, xsell_day_exact)))
plot_boxplot(data, by = "dna_visittrafficsubtype")
plot_scatterplot(data %>% select(weekstogetresult_grp, xsell_day_exact), by = "xsell_day_exact")
```





```r
theme.all <- theme(panel.background = element_blank()
                   ,plot.background = element_blank()
                   ,panel.grid = element_blank()
                   ,axis.title.y = element_blank()
                   #,axis.text.y = element_blank()
                   ,axis.ticks = element_blank())
```

<br>
<br>
<br>
<br>




#### Customer type and Period of time for DNA tests return
When customers get DNA tests sooner (1-4 weeks), they are more likely to also purchase ACOM (see `1 week` in the "time range to subscribe" graph and `1 week` until `4 weeks` in the line graph) <br>



```r
data %>%
  filter(xsell_gsa == 1, customer_type_group != "Acom Sub", !is.na(weekstogetresult_grp)) %>% 
  select(ordernumber, ordercreatedate, customer_type_group, weekstogetresult_grp, xsell_gsa, xsell_day_exact, cross.sell, cross.sell.date) %>%
  ggplot(aes(x = ordercreatedate, xend = cross.sell.date, y = ordernumber)) +
  geom_dumbbell(aes(color = cross.sell)) +
  scale_color_manual(values = c("gray45", "#9AC10E"), guide = F) +
  facet_grid(weekstogetresult_grp~customer_type_group) +
  theme.all +
  theme(axis.text.y = element_blank()) +
  labs(title = "Time range from purchasing DNA tests and ACOM subscription"
       ,subtitle = "The lines start in the order date and ends in the subscription date")
```

![](Data_Exploration_Analysis_-_cross_selling_files/figure-html/unnamed-chunk-6-1.png)<!-- -->

```r
data %>% 
  filter(xsell_gsa == 1, customer_type_group != "Acom Sub", !is.na(weekstogetresult_grp)) %>% 
  select(ordernumber, ordercreatedate, customer_type_group, weekstogetresult_grp, xsell_gsa, xsell_day_exact, cross.sell, cross.sell.date) %>% 
  group_by(weekstogetresult_grp) %>% 
  mutate(total.week = n()) %>% 
  group_by(weekstogetresult_grp, customer_type_group) %>% 
  mutate(total.ctype = n()) %>% 
  group_by(weekstogetresult_grp, customer_type_group, cross.sell) %>% 
  mutate(ratio = round((n() / total.ctype) * 100, 1)) %>% 
  ungroup() %>% 
  filter(cross.sell == 1) %>% 
  select(customer_type_group, weekstogetresult_grp, ratio) %>% 
  unique() %>% 
  #spread(customer_type_group, ratio) %>% 
  ggplot(aes(weekstogetresult_grp, ratio, group = customer_type_group)) +
  geom_line(aes(color = customer_type_group), size = 1) +
  scale_color_manual(values = c("gray45", "#9AC10E")) +
  theme.all +
  theme(axis.text.x = element_text(angle = 90, hjust = 1)
        ,axis.title.x = element_blank()) +
  labs(y = "Ratio (%)"
       ,title = "Cross-selling ratio"
       ,x = "Period of time | DNA tests results")
```

![](Data_Exploration_Analysis_-_cross_selling_files/figure-html/unnamed-chunk-6-2.png)<!-- -->

<br>
<br>
<br>
<br>

#### Long periods of DNA test's return does NOT affect ACOM cross-selling

```r
data %>% 
  filter(!is.na(weekstogetresult_grp), xsell_gsa == 1) %>% 
  select(ordernumber, weekstogetresult_grp, cross.sell) %>% 
  group_by(weekstogetresult_grp) %>% 
  mutate(total.week = n()) %>% 
  group_by(weekstogetresult_grp, cross.sell) %>% 
  mutate(total.cross.sell = n()) %>% 
  mutate(ratio = total.cross.sell / total.week) %>% 
  ungroup() %>% 
  select(-ordernumber) %>% 
  unique() %>% 
  ggplot(aes(cross.sell, ratio, fill = cross.sell)) +
  geom_bar(stat = "identity") +
  geom_text(aes(label = round(ratio, 2), y = ratio + .1, color = cross.sell, fontface = ifelse(cross.sell == 1 & weekstogetresult_grp %in% c(1, 9, 10, 11), "bold", "plain"))) +
  scale_fill_manual(values = c("gray45", "#9AC10E"), guide = F) +
  scale_color_manual(values = c("gray45", "#9AC10E"), guide = F) +
  facet_wrap(~weekstogetresult_grp) +
  theme.all +
  theme(axis.text.x = element_blank()) +
  labs(title = "Cross-selling ratio"
       ,x = "Period of time | DNA tests results")
```

![](Data_Exploration_Analysis_-_cross_selling_files/figure-html/unnamed-chunk-7-1.png)<!-- -->

<br>
<br>
<br>
<br>

#### DNA traffic channels that are more likely to cross-sell over all customers

```r
data %>%
  select(ordernumber, dna_visittrafficsubtype, xsell_gsa, cross.sell) %>% 
  filter(dna_visittrafficsubtype %in% c("Affiliate External", "content marketing", "direct core homepage", "direct non-homepage", "Email Campaigns", "geo-redirect", "iOS App", "organic nonbrand", "paid search - dna brand", "direct dna homepage", "email no source id", "External Paid Media", "organic core brand", "Paid Search GDN", "Email Programs", "external referrals", "internal referrals", "organic dna brand", "paid search - core brand", "social media organic")
         ,!is.na(dna_visittrafficsubtype)) %>%    #,xsell_gsa == 1)) %>% 
  group_by(dna_visittrafficsubtype) %>% 
  mutate(total.traffic = n()) %>% 
  group_by(dna_visittrafficsubtype, cross.sell) %>% 
  mutate(ratio = round((n() / total.traffic) * 100, 1)) %>% 
  select(-ordernumber) %>% 
  filter(cross.sell == 1) %>% 
  unique() %>%
  ggplot(aes(reorder(dna_visittrafficsubtype, ratio), ratio, fill = ratio)) +
  geom_bar(stat = "identity") +
  coord_flip() +
  scale_fill_gradient2(low = "gray30", high = "#9AC10E", guide = F) +
  theme.all +
  labs(y = "Subscription ratio (%)")
```

![](Data_Exploration_Analysis_-_cross_selling_files/figure-html/unnamed-chunk-8-1.png)<!-- -->

<br>
<br>


#### DNA traffic channels that are more likely to cross-sell only over customers whom subscribed to ACOM


```r
data %>%
  select(ordernumber, dna_visittrafficsubtype, xsell_gsa, cross.sell) %>% 
  filter(dna_visittrafficsubtype %in% c("Affiliate External", "content marketing", "direct core homepage", "direct non-homepage", "Email Campaigns", "geo-redirect", "iOS App", "organic nonbrand", "paid search - dna brand", "direct dna homepage", "email no source id", "External Paid Media", "organic core brand", "Paid Search GDN", "Email Programs", "external referrals", "internal referrals", "organic dna brand", "paid search - core brand", "social media organic")
         ,!is.na(dna_visittrafficsubtype), xsell_gsa == 1) %>% 
  group_by(dna_visittrafficsubtype) %>% 
  mutate(total.traffic = n()) %>% 
  group_by(dna_visittrafficsubtype, cross.sell) %>% 
  mutate(ratio = round((n() / total.traffic) * 100, 1)) %>% 
  select(-ordernumber) %>% 
  filter(cross.sell == 1) %>% 
  unique() %>%
  ggplot(aes(reorder(dna_visittrafficsubtype, ratio), ratio, fill = ratio)) +
  geom_bar(stat = "identity") +
  coord_flip() +
  scale_fill_gradient2(low = "gray30", high = "#9AC10E", guide = F) +
  theme.all +
  labs(y = "Subscription ratio (%)")
```

![](Data_Exploration_Analysis_-_cross_selling_files/figure-html/unnamed-chunk-9-1.png)<!-- -->



**Traffic channels** that are more effective on customers interested on subscribing to ACOM

  * Paid Search GDN
  * Direct non-homepage
  * Organic DNA brad
  * Affiliate External                                                                                           
  
  
  




















