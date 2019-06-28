library(tidyverse)


## Simulating Data from a Regression Model
## This R-chunk is meant to be played in your R Console.
## It allows you to explore how the various elements
## of the regression model combine together to "create"
## data and then use the data to "re-create" the line.

set.seed(101) #Allows us to always get the same "random" sample
#Change to a new number to get a new sample

n <- 300 #set the sample size

X_i <- runif(n, 12, 45) 
#Gives n random values from a uniform distribution between 15 to 45.

beta0 <- 8 #Our choice for the y-intercept. 

beta1 <- 55 #Our choice for the slope. 

beta2 <- -1.1

sigma <- 180.5 #Our choice for the std. deviation of the error terms.


epsilon_i <- rnorm(n, 0, sigma) 
#Gives n random values from a normal distribution with mean = 0, st. dev. = sigma.

Y_i <- beta0 + beta1*X_i + beta2*X_i^2 + epsilon_i 
#Create Y using the normal error regression model

fabData <- data.frame(y=Y_i, x=X_i) 
#Store the data as data

#View(fabData) 


#In the real world, we begin with data (like fabData) and try to recover the model that 
# (we assume) was used to created it.

fab.lm <- lm(y ~ x + I(x^2), data=fabData) #Fit an estimated regression model to the fabData.

summary(fab.lm) #Summarize your model. 

#plot(y ~ x, data=fabData) #Plot the data.

#abline(fab.lm) #Add the estimated regression line to your plot.


# Now for something you can't do in real life... but since we created the data...

#abline(beta0, beta1, lty=2) 
#Add the true regression line to your plot using a dashed line (lty=2). 

#legend("topleft", legend=c("True Line", "Estimated Line"), lty=c(2,1), bty="n") 
#Add a legend to your plot specifying which line is which.




# QUADRATIC REGRESSION RELATION DIAGRAM

b <- fab.lm$coefficients


fabData %>% 
  ggplot(aes(x, y)) +
  geom_point(aes(),color = "grey50", alpha = .5) +
  #geom_smooth(method = "lm", se = F, formula = y ~ poly(x, 2)) +
  stat_function(fun = function(x) b[1] + b[2]*x + b[3]*x^2, col = "firebrick") +    # estimated line
  stat_function(fun = function(x) beta0 + beta1*x + beta2*x^2, col = "blue") +   #true line
  theme(panel.background = element_blank(),
        panel.grid = element_blank())





# TWO-LINES REGRESSION RELATION DIAGRAM


n <- 200

X_i <- runif(n, -45, 45) 
Z_i <- sample(c(0, 1), n, replace = T)

beta0 <- 350
beta1 <- 7
beta2 <- -18.6
beta3 <- -3.8
sigma <- 65

epsilon_i <- rnorm(n, 0, sigma) 

Y_i <- beta0 + beta1*X_i + beta2*Z_i + beta3*X_i*Z_i + epsilon_i 

fabData <- data.frame(y=Y_i, x=X_i, z=as.integer(Z_i))

# Regression for group 0
fab.lm0 <- lm(y ~ x + z, data=subset(fabData, z == 0))
summary(fab.lm0)
b0 <- fab.lm0$coefficients

# Regression for group 1
fab.lm1 <- lm(y ~ x + z, data=subset(fabData, z == 1))
summary(fab.lm1)
b1 <- fab.lm1$coefficients

fabData %>% 
  ggplot(aes(x, y, color = factor(z))) +
  geom_point(alpha = .3) +
  scale_color_manual(values = c("firebrick", "blue"), guide = F) +
  # group 0
  stat_function(fun = function(x) b0[1] + b0[2]*x, col = "firebrick", size = .8, linetype = "solid") +
  stat_function(fun = function(x) beta0 + beta1*x, col = "firebrick", size = .8, linetype = "dashed") +
  # group 1
  stat_function(fun = function(x) b1[1] + b1[2]*x, col = "blue", size = .8, linetype = "solid") +
  stat_function(fun = function(x) (beta0+beta2) + (beta1+beta3)*x, col = "blue", size = .8, linetype = "dashed") +
  
  theme(panel.background = element_blank(),
        panel.grid = element_blank())







# CUBIC REGRESSION RELATION DIAGRAM


n <- 200

X_i <- runif(n, -30, 35) 

beta0 <- 50
beta1 <- 10
beta2 <- .5
beta3 <- -.2
sigma <- 800

epsilon_i <- rnorm(n, 0, sigma) 

Y_i <- beta0 + beta1*X_i + beta2*X_i^2 + beta3*X_i^3 + epsilon_i 

fabData <- data.frame(y=Y_i, x=X_i)

# Regression for group 0
fab.lm3 <- lm(y ~ x + I(x^2) + I(x^3), data = fabData)
summary(fab.lm3)
b3 <- fab.lm3$coefficients


fabData %>% 
  ggplot(aes(x, y)) +
  geom_point(alpha = .3) +
  stat_function(fun = function(x) b3[1] + b3[2]*x + b3[3]*x^2 + b3[4]*x^3, col = "firebrick") +
  stat_function(fun = function(x) beta0 + beta1*x + (beta2)*x^2 + (beta3)*x^3, 
                col = "firebrick", linetype = "dashed") +
  theme(panel.background = element_blank(),
        panel.grid = element_blank())


