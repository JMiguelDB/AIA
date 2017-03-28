import json
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import numpy as np
from sklearn import metrics
from sklearn.model_selection import GridSearchCV, ShuffleSplit
from nltk.corpus import stopwords
from sklearn.cross_validation import train_test_split

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
data = np.array(data)
target = np.array(target)
#Generamos el conjunto para distinguir entre positivos y negativos
data_pos_neg = data[(target == 'positive') | (target == 'negative')]
target_pos_neg = target[(target == 'positive') | (target == 'negative')]
#Generamos el conjunto para distinguir entre tweets con sentimientos frente al resto
data_sent = data[(target == 'positive') | (target == 'negative') | (target == 'irrelevant')]
target_sent = target[(target == 'positive') | (target == 'negative') | (target == 'irrelevant')]
#Generamos el conjunto para distinguir entre tweets positivos frente al resto
data_pos = data[(target == 'positive')]
target_pos = target[(target == 'positive')]
#Generamos el conjunto para distinguir entre tweets negativos frente al resto
data_neg = data[(target == 'negative')]
target_neg = target[(target == 'negative')]

#Generamos un conjunto de entrenamiento y de test para el sistema de clasificación
data_train, data_test, target_train, target_test = train_test_split(data_neg, target_neg, test_size=0.5)

#Generamos el pipeline con el sistema que se utilizara	
text_clf = Pipeline([('tfidf', TfidfVectorizer()),('clf', MultinomialNB()),])
#Definimos los parametros que utilizara el sistema
parameters = {
        'tfidf__ngram_range': [(1, 1), (1, 2), (1, 3)],
        'tfidf__stop_words': [stopwords.words("english")],
        'tfidf__use_idf': [True, False],
        'tfidf__smooth_idf': [True, False],
        'tfidf__sublinear_tf': [True, False],
        'tfidf__binary': [True, False],
        'clf__alpha': [1e-2, 1e-3, 1e-4],
    }
#Aplicamos los parametros al sistema
gs_clf = GridSearchCV(text_clf, parameters, verbose = True, cv = ShuffleSplit(train_size = .25, n_splits = 3, random_state = 1))
#Entrenamos el sistema
print("Iniciado entrenamiento")
gs_clf = gs_clf.fit(data_train, target_train)
print("Entrenamiento realizado")
#Realizamos la prediccion
predicted = gs_clf.predict(target)

#-------------------- Resultados ---------------------------------
#print(list(predicted))
print("Precision del sistema:",np.mean(predicted == target))
target_names = ['positive','negative','neutral','irrelevant']
print(metrics.classification_report(target, predicted,target_names))
print(metrics.confusion_matrix(target, predicted))
