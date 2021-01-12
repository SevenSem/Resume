from pprint import pprint

from .helper import get_word_count
from .idf import get_idf_sentences, get_idf_words
from .stringmanip import clean_sentence, get_sentences, get_words
from .tf import get_tf_sentences, get_tf_words


paragraph = "Summary I consider python myself as a hardworking, organized initiative and consistent person with good academic and practical skills. I accept challenges; it allows me broaden my existing knowledge and skills. I work persistently and diligently upholding the work and professionalism to get the best outcome. Skill Highlights , Project management , Strong decision maker • Strong Programming Knowledge • Creative design • Innovative • Service-focused Experience Localhost Projects 2017-Now • Working with Database in Java, Python and PHP • Developed a Blog website using Django Framework • Working with WordPress • Creating a beautiful template using bootstrap and CSS • Work with senior developer to manage large, complexdesign projects for corporate clients. Web Server Project  • Django Web Application on Heroku  • python django Working with WordPress and cPanel • Handling the problems related to Database (MySQL) Blogger: 2017- Now • Working with Blogger • Working with WordPress Education Bachelor of Computer Science and Technology: Trinity International College, 2016-2020 python  Tribhuvan University in python knowledge django django knowledge wordpress Nepal Bachelor Project: django framework Online Resume Project and Blog Web Application Knowledge on: Python | Django | JavaScript | React Js | HTML/CSS Database: MYSQL/ MongoDB and SQL Lite"

words = get_words(paragraph)
sentences, len_sentences = get_sentences(paragraph)
words_count, words_len = get_word_count(words)


tf_words = get_tf_words(words, words_count, words_len)
print('TF Words -->')
print('-'*30)
pprint(tf_words)
print('')

tf_sentences = get_tf_sentences(sentences, tf_words)
print('TF Sentences -->')
print('-'*30)
pprint(tf_sentences)
print('')


idf_words = get_idf_words(words, words_count, words_len, len_sentences)
pprint('IDF Words -->')
print('-'*30)
print(idf_words)
print('')

idf_sentences = get_idf_sentences(sentences, idf_words)
pprint('IDF Sentences -->')
print('-'*30)
print(idf_sentences)
print('')

#Calculating tfidf of each sentence. tfidf = tf*idf
tfidf = {s:(tf_words[s]*idf_words[s]) for s in words}

#Sorting the sentences based on their tfidf score.
#Higher the score, more the importance.
imp_word = sorted(tfidf.items(), key = lambda kv:(kv[1], kv[0]), reverse = True)
print('')
print('Sentences sorted -->')
print('-'*30)

#keyword extraction
test_list = [] 
x = input('Enter your name:')
test_list.append(x)
subs = 'Geek'
ttt = ("hello",3245)
print(type(ttt))

results = [data for data in imp_word if any(i in data for i in test_list)]
words_counts = [data for data in words_count if any(i in data for i in test_list)]
print("Filtered tuple from list are : " + str(results)) 

print(words_counts)
