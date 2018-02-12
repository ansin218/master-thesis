library(ggplot2)
library(scales)

luceneFile <- "lucene_rss_issues.csv"
luceneData <- read.csv(luceneFile, header=TRUE, sep=",")

luceneData$countCat <- cut(luceneData$count, breaks=c(5,10,15,20,25,30))

luceneData <- luceneData[!is.na(luceneData$countCat), ]

# Plot stratified data analysis statistics
ggplot(luceneData, aes(x = factor(luceneData$countCat))) +
  geom_bar(aes(y = (..count..))) +
  labs(x="Count Category",y="Count Frequency") +
  theme(plot.title = element_text(hjust = 0.5)) +
  geom_text(aes( label = (..count..), y= ..count.. ), stat="count", vjust = -.5)
