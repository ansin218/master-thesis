library(ggplot2)
library(reshape2)

x <- c(1, 2, 3, 4, 5)
lucene <- c(53, 23, 12, 7, 5)
thunderbird <- c(68, 20, 7, 3, 2)
ubuntu <- c(61, 19, 10, 6, 4)

df <- data.frame(x, lucene, thunderbird, ubuntu)

chart_data <- melt(df, id='x')
names(chart_data) <- c('x', 'func', 'value')

ggplot() +
  geom_line(data = chart_data, aes(x = x, y = value, color = func), size = 1)+
  xlab("Strata") +
  ylab("Issues")
