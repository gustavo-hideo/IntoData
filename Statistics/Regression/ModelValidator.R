

# Creating train/test data

keep <- sample(1:nrow(d2), nrow(d2)*.6)

train <- d2[keep, ]
test <- d2[-keep, ]


# Applying model in test data

lm2v <- lm(SalePrice ~ Neighborhood + OverallQual + X2ndFlrSF +  X1stFlrSF + TotalBsmtSF + BsmtUnfSF +  YearRemodAdd + Neighborhood:YearRemodAdd + Neighborhood:OverallQual + KitchenAbvGr:GarageArea + KitchenAbvGr:TotalBsmtSF + Neighborhood2:GarageArea + Neighborhood:X1stFlrSF,
           data = test)

pander::pander(summary(lm2v))




# Calculating Adj.R-Squared from predictions

# ynew
ynew <- test$SalePrice

# y-hat for the model
yh2 <- predict(lm2, newdata = data.frame(test))

# y-bar
ybar <- mean(ynew)

# SSTO
ssto <- sum( (ynew - ybar)^2 )

# SSE
sse <- sum( (ynew - yh2)^2 )

# R-squared
r2 <- 1 - sse/ssto

# Adjusted r-squared
n <- length(ynew)
p <- length(coef(lm2))
r2a <- 1 - (n - 1) / (n - p) * sse/ssto




