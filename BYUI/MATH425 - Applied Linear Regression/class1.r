


library(tidyverse)

mtcars %>%
    ggplot(aes(mpg)) +
    geom_histogram(bins = 6, fill = "steelblue", color = "black")


round(sd(mtcars$mpg), 2)


mtcars %>%
    ggplot(aes(cyl, mpg, group = cyl)) +
    geom_boxplot()


mtcars %>%
    group_by(cyl) %>%
    mutate(avg = round(sd(mpg), 2)) %>%
    select(cyl, avg) %>%
    unique()




mtcars %>%
    ggplot(aes(qsec, mpg)) +
    geom_jitter()


lm1 <- lm(mpg ~ qsec, data = mtcars)
summary(lm1)