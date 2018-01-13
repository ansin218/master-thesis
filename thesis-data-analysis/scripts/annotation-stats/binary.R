library(ggplot2)
library(reshape2)

x <- c('Lucene', 'Thunderbird', 'Ubuntu')
relevant <- c(1780, 1509, 1349)
irrelevant <- c(666, 1577, 1433)

df <- data.frame(x, relevant, irrelevant)
df <- melt(df, id.vars = "x")

ggplot(df, aes(x, value, fill = variable)) + geom_bar(aes(fill = variable), position = position_dodge(0.9), stat="identity") + 
  coord_flip() + 
  geom_text(aes(label = value), position = position_dodge(0.9), hjust = 1.25, vjust = 0.5) +
  xlab("Projects") +
  ylab("Number of Sentences")

  