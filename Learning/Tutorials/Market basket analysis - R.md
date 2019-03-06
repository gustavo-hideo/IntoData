---
title: "Market basket analysis"
author: "Gustavo Hideo Higa Correa"
date: "February 19, 2019"
output:
  html_document:  
    keep_md: true
    toc: true
    toc_float: true
    code_folding: hide
    fig_height: 6
    fig_width: 12
    fig_align: 'center'
theme: cosmo
editor_options: 
  chunk_output_type: console
---


```{r}
transactional.data.path <- "C:/DataScience/Datasets/Grocery/dunnhumby - The Complete Journey CSV/transaction_data.csv"

product.path <- "C:/DataScience/Datasets/Grocery/dunnhumby - The Complete Journey CSV/product.csv"

tosave.path <- "C:/DataScience/Datasets/Grocery/dunnhumby - The Complete Journey CSV/tidydata.csv"

```



## Finding patterns using Association Rules

**Association rule** is a rule-based machine learning method for discovering interesting relations between variables in large databases.

```{r}
library(tidyverse)
library(arules)
```


#### Dowloading and loading the dataset
Detailed information of the dataset: [dunnhumby](https://www.dunnhumby.com/careers/engineering/sourcefiles) "The Complete Journey" <br>

Loading the data with transactions:

```{r}
data <- read_csv(transactional.data.path)
```
<br>

Loading the list of `PRODUCTS` removing categories with low importance:
```{r}
products <- read_csv(product.path) %>%
    select(PRODUCT_ID, DEPARTMENT, COMMODITY_DESC, SUB_COMMODITY_DESC) %>%
    filter(!DEPARTMENT %in% c("ELECT &PLUMBING", "GM MERCH EXP", "KIOSK-GAS", "MISC SALES TRAN", "MISC. TRANS."
                             ,"PHARMACY SUPPLY", "POSTAL CENTER", "PROD-WHS SALES", "AUTOMOTIVE", "CHARITABLE CONT"
                             ,"CHEF SHOPPE", "CNTRL/STORE SUP", "COUP/STR & MFG", "DAIRY DELI", "DELI/SNACK BAR"
                             ,"FROZEN GROCERY", "GM MERCH EXP", "GRO BAKERY", "HBC", "HOUSEWARES", "KIOSK-GAS"
                             ,"MEAT-WHSE", "PHOTO", "PORK", "RX", "SALAD BAR", "TOYS", "VIDEO", "VIDEO RENTAL")
           ,COMMODITY_DESC != "NO COMMODITY DESCRIPTION"
           ,SUB_COMMODITY_DESC != "NO SUBCOMMODITY DESCRIPTION")
```
<br>

### Preparing data
Merging transactions and products' names; <br>
Saving as `.csv` to read later using `read.transactions()`

```{r}
data.prod <- data %>%
    inner_join(products, by = "PRODUCT_ID") %>%
    select(BASKET_ID, SUB_COMMODITY_DESC) %>%
    write_csv(tosave.path)
```
<br>

Converting dataframe to `sparse matrix`:

```{r}
transactions <- read.transactions(tosave.path
                                ,format = "single"  # the format of the dataframe is long, not wide
                                ,sep = ","
                                ,cols = c("BASKET_ID", "SUB_COMMODITY_DESC"))
```
<br>

Now we have the data ready to be used for `market basket analysis`
<br>

### Basic concepts

* **Support**
  * measures how frequently it occurs in the data
 $${support(X)} = {{count(X)} \over {N}}$$

* **Confidence**
  * measures the predictive power or accuracy
 $${confidence(X->Y)} = {{support(X,Y)} \over {support(X)}}$$

* **Lift**
  * measures how much likely one item is to be purchased relative to its typical purchase rate, given that you know another item has been purchased.
$${lift(X->Y)} = {{confidence(X,Y)} \over {support(Y)}}$$

### Descriptive analysis

General summary of items
```{r}
summary(transactions)
```
<br>

First 5 transactions
```{r}
inspect(transaction[1:5])
```
<br>

Support level of the 3 first items
```{r}
itemFrequency(transaction[, 1:3])
```
<br>

Items with at least 10% support level
```{r}
itemFrequencyPlot(transaction, support = 0.1)
```
<br>

Top 20 support level items
```{r}
itemFrequencyPlot(transaction, topN = 20)
```
<br>

Plotting sample of the sparse matrix
```{r}
image(sample(transaction, 100))
```
<br>


### Creating the model
```{r}
transactions.rules <- apriori(transaction
    ,parameter = list(support = 0.003  # minimum support
    ,confidence = 0.25  # minimum confidence
    ,minlen = 2))  # minimum number of items per rule
```
<br>
Model description
```{r}
summary(transactions.rules)
```
<br>

Sorting by lift (first 100)
```{r}
inspect(sort(transactions.rules, by = "lift")[1:100])
```
<br>


### Improving model
Removing products that are purchased too often

```{r}
nomilk.rules <- subset(transactions.rules, !items %in% c("FLUID MILK WHITE ONLY", "BANANAS", "MAINSTREAM", "SHREDDED CHEESE"))
```
<br>

#### Interesting findings:
* Those who buy <span style="color:blue">Preservers jam marmalade</span> are **`11.7`** times more likely to also buy <span style="color:green">Peanut butter</span>
* Those who buy <span style="color:blue">Bagels</span> are **`10.6`** times more likely to also buy <span style="color:green">Cream cheese</span>
* Those who buy <span style="color:blue">Skillet dinners</span> are **`9.3`** times more likely to also buy <span style="color:green">Tuna</span>
* Those who buy <span style="color:blue">Fruit snacks</span> are **`6.03`** times more likely to also buy <span style="color:green">Kids cereal</span>
* Those who buy <span style="color:blue">Hamburger buns</span> and `Soft drinks can` are **`4.8`** times more likely to also buy <span style="color:green">Potato chips</span>
<br>

```{r}
inspect(sort(nomilk.rules, by = "lift"))
```














