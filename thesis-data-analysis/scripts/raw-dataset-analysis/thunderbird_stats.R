library(ggplot2)
library(scales)

thunderbirdFile <- "thunderbird_issues.csv"
thunderbirdData <- read.csv(thunderbirdFile, header=TRUE, sep=",")

thunderbirdData$countCat <- cut(thunderbirdData$count, breaks=c(1,5,10,15,20,25,30,35,40,45,50,100,500))

thunderbirdData <- thunderbirdData[!is.na(thunderbirdData$countCat), ]

ggplot(thunderbirdData, aes(x = factor(thunderbirdData$countCat))) +
  geom_bar(aes(y = (..count..))) +
  labs(x="Comments Count Category",y="Number of Issues") +
  ggtitle("Mozilla Thunderbird Issue Trackers Comments Distribution") +
  theme(plot.title = element_text(hjust = 0.5), axis.text.x = element_text(color = "black", size = 11), axis.text.y = element_text(color = "black", size = 11)) +
  geom_text(aes( label = (..count..), y= ..count.. ), stat="count", vjust = -.5)
