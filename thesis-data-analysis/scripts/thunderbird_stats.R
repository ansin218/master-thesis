library(ggplot2)
library(scales)

thunderbirdFile <- "thunderbird_count.csv"
thunderbirdData <- read.csv(thunderbirdFile, header=TRUE, sep=",")

thunderbirdData$countCat <- cut(thunderbirdData$COUNT, breaks=c(1,5,10,15,20,25,30,35,40,45,50,100,500))

ggplot(thunderbirdData, aes(x = factor(thunderbirdData$countCat))) +
  geom_bar(aes(y = (..count..))) +
  labs(x="Count Category",y="Count Frequency") +
  ggtitle("Thunderbird Issue Tracker Comment Distribution") +
  theme(plot.title = element_text(hjust = 0.5)) +
  geom_text(aes( label = (..count..), y= ..count.. ), stat="count", vjust = -.5)
