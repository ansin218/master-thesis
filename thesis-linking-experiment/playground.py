# Similarity comparison done here
# May be use something like Jaccard similarity or Cosine similarity 

a = ['Munich', 'Chennai', 'Regensburg']
b = ['Chennai', 'Riyadh', 'Atlanta']
#b = ['Munich', 'Chennai']
#b = ['Istanbul', 'Casteggio']

# Instead of performing multiple loop operations
# Try performing set difference using set operations
s = 0

for x in range(len(a)):
	for y in range(len(b)):
		if(a[x] == b[y]):
			print('==> Similar: ', a[x], b[y])
			s += 1

print('Complete List: ', a + b)

if(s == 0):
	print('Completely Dissimilar')
else:
	if(len(a) == len(b)):
		if(s == len(a)):
			print('Completely Similar: 100%')
		else:
			if(s == 0):
				print('Completely Dissimilar')
			else:
				print('Partially Similar: ', (s * 100) / (len(a) + len(b) - s), '%')
	else:
		print('Partially Similar: ', (s * 100) / (len(a) + len(b) - s), '%')


# Libraries for performing LDA on comments

############# TO DO ######################

# Try to filter and extract the keywords alone

# -*- coding: utf-8 -*-
import pymysql
import pymysql.cursors
from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from gensim import corpora, models, utils
import gensim
from time import time

start_time = time()

conn = pymysql.connect(host='localhost', user='root', password='password', db='Issue_Trackers', autocommit=True, use_unicode=True, charset="utf8")

cursor_1 = conn.cursor()
cursor_1.execute("SELECT DISTINCT(comment) FROM lucene_rss_comments")

lucene_rss_list = list()

for row in cursor_1:
    lucene_rss_list.append(row[0])

for x in range(len(lucene_rss_list)):
	#print('Comment: ', lucene_rss_list[x])

	tokenizer = RegexpTokenizer(r'\w+')
	en_stop = get_stop_words('en')
	alphaList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	numList = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	customList1 = ['can', 'due', 'jira', 'lucene', 'instead', 'org', 'apache', 'hole', 'probably', 'use', 'another']
	customList2 = ['just', 'know', 'branch_3x', 'make', 'better', 'like', 'got', 'will', 've', 'see', 'afor', 'yes']
	customList3 = ['don', 'maybe', 'never', 'also', 'many', 'look', 'll', 'com', 'done', 'think', 'thank', 'might']
	customList4 = ['now', 'lon', 'method', 'much', 'need', 'sure', 'thanks', 'doesn', 'used', 'get', 'ok', '023']
	customList5 = ['well', 'since', 'using', 'rice', '64', 'havent', 'still']
	en_stop = en_stop + alphaList + numList + customList1 + customList2 + customList3 + customList4 + customList5

	p_stemmer = PorterStemmer()
	lmtzr = WordNetLemmatizer()

	temp_list = list()
	temp_list.append(lucene_rss_list[x])
	#print(len(temp_list))
	
	doc_set = temp_list

	texts = []

	for i in doc_set:

	    raw = i.lower()
	    tokens = tokenizer.tokenize(raw)
	    stopped_tokens = [i for i in tokens if not i in en_stop]
	    stemmed_tokens = [lmtzr.lemmatize(i) for i in stopped_tokens]
	    texts.append(stemmed_tokens)

	dictionary = corpora.Dictionary(texts)
	corpus = [dictionary.doc2bow(text) for text in texts]
	try:
		ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics = 1, id2word = dictionary, passes = 2)
		print(ldamodel.print_topics(1))
	except ValueError:
		print('Not Enough Data')

end_time = time()
time_taken = end_time - start_time

print("Total time taken in seconds: ", time_taken)
