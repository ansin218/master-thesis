library(ggplot2)
library(scales)

ubuntuFile <- "ubuntu_count.csv"
ubuntuData <- read.csv(ubuntuFile, header=TRUE, sep=",")

ubuntuData$countCat <- cut(ubuntuData$COUNT, breaks=c(1,5,10,15,20,25,30,35,40,45,50,100,500))

ggplot(ubuntuData, aes(x = factor(ubuntuData$countCat))) +
  geom_bar(aes(y = (..count..))) +
  labs(x="Count Category",y="Count Frequency") +
  ggtitle("Ubuntu Issue Tracker Comment Distribution") +
  theme(plot.title = element_text(hjust = 0.5)) +
  geom_text(aes( label = (..count..), y= ..count.. ), stat="count", vjust = -.5)
