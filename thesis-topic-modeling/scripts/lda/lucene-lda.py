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
cursor_1.execute("SELECT * FROM lucene_rss_comments")

lucene_rss_list = list()

for row in cursor_1:
    lucene_rss_list.append(row[4])

tokenizer = RegexpTokenizer(r'\w+')
en_stop = get_stop_words('en')
alphaList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numList = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
customList1 = ['can', 'due', 'jira', 'lucene', 'thunderbird', 'instead', 'org', 'apache', 'hole', 'probably', 'use', 'another', 'created']
customList2 = ['just', 'know', 'branch_3x', 'make', 'better', 'like', 'got', 'will', 've', 'see', 'afor', 'yes', 'comment', 'message', 'say']
customList3 = ['don', 'maybe', 'never', 'also', 'many', 'look', 'll', 'com', 'done', 'think', 'thank', 'might', 'inbox', 'address', 'already']
customList4 = ['now', 'lon', 'method', 'much', 'need', 'sure', 'thanks', 'doesn', 'used', 'get', 'ok', '023', 'reply', 'tb', 'either','try']
customList5 = ['well', 'since', 'using', 'rice', '64', '27', '21', '16', 'without', '14', '12', '19', '09', '25', '2013', 'mail', 'name']
customList6 = ['00', '1014', '10', '03', '28', 'still', '2016', '15', '11901', 'please', '30', '0050', '04', '026', 'may', 'email', 'yet']
customList7 = ['11', '31', '2147483647', '26', '13', 'ubuntu', 'common', 'find', 'found', 'version', 'something', 'seem', 'seems', 'comm']
customList8 = ['change', 'changes', 'changed', 'tool', 'tools', 'user', 'users', '32', '22', '17', 'status', 'linux', 'error', 'info']
customList9 = ['patch', 'patches', 'issue', 'issues', 'bug', 'bugs', 'problem', 'problems', 'fix', 'fixes', 'fixed', 'test', 'tests']
customList10 = ['management', 'usr', 'focus', 'application', 'log', 'package', 'packages', 'logs', 'work', 'worked', 'report', 'works']
customList11 = ['mozilla', 'messages', '06', 'www', 'http', 'tell', 'first', 'one', 'two', 'freiburg', 'uni', 'brain', 'window', 'wayne']
customList12 = ['true', 'false', 'wrong', 'way', '38', 'errors', 'correct', 'rev', 'tried', 'actually', 'want', 'wanted', 'disable', 'disabled']
customList13 = ['merge', 'create', 'merged', 'created', 'good', 'err', 'maven', 'thing', 'trunk', 'commit', 'committed', 'pull', 'github']
customList14 = ['adrien', 'robert', 'bulk', 'michael', 'branch_5x', 'git', 'svn', 'solr', 'merges', 'read', 'attached', 'current', 'required']
en_stop = en_stop + alphaList + numList + customList1 + customList2 + customList3 + customList4 + customList5 + customList14
en_stop = en_stop + customList6 + customList7 + customList8 + customList9 + customList10 + customList11 + customList12 + customList13

p_stemmer = PorterStemmer()
lmtzr = WordNetLemmatizer()

doc_set = lucene_rss_list

texts = []

for i in doc_set:

    raw = i.lower()
    tokens = tokenizer.tokenize(raw)
    stopped_tokens = [i for i in tokens if not i in en_stop]
    stemmed_tokens = [lmtzr.lemmatize(i) for i in stopped_tokens]
    texts.append(stemmed_tokens)

dictionary = corpora.Dictionary(texts)
corpus = [dictionary.doc2bow(text) for text in texts]
ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics = 10, id2word = dictionary, passes = 5)

for i in  ldamodel.show_topics():
    print(i[0], i[1])

end_time = time()
time_taken = end_time - start_time

print("Total time taken in seconds: ", time_taken)
