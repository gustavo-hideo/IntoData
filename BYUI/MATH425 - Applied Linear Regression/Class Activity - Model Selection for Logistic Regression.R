
# Logistic Regression
# Model Selection
# Math 425 Grades

library(tidyverse)

d <- read.csv("./Data/Math425HistoricGrades.csv") %>% 
  mutate(Final.Letter.Grade = ifelse(Final.Letter.Grade == "A", 1, 0))


pairs(d)


glm1 <- glm(Final.Letter.Grade ~ Hard.Work.Subtotal.Numerator +
                                 Final.Exam.Score,
            data = d, family = "binomial")

summary(glm1)



pairs(cbind(R = glm1$residuals, Fit = glm1$fitted.values, d))


d %>% 
  ggplot(aes(Hard.Work.Subtotal.Numerator, Final.Letter.Grade)) +
  geom_point()
