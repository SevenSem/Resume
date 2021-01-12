from django.shortcuts import render
from pprint import pprint
from .helper import get_word_count
from .idf import get_idf_sentences, get_idf_words
from .stringmanip import clean_sentence, get_sentences, get_words
from .tf import get_tf_sentences, get_tf_words
from .models import UploadCv

from django.views.generic.edit import FormView, CreateView
from .forms import FileFieldForm
from django.views.generic.edit import FormView
import PyPDF2

class FileFieldView(CreateView):
    model = UploadCv
    fields = ['personalinfo', 'uploadfile']
    template_name = 'pages/upload.html' 
    success_url = 'uploadcv'  

    def form_valid(self, form):
        form.instance.cv_user = self.request.user
        return super().form_valid(form)

def prediction(request):
    pdf_file = UploadCv.objects.all()[:1]
    for data in pdf_file:
        if request.user == data.cv_user:
            pdf = f'media/{data.uploadfile}'
            epdf = f"'{pdf}'"
    print(epdf)
    pdfFileObj = open(pdf, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    print(pdfReader.numPages)
    pageObj = pdfReader.getPage(0)
    a = pageObj.extractText()
    print(a)
    

    paragraph = "fsdfns python asfasf asda safa is am arae"
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

    test_list = ['python','django'] 
    # x = input('Enter your name:')
    # test_list.append(x)

    results = [data for data in imp_word if any(i in data for i in test_list)]
    words_counts = [data for data in words_count if any(i in data for i in test_list)]

    print(words_counts)

    data = {
        'data': results
    }
    return render(request,'pages/prediction.html', data)