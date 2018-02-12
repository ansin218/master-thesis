library(ggplot2)
library(reshape2)

x <- c(1, 2, 3, 4, 5)
lucene <- c(53, 23, 12, 7, 5)
thunderbird <- c(68, 20, 7, 3, 2)
ubuntu <- c(61, 19, 10, 6, 4)

df <- data.frame(x, lucene, thunderbird, ubuntu)

chart_data <- melt(df, id='x')
names(chart_data) <- c('x', 'dataset', 'value')

# Plot stratified data analysis statistics of all three datasets using line graph
ggplot() +
  geom_line(data = chart_data, aes(x = x, y = value, color = dataset), size = 1)+
  labs(x="Strata", y="Number of Issues") +
  ggtitle("Number of Issues in each Strata") +
  theme(plot.title = element_text(hjust = 0.5), legend.title=element_text(size=14), legend.text = element_text(colour="black", size=12), axis.text.x = element_text(color = "black", size = 11), axis.text.y = element_text(color = "black", size = 11))
