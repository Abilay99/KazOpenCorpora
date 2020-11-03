import re
from Global import (TF_IDF, tf_idf, bigram, bi_tf_idf)
import os,glob
from tqdm import tqdm
from time import monotonic
from datetime import timedelta


papka_korpus = os.path.dirname(__file__)
papka_keywords = os.path.join(papka_korpus, "testKeywords")
papka_outtexts = os.path.join(papka_korpus, "testouttexts")
papka_train = os.path.join(papka_korpus, "testtrain")
#TF_IDF jaily aqparat
print(TF_IDF.__doc__)
#-------------------------------------------------------------------------------------------------

def sozgebolu(text):
    tag = re.findall(r'[<]+\w+[>]+', text)
    sozder = re.split(r'[<]+\w+[>]+', text)
    for i in range(len(sozder)):
        sozder[i] = str(sozder[i]).lower()
        new = ""
        for j in sozder[i]:
            if j in "abcdefghigklmnopqrstuvwxyzаәбвгғдеёжзийкқлмнңоөпрстуұүфхһцчшщьыъіэюя1234567890-":
                new += j
        sozder[i] = new
    if sozder[len(sozder)-1] == '':
        del sozder[len(sozder)-1]
    return [sozder, tag]
#----------------------------------------------------------------------------------------------------

#stopwordtar
f = open(os.path.join(papka_korpus,"Global/MorfAnaliz/stopw.txt"), 'r', encoding="utf-8")
stxt = list(f.readlines())
for i in range(len(stxt)):
    l = "" 
    for j in range(len(stxt[i])):
        if stxt[i][j] != '\n':
            l += stxt[i][j]
    stxt[i] = l

#textter

global_katolog = "/media/gpu2/59f87a06-90bf-49c9-a6c0-34f26ab5287c/SEproject/corporaD/outtexts/" 
files = glob.glob(os.path.join(papka_outtexts, "*.gt"))
length = len(files)
pbar = tqdm(files)
start_time = monotonic()
for fail in pbar:
    filename = fail[fail.rfind("/")+1:]
    pbar.set_description(f"Жасалуда {str(filename)}")
    with open(fail, 'r', encoding="utf-8") as f:
        inddot = filename.rfind(".")
        txt = f.read()
        #failda berilgen matinnen tek sozderdi wygaryp beredi
        soz = sozgebolu(txt)
        #stopwordtard alyp tastau
        n = len(soz[0])
        i = 0
        while i < n:
            for j in stxt:
                if soz[0][i] == j:
                    soz[0].remove(j)
                    del soz[1][i]
                    n -= 1
                    i -= 1
                    break
            i += 1
        #TF_IDF klasssyndagy konstruktordy qoldanyluy
        TfIdf = tf_idf(text = soz, papka_train = papka_train)
        #esepteuler
        tf = TfIdf.tf_esepteu()
        idf = TfIdf.idf_esepteu()
        tfidf = TfIdf.tf_idf_esepteu()
        #bigram klasssyndagy konstruktordy qoldanyluy
        bi = bigram(text = txt, papka_korpus = papka_korpus)
        text = [bi.newlemm, bi.lastlemm]
        #bigram TF_IDF klasssyndagy konstruktordy qoldanyluy
        BiTfIdf = bi_tf_idf(text = text, papka_train = papka_train)
        bi_tf = BiTfIdf.bi_tf_esepteu()
        bi_idf = BiTfIdf.bi_idf_esepteu()
        bi_tfidf = BiTfIdf.bi_tf_idf_esepteu()
        with open(os.path.join(papka_keywords, str(filename[:inddot])+".kw"), 'w', encoding="utf-8") as out_keywords:
            spis = []
            for x in tfidf:
                spis.append(str(x))
            for x in bi_tfidf:
                spis.append(str(x))
            out_keywords.write("\n".join(spis))
end_time = monotonic()
timedel = end_time - start_time 

print("Аяқталды! Барлығы {0} құжат. Жұмсалған уақыт: {1}".format(length, timedelta(seconds=timedel)))
        
