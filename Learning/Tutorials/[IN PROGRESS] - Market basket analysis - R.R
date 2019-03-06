
# MARKET BASKET ANALYSIS
## Finding patterns using Association Rules

library(tidyverse)
library(arules)


# The Complete Journey
# http://www.dunnhumby.com/careers/engineering/sourcefiles?sourcefile=https%3A//www.dunnhumby.com/sites/default/files/sourcefiles/dunnhumby_The-Complete-Journey.zip

# LOADING DATASETS
data <- read_csv("C:/DataScience/Datasets/Grocery/dunnhumby - The Complete Journey CSV/transaction_data.csv")

products <- read_csv("C:/DataScience/Datasets/Grocery/dunnhumby - The Complete Journey CSV/product.csv") %>%
    select(PRODUCT_ID, DEPARTMENT, COMMODITY_DESC, SUB_COMMODITY_DESC) %>%
    filter(!DEPARTMENT %in% c("ELECT &PLUMBING", "GM MERCH EXP", "KIOSK-GAS", "MISC SALES TRAN", "MISC. TRANS."
                             ,"PHARMACY SUPPLY", "POSTAL CENTER", "PROD-WHS SALES", "AUTOMOTIVE", "CHARITABLE CONT"
                             ,"CHEF SHOPPE", "CNTRL/STORE SUP", "COUP/STR & MFG", "DAIRY DELI", "DELI/SNACK BAR"
                             ,"FROZEN GROCERY", "GM MERCH EXP", "GRO BAKERY", "HBC", "HOUSEWARES", "KIOSK-GAS"
                             ,"MEAT-WHSE", "PHOTO", "PORK", "RX", "SALAD BAR", "TOYS", "VIDEO", "VIDEO RENTAL")
           ,COMMODITY_DESC != "NO COMMODITY DESCRIPTION"
           ,SUB_COMMODITY_DESC != "NO SUBCOMMODITY DESCRIPTION")


# PREPARING DATA

# Merging to get data with products names
data.prod <- data %>%
    inner_join(products, by = "PRODUCT_ID") %>%
    select(BASKET_ID, SUB_COMMODITY_DESC) %>% #COMMODITY_DESC,)
    write_csv("C:/DataScience/Datasets/Grocery/dunnhumby - The Complete Journey CSV/tidydata.csv")

# Converting data to transaction type (sparse matrix)
transactions <- read.transactions("C:/DataScience/Datasets/Grocery/dunnhumby - The Complete Journey CSV/tidydata.csv"
                                ,format = "single"
                                ,sep = ","
                                ,cols = c("BASKET_ID", "SUB_COMMODITY_DESC"))

# DESCRIPTIVE ANALYSIS
summary(transactions)   # general summary of items
inspect(transaction[1:5])   # returns the first 5 transactions
itemFrequency(transaction[, 1:3])   # support level of the 3 first items
itemFrequencyPlot(transaction, support = 0.1)   # items with at least 10% support level
itemFrequencyPlot(transaction, topN = 20)  # top N support level items
image(sample(transaction, 100))   # plotting sample of the sparse matrix


# MODEL
transactions.rules <- apriori(transaction, parameter = list(support = 0.003
                                                           ,confidence = 0.25
                                                           ,minlen = 2))


summary(transactions.rules)
inspect(sort(transactions.rules, by = "lift")[1:100])


# NO MILK AND BANANAS AND CHEESE
nomilk.rules <- subset(transactions.rules, !items %in% c("FLUID MILK WHITE ONLY", "BANANAS", "MAINSTREAM", "SHREDDED CHEESE"))
inspect(sort(nomilk.rules, by = "lift"))


 #{PASTA: CANNED}                  => {KIDS CEREAL}  
 #{ASEPTIC PACK JUICE AND DRINKS}  => {KIDS CEREAL} 
 #{PRESERVES JAM MARMALADE}        => {PEANUT BUTTER}                  0.003273329  0.3032210 11.659308   819
 #{BAGELS}                         => {CREAM CHEESE}                   0.005155793  0.3592314 10.634304  1290
 #{SKILLET DINNERS}                => {TUNA}                           0.003549104  0.2504937  9.323790   888
 #{FRUIT SNACKS}                   => {KIDS CEREAL}                    0.004696168  0.3106001  6.037866  1175
 #{HAMBURGER BUNS, SOFT DRINKS 12/18&15PK CAN CAR} => {POTATO CHIPS}                   0.003365254  0.3459326  4.765649   842




