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
  ggtitle("Rationale Frequency") +
  theme(plot.title = element_text(hjust = 0.5), legend.title=element_text(size=14), legend.text = element_text(colour="black", size=12), axis.text.x = element_text(color = "black", size = 12), axis.text.y = element_text(color = "black", size = 12)) +
  xlab("Projects") +
  ylab("Number of Sentences") + 
  scale_fill_manual(values=c("#BE3F3F", "#e5b2b2"), 
                    name="Rationale",
                    labels=c("With Rationale", "Without Rationale"))

  