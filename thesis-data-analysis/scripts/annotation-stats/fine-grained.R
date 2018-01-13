library(ggplot2)
library(reshape2)

x <- c('Lucene', 'Thunderbird', 'Ubuntu')
issue <- c(259, 747, 687)
alternative <- c(828, 484, 410)
pro <- c(543, 224, 189)
con <- c(284, 228, 152)
decision <- c(207, 80, 117)

df <- data.frame(x, issue, alternative, pro, con, decision)
df <- melt(df, id.vars = "x")

ggplot(df, aes(x, value, fill = variable)) + geom_bar(aes(fill = variable), position = position_dodge(0.9), stat="identity") + 
  coord_flip() + 
  geom_text(aes(label = value), position = position_dodge(0.9), hjust = 1.25, vjust = 0.5) +
  xlab("Projects") +
  ylab("Number of Sentences")

