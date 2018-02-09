library(ggplot2)
library(scales)

luceneFile <- "lucene_issues.csv"
luceneData <- read.csv(luceneFile, header=TRUE, sep=",")

luceneData$countCat <- cut(luceneData$count, breaks=c(1,5,10,15,20,25,30,35,40,45,50,100,150))

luceneData <- luceneData[!is.na(luceneData$countCat), ]

ggplot(luceneData, aes(x = factor(luceneData$countCat))) +
  geom_bar(aes(y = (..count..))) +
  labs(x="Comments Count Category",y="Number of Issues") +
  ggtitle("Apache Lucene Issue Trackers Comments Distribution") +
  theme(plot.title = element_text(hjust = 0.5), axis.text.x = element_text(color = "black", size = 11), axis.text.y = element_text(color = "black", size = 11)) +
  geom_text(aes( label = (..count..), y= ..count.. ), stat="count", vjust = -.5)
