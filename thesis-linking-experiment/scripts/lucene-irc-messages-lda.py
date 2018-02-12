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

# Load IRC dataset
cursor_1 = conn.cursor()
cursor_2 = conn.cursor()
cursor_1.execute("SELECT DISTINCT(id), message FROM `lucene_fine_grained`")

lucene_irc_list = list()
irc_msg_id_list = list()
keywords_list = list()

for row in cursor_1:
	irc_msg_id_list.append(row[0])
	lucene_irc_list.append(row[1])

for x in range(len(lucene_irc_list)):

	tokenizer = RegexpTokenizer(r'\w+')
	en_stop = get_stop_words('en')
	
	# Create custom stopwords list
	alphaList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	numList = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	customList1 = ['can', 'due', 'jira', 'lucene', 'thunderbird', 'instead', 'org', 'apache', 'hole', 'probably', 'use', 'another', 'created']
	customList2 = ['just', 'know', 'make', 'better', 'like', 'got', 'will', 've', 'see', 'afor', 'yes', 'comment', 'message', 'say']
	customList3 = ['don', 'maybe', 'never', 'also', 'many', 'look', 'll', 'com', 'done', 'think', 'thank', 'might', 'inbox', 'address', 'already']
	customList4 = ['now', 'lon', 'method', 'much', 'need', 'sure', 'thanks', 'doesn', 'used', 'get', 'ok', '023', 'reply', 'tb', 'either','try']
	customList5 = ['well', 'since', 'using', 'rice', '64', '27', '21', '16', 'without', '14', '12', '19', '09', '25', '2013', 'mail', 'name']
	customList6 = ['00', '1014', '10', '03', '28', 'still', '2016', '15', '11901', 'please', '30', '0050', '04', '026', 'may', 'email', 'yet', 'sorr']
	customList7 = ['11', '31', '2147483647', '26', '13', 'ubuntu', 'common', 'find', 'found', 'version', 'something', 'seem', 'seems', 'comm', 'resolved']
	customList8 = ['change', 'changes', 'changed', 'tool', 'tools', 'user', 'users', '32', '22', '17', 'status', 'linux', 'error', 'info', 'forget', 'forgot']
	customList9 = ['patch', 'patches', 'issue', 'issues', 'bug', 'bugs', 'problem', 'problems', 'fix', 'fixes', 'fixed', 'test', 'tests', 'discussion', 'failure']
	customList10 = ['management', 'usr', 'focus', 'application', 'log', 'package', 'packages', 'logs', 'work', 'worked', 'report', 'works', 'pick', 'picks']
	customList11 = ['mozilla', 'messages', '06', 'www', 'http', 'tell', 'first', 'one', 'two', 'freiburg', 'uni', 'brain', 'window', 'wayne', 'soon', 'picked']
	customList12 = ['true', 'false', 'wrong', 'way', '38', 'errors', 'correct', 'rev', 'tried', 'actually', 'want', 'wanted', 'disable', 'disabled', 'checked']
	customList13 = ['merge', 'create', 'merged', 'created', 'good', 'err', 'maven', 'thing', 'trunk', 'commit', 'committed', 'pull', 'github', 'checks']
	customList14 = ['adrien', 'robert', 'bulk', 'michael', 'git', 'svn', 'solr', 'merges', 'read', 'attached', 'current', 'required', 'moves', 'check']
	customList15 = ['havent', 'store', 'stored', 'stores', 'one', 'close', 'look', 'looks', 'looked', 'revision', 'add', 'start', 'move', 'description']
	customList16 = ['release', 'likewise', 'different', 'wait', 'confused', 'right', 'far', 'anyway', 'anyways', 'one', 'releases', 'branch', 'around']
	customList17 = ['including', 'ready', 'fail', 'mechanism', 'incoming', 'dev', 'spell', 'thats', 'bit', 'bits', 'yeah', 'anywhere', 'suggests']
	customList18 = ['push', 'pull', 'code', 'rule', 'feel', 'feels', 'felt', 'forgive', 'didnt', 'although', 'new', 'adding', 'reason', 'suggested']
	customList19 = ['wanting', 'rule', 'legitimately', 'however', 'us', 'currently', 'way', 'ways', 'unnecessary', 'copy', 'pass', 'passed', 'suggest']
	customList20 = ['come', 'cool', 'testing', 'run', 'latest', 'round', 'rounds', 'update', 'updates', 'updated', 'agree', 'shall', 'arrive', 'arrived', 'line']
	customList21 = ['tested', 'happen', 'anythings', 'forms', 'help', 'easily', 'write', 'writes', 'lot', 'lots', 'aspect', 'comments', 'committing', 'thing']
	customList22 = ['quick', 'really', 'fine', 'keep', 'everything', 'non', 'correct', 'correctly', 'simple', 'clear', 'didnt', 'didn', 'time', 'times', 'likely', 'oh']
	customList23 = ['crash', 'crashed', 'book', 'occur', 'started', 'result', 'seperate', 'get', 'gets', 'duplicate', 'marked', 'necessary', 'completely', 'may', 'even']
	customList24 = ['source', 'mark', 'marked', 'big', 'require', 'need', 'required', 'occurs', 'ubuntu', 'try', 'mail', 'thunderbird', 'creating', 'create']
	customList25 = ['normal', 'annoying', 'closed', 'present', 'tb', 'guessing', 'cover', 'hmm', 'affect', 'entire', 'ah', 'commented', 'commenting', 'comments', 'comment']
	customList26 = ['try', 'forever', 'added', 'specified', 'whatever', 'hello', 'specifies', 'specify', 'affect', 'ask', 'asks', 'asked', 'exactly', 'exact', 'saying']
	customList27 = ['recently', 'rather', 'described', 'caused', 'come', 'bad', 'comes', 'came', 'told', 'tell', 'looked', 'looking', 'confirming', 'per', 'cause', 'share', 'away', 'included', 'seemed', 'seem', 'taking', 'fewer']
	customList28 = ['happen', 'happens', 'happening', 'within', 'helpful', 'working', 'getting', 'trying', 'something', 'reason', 'reasons', 'finish', 'enable', 'every', 'take' 'anything', 'understand', 'without', 'version', 'persists', 'persist', 'daily']
	customList29 = ['delete', 'deleting', 'showing', 'simply', 'running', 'said', 'next', 'keeping', 'mind', 'advice', 'seeing', 'behavior', 'think', 'thought', 'back', 'already', 'needed', 'incorrect', 'follows', 'won', 'together']
	customList30 = ['perfect', 'affect', 'affects', 'feature', 'related', 'quite', 'wrongly', 'separate', 'seen', 'anyone', 'lately', 'removing', 'missed', 'anything', 'highly', 'unlikely', 'quickly', 'someone', 'checking', 'handled', 'handle', 'possibly']
	customList31 = ['must', 'shouldn', 'shouldnt', 'really', 'supported', 'return', 'isnt', 'isn', 'busy', 'make', 'always', 'similar', 'dealt', 'behind', 'opnion', 'decent', 'directly', 'please', 'reply', 'replying', 'replied']
	customList32 = ['launchpad', 'able', 'provide', 'recent', 'last', 'important', 'though', 'confirm', 'confirmed', 'cool', 'find', 'make', 'makes', 'made', 'indirectly', 'show', 'plenty', 'mention', 'modified', 'nomination', 'nominated', 'causing']
	customList33 = ['turn', 'provides', 'turned', 'turning', 'turns', 'leaving', 'explanation', 'higher', 'affect', 'affected', 'consider', 'case', 'cases', 'successful', 'gave', 'give', 'definite', 'definitely']
	customList34 = ['let', 'https', 'http', 'experiencing', 'visited', 'importance', 'information', 'give', 'gives', 'gave', 'expect', 'expected', 'expects', 'axtually', 'following', 'common', 'avoid', 'sorted']
	
	en_stop = en_stop + alphaList + numList + customList1 + customList2 + customList3 + customList4 + customList5 + customList14
	en_stop = en_stop + customList6 + customList7 + customList8 + customList9 + customList10 + customList11 + customList12 + customList13
	en_stop = en_stop + customList15 + customList16 + customList17 + customList18 + customList19 + customList20 + customList21 + customList22
	en_stop = en_stop + customList23 + customList24 + customList25 + customList26 + customList27 + customList28 + customList29 + customList30
	en_stop = en_stop + customList31 +  customList32 + customList33 + customList34

	p_stemmer = PorterStemmer()
	lmtzr = WordNetLemmatizer()

	temp_list = list()
	temp_list.append(lucene_irc_list[x])

	doc_set = temp_list

	texts = []

	# Generate keywords using LDA
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
		for i in ldamodel.show_topics():
			rawTopics = i[1]
			lenTopics = rawTopics.count('+') + 1
			keywords = ''
			for j in range(lenTopics):
				rawTopics = rawTopics.split('"', 1)
				rawTopics = rawTopics[1].split('"', 1)
				if(j == lenTopics-1):
					keywords = keywords + rawTopics[0]
				else:
					keywords = keywords + rawTopics[0] + ' '
				rawTopics = rawTopics[1]
			print(keywords)
		keywords_list.append(keywords)
	except ValueError:
		keyword = 'Insufficient Data'
		keywords_list.append(keyword)

for a in range(len(lucene_irc_list)):
	try:
	    cursor_2.execute("""INSERT INTO lucene_irc_keywords_lda (msg_id, message, keywords) VALUES ("%s", "%s", "%s")""" % (irc_msg_id_list[a], lucene_irc_list[a], keywords_list[a]))
	except:
	    conn.rollback()

end_time = time()
time_taken = end_time - start_time

print("Total time taken in seconds: ", time_taken)
