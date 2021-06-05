from django.shortcuts import render
from pprint import pprint
from .helper import get_word_count
from .idf import get_idf_sentences, get_idf_words
from .stringmanip import clean_sentence, get_sentences, get_words
from .tf import get_tf_sentences, get_tf_words
from .models import UploadCv
import fitz
from personality.models import * 

from django.views.generic.edit import FormView, CreateView
from .forms import FileFieldForm
from django.views.generic.edit import FormView
import PyPDF2

class FileFieldView(CreateView):
    model = UploadCv
    fields = ['uploadfile', 'keywords']
    template_name = 'pages/upload.html' 
    success_url = 'prediction'  

    def form_valid(self, form):
        form.instance.cv_user = self.request.user
        return super().form_valid(form)

def prediction(request):
    pdf_file = UploadCv.objects.filter(cv_user=request.user).order_by("-id")[0]
    epdf =  f'media/{pdf_file.uploadfile}'
    with fitz.open(epdf) as doc:
        texts = ""
        for page in doc:
            texts += page.getText()

    print(texts)

    print(texts)
    
    paragraph = texts
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
    idf_sentences = get_idf_sentences(sentences, idf_words)

    tfidf = {s:(tf_words[s]*idf_words[s]) for s in words}

    imp_word = sorted(tfidf.items(), key = lambda kv:(kv[1], kv[0]), reverse = True)
    print('')
    print('-'*30)

    keywords_test=  UploadCv.objects.filter(cv_user=request.user).order_by("-id")[0]
    keyword = keywords_test.keywords

    #converting string into list, using string.split 
    """ here keyword is string fetched from database, we need it in string so we convert it"""
    def Convert(string):
        li = list(string.split(","))
        return li
    
    test_list = Convert(keyword)
    print(test_list)
    # x = input('Enter your name:')
    # test_list.append(x)

    results = [data for data in imp_word if any(i in data for i in test_list)]

    words_counts = [data for data in imp_word if any(i in data for i in test_list)]

    print(words_counts)
    print("res",results)
    def drawChart():
        datas = google.visualization.arrayToDataTable([
        ['Task', 'Hours per Day'],
        ['Work', {data}],
        ['Eat', 2],
        ])
        return draw
    key = []
    value = []
    if results:    
        for i in results:
            x =int(i[1]*1000)
            print(x)
            value.append(x)
        print(value)
    
    if results:    
        for i in results:
            x =i[0]
            key.append(x)
        print(key)
    print(key[0])
    data = {
        'data': results,
        'key' : key,
        'value' : value,
        'bestkey' : key[0],
        'keywords' : test_list,
        'file_url': epdf,
        'avg' : PersonalityData.objects.filter(user__username= request.user).order_by('-id')[:1],
        'personalityresult' : PersonalityResult.objects.all()
    }
    return render(request,'pages/prediction.html', data)