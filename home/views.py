from django.shortcuts import render
import pickle
from nltk import word_tokenize
from .models import Facts
import pandas as pd
#from sklearn.feature_extraction.text import TfidfVectorizer
#from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    return render(request, 'home.html')


# def spam(request):
#     fc = Facts.objects.all()
#     result = None
#     if request.method == "POST":
#         form = request.POST.get('fact')
#         text = pickle.load(open('static/new_spam_detector.sav', 'rb'))
#         result = text.predict([form])
#         add_fact = Facts(fact = form)
#         add_fact.save()
#         str = "SPAM" if result else  "NOT SPAM"
#         #form = FactsForm()
#         result = str
#         print("The given statement is ", result)
#     return render(request,'spam.html', { 'result': result,})

def who(request):
    df1 = pd.read_csv('static/who_health_facts.csv')
    x = df1.to_dict()
    del x['Unnamed: 0']
    final_data_dict = {}
    for i in x.keys():
        final_data_dict[i] = x[i][0].split('.  ,')
    temp = final_data_dict.keys()
    result = None
    if request.method == "POST":
        Y = request.POST.get('fact')
        c = request.POST.get('choose')
        data_ = final_data_dict[c]
        cosine_val = []
        for X in data_:
            X_list = word_tokenize(X)
            Y_list = word_tokenize(Y)
            l1 = [];l2 = []
            # remove stop words from string
            X_set = {w for w in X_list}
            Y_set = {w for w in Y_list}
            rvector = X_set.union(Y_set)
            for w in rvector:
                if w in X_set:
                    l1.append(1)  # create a vector
                else:
                    l1.append(0)
                if w in Y_set:
                    l2.append(1)
                else:
                    l2.append(0)
            c = 0
            # cosine formula
            for i in range(len(rvector)):
                c += l1[i] * l2[i]
            cosine = c / float((sum(l1) * sum(l2)) ** 0.5)
            cosine_val.append(cosine)
        result = data_[cosine_val.index(max(cosine_val))]

    return render(request, 'who.html', {'temp': temp, 'result':result})

