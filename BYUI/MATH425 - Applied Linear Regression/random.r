



cor(mtcars$disp, mtcars$wt)^2


lm1 <- lm(mpg~wt, data=mtcars)
summary(lm1)
predict(lm1, data.frame(wt=2.700), interval = "prediction")[1]


round(log(5000), 3)
round(exp(log(5000)), 0)

log(10000)
exp(4)

library(tidyverse)

par(mfrow = c(1, 2))
hist(islands, col = "forestgreen")
hist(log(islands), col = "cornflowerblue")
hist(log(islands), col = "cornflowerblue")
axis(1, at = 2:10, labels = round(exp(2:10), 0))


library(mosaicData)
library(tidyverse)
plot(gasbill ~ temp, data = Utilities)

lm.gb <- lm(log(gasbill) ~ temp, data = Utilities)
summary(lm.gb)
lm.gb$coefficients[2]

Utilities %>%
    ggplot(aes(temp, log(gasbill))) +
    geom_point() +
    geom_smooth(method = "lm", se = F, color = "black")

Utilities %>%
    ggplot(aes(temp, gasbill)) +
    geom_point() +
    geom_smooth(method = "lm", se = F, color = "black") +
    stat_function(fun = function(x) exp(lm.gb$coefficients[1] + lm.gb$coefficients[2]*x), color = "cornflowerblue")



#kCEpW4hBA6QxFegmofkKW39fOXDduvIM



lm1 <- lm(mpg ~ hp, data = mtcars)
summary(lm1)
plot(mpg ~ hp, data = mtcars)
abline()



lm1 <- lm(dist~speed, data = cars)
summary(lm1)7584





curve(dt(x, 3), from=-4, to=4, lwd=2)
curve(dnorm(x), add=TRUE, col="gray")
abline(h=0, v=c(-1,1), col=c("gray","orange","orange"), lwd=c(1,2,2))

pt(-1, 3)*2 #gives the area more extreme than t=-1 for t-dist with 3 df.






library(mosaic)
library(tidyverse)
library(car)


p <- Utilities %>%
    ggplot(aes(temp, gasbill)) +
    geom_point() +
    geom_smooth(method = "lm", se = F, color = "pink") +
    theme(panel.background = element_blank(),
          panel.grid = element_blank())

lm2 <- lm(gasbill ~ temp, data = Utilities)
plot(lm2, which = 1)  # bending with bad variance. try transformations

boxCox(lm2, lambda = seq(0, 1, 0.1))

lm2b <- lm(sqrt(gasbill) ~ temp, data = Utilities)

pred <- predict(lm2, data.frame(temp = 30), interval = "prediction")
pred2 <- predict(lm2b, data.frame(temp = 30), interval = "prediction")

p +
stat_function(fun = function(x) (lm2b$coefficients[1] + lm2b$coefficients[2] * x)^2, color = "skyblue", linetype = 2, size = 1.3) +
geom_hline(yintercept = pred2[1]^2, color = "skyblue", linetype = 2, size = 1) +
geom_hline(yintercept = pred2[2]^2, color = "skyblue", linetype = 2, size = 1) +
geom_hline(yintercept = pred2[3]^2, color = "skyblue", linetype = 2, size = 1) +
geom_hline(yintercept = pred[1], color = "pink", linetype = 2, size = 1) +
geom_hline(yintercept = pred[2], color = "pink", linetype = 2, size = 1) +
geom_hline(yintercept = pred[3], color = "pink", linetype = 2, size = 1)














