library(ggplot2)
library(scales)

thunderbirdFile <- "thunderbird_rss_issues.csv"
thunderbirdData <- read.csv(thunderbirdFile, header=TRUE, sep=",")

thunderbirdData$countCat <- cut(thunderbirdData$count, breaks=c(5,10,15,20,25,30))

thunderbirdData <- thunderbirdData[!is.na(thunderbirdData$countCat), ]

ggplot(thunderbirdData, aes(x = factor(thunderbirdData$countCat))) +
  geom_bar(aes(y = (..count..))) +
  labs(x="Count Category",y="Count Frequency") +
  theme(plot.title = element_text(hjust = 0.5)) +
  geom_text(aes( label = (..count..), y= ..count.. ), stat="count", vjust = -.5)
