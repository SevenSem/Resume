from django.shortcuts import render
from pprint import pprint
from .helper import get_word_count
from .idf import get_idf_sentences, get_idf_words
from .stringmanip import clean_sentence, get_sentences, get_words
from .tf import get_tf_sentences, get_tf_words
from .models import UploadCv
import fitz
from personality.models import * 
from account.models import Applicant
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

    paragraph = texts
    words = get_words(paragraph)
    sentences, len_sentences = get_sentences(paragraph)
    words_count, words_len = get_word_count(words)

    tf_words = get_tf_words(words, words_count, words_len)

    tf_sentences = get_tf_sentences(sentences, tf_words)
    
    print(tf_sentences)
    idf_words = get_idf_words(words, words_count, words_len, len_sentences)
    idf_sentences = get_idf_sentences(sentences, idf_words)

    tfidf = {s:(tf_words[s]*idf_words[s]) for s in words}

    imp_word = sorted(tfidf.items(), key = lambda kv:(kv[1], kv[0]), reverse = True)

    keywords_test=  UploadCv.objects.filter(cv_user=request.user).order_by("-id")[0]
    keyword = keywords_test.keywords
    stfidf = {s:(tf_sentences[s]*idf_sentences[s]) for s in sentences}
    imp_sentences = sorted(stfidf.items(), key = lambda kv:(kv[1], kv[0]), reverse = True)

        
    tfidfimpsentnc = {s:(tf_sentences[s]*idf_sentences[s]) for s in sentences}
    imp_sentences_line = sorted(tfidfimpsentnc.items(), key = lambda kv:(kv[1], kv[0]), reverse = True)


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


    print("imp_word ++++++")
    print(imp_word)
    print("imp_word++++++")
    print(results)
    key = []
    value = []

    keyforrem =[]
    valueforrem = []

    if imp_word:   
        index = 0
        for data in imp_word:
            index = index+1
            
            x =float(data[1]*1000)
            y =data[0]
            keyforrem.append(y)
            valueforrem.append(x)

        print("tindx",index)

    if results:    
        for i in results:
            x =int(i[1]*1000)
            y =i[0]
            key.append(y)
            value.append(x)
    
    
    isentences = []
    if imp_sentences_line:
        for i in imp_sentences_line:
            imp = i[0]
            isentences.append(imp)
            

    if key:
        bestkey =  key[0]
    else:
        bestkey = 0


    print(valueforrem)
    data = {
        'data': results,
        'key' : key,
        'value' : value,
        'keyforrem' : keyforrem,
        'valueforrem' : valueforrem,
        'bestkey' :bestkey,
        'keywords' : test_list,
        'file_url': epdf,
        'imp_sentences_line' : isentences[0],

        'avg' : PersonalityData.objects.filter(user__username= request.user).order_by('-id')[:1],
        'personalityresult' : PersonalityResult.objects.all()
    }
    return render(request,'pages/prediction.html', data)