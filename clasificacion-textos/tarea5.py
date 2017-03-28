import json
from pathlib import Path
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import numpy as np
from sklearn import metrics
from sklearn.model_selection import GridSearchCV
from nltk.corpus import stopwords

def cargaTweets(archivo):
    cat = []
    tweet_text = []
    with open (archivo) as raw_data:
        for item in raw_data:
            tema,categoria,nombreTweet = item.split(",")
            tweet = Path("rawdata/" + nombreTweet[1:-2] + ".json")
            if tweet.is_file():
                if cargaJson("rawdata/" + nombreTweet[1:-2] + ".json", tweet_text) == True:
                    cat.append(categoria[1:-1])
    return tweet_text, cat

def cargaJson(archivo, lista):
    idioma_en = False
    with open(archivo) as json_data:
        d = json.load(json_data)
        if d["lang"] == "en":
            lista.append(d["text"])
            idioma_en = True
    return idioma_en

data,target = cargaTweets("corpus.csv")

#Generamos el pipeline con el sistema que se utilizara	
text_clf = Pipeline([('vect', CountVectorizer()),('tfidf', TfidfTransformer()),('clf', MultinomialNB()),])
#Definimos los parametros que utilizara el sistema
parameters = {'vect__ngram_range': [(1, 1), (1, 2), (1,3)],
              'stop_words': stopwords.words("english"),
              'tfidf__use_idf': (True, False, False),
              'clf__alpha': (1e-2, 1e-3, 1e-4),
            }
#Aplicamos los parametros al sistema
gs_clf = GridSearchCV(text_clf, parameters, n_jobs=-1)
#Entrenamos el sistema
mitad = int(len(data)/2)
gs_clf = gs_clf.fit(data[:mitad], target[:mitad])
#Realizamos la prediccion
predicted = gs_clf.predict(data[mitad+1:])

#-------------------- Resultados ---------------------------------
print(list(predicted))
print(np.mean(predicted == target))
target_names = ['positive','negative','neutral','irrelevant']
print(metrics.classification_report(target, predicted,target_names))
metrics.confusion_matrix(target, predicted)