# **Interactive maps with R (leaflet)**

Create interactive maps in R using the `leaflet` package.

## **Libraries**
```r
library(tidyverse)
#devtools::install_github("rstudio/leaflet")
library(leaflet)
```

## **Loading dataset**
The dataset we are loading contains `longitude` and `latitude`.
```r
geo <- read_csv("https://www.accessdata.fda.gov/scripts/infantformula/InfantFormulaRecallList2010.xls")
```