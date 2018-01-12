library(ggplot2)
library(scales)

luceneFile <- "lucene_issues.csv"
luceneData <- read.csv(luceneFile, header=TRUE, sep=",")

luceneData$countCat <- cut(luceneData$count, breaks=c(1,5,10,15,20,25,30,35,40,45,50,100,150))

luceneData <- luceneData[!is.na(luceneData$countCat), ]

ggplot(luceneData, aes(x = factor(luceneData$countCat))) +
  geom_bar(aes(y = (..count..))) +
  labs(x="Count Category",y="Count Frequency") +
  ggtitle("Apache Lucene Issue Trackers Comment Distribution") +
  theme(plot.title = element_text(hjust = 0.5)) +
  geom_text(aes( label = (..count..), y= ..count.. ), stat="count", vjust = -.5)
