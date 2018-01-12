library(ggplot2)
library(scales)

ubuntuFile <- "ubuntu_rss_issues.csv"
ubuntuData <- read.csv(ubuntuFile, header=TRUE, sep=",")

ubuntuData$countCat <- cut(ubuntuData$count, breaks=c(5,10,15,20,25,30))

ubuntuData <- ubuntuData[!is.na(ubuntuData$countCat), ]

ggplot(ubuntuData, aes(x = factor(ubuntuData$countCat))) +
  geom_bar(aes(y = (..count..))) +
  labs(x="Count Category",y="Count Frequency") +
  theme(plot.title = element_text(hjust = 0.5)) +
  geom_text(aes( label = (..count..), y= ..count.. ), stat="count", vjust = -.5)
