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
cursor_1.execute("SELECT DISTINCT(comment), comment_id, issue_id FROM `lucene_rss_comments` WHERE 1")

lucene_rss_list = list()

for row in cursor_1:
    lucene_rss_list.append(row[0])

for x in range(len(lucene_rss_list)):
	print('Comment: ', x + 1)

	tokenizer = RegexpTokenizer(r'\w+')
	en_stop = get_stop_words('en')
	alphaList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	numList = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	customList1 = ['can', 'due', 'jira', 'lucene', 'instead', 'org', 'apache', 'hole', 'probably', 'use', 'another']
	customList2 = ['just', 'know', 'branch_3x', 'make', 'better', 'like', 'got', 'will', 've', 'see', 'afor', 'yes']
	customList3 = ['don', 'maybe', 'never', 'also', 'many', 'look', 'll', 'com', 'done', 'think', 'thank', 'might']
	customList4 = ['now', 'lon', 'method', 'much', 'need', 'sure', 'thanks', 'doesn', 'used', 'get', 'ok', '023']
	customList5 = ['well', 'since', 'using', 'rice', '64', 'havent', 'still', 'thats']
	en_stop = en_stop + alphaList + numList + customList1 + customList2 + customList3 + customList4 + customList5

	p_stemmer = PorterStemmer()
	lmtzr = WordNetLemmatizer()

	temp_list = list()
	temp_list.append(lucene_rss_list[x])

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
		print('Insufficient Data')

end_time = time()
time_taken = end_time - start_time

print("Total time taken in seconds: ", time_taken)
