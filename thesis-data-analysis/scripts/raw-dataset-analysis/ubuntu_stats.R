library(ggplot2)
library(scales)

ubuntuFile <- "ubuntu_issues.csv"
ubuntuData <- read.csv(ubuntuFile, header=TRUE, sep=",")

ubuntuData$countCat <- cut(ubuntuData$count, breaks=c(1,5,10,15,20,25,30,35,40,45,50,100,500))

ubuntuData <- ubuntuData[!is.na(ubuntuData$countCat), ]

ggplot(ubuntuData, aes(x = factor(ubuntuData$countCat))) +
  geom_bar(aes(y = (..count..))) +
  labs(x="Comments Count Category",y="Number of Issues") +
  ggtitle("Ubuntu Issue Trackers Comment Distribution") +
  theme(plot.title = element_text(hjust = 0.5), axis.text.x = element_text(color = "black", size = 11), axis.text.y = element_text(color = "black", size = 11)) +
  geom_text(aes( label = (..count..), y= ..count.. ), stat="count", vjust = -.5)
