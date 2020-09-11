import os
from Global import (TF_IDF, bi_tf_idf, bigram)

papka_korpus = os.path.dirname(__file__)
papka_train = os.path.join(os.path.dirname(__file__), "train")
#TF_IDF jaily aqparat
print(TF_IDF.__doc__)

def head(text):
    string = "\n"
    i = 0
    while i < 70:
        string += "="
        i += 1
    string += "\n"
    i = 0
    while i < int(35-len(text)/2):
        string += " "
        i += 1
    string += text + "\n"
    i = 0
    while i < 70:
        string += "="
        i += 1
    string += "\n"
    return string

f = open(os.path.join(os.path.join(papka_korpus, "outtexts"), "Elbasy kitaptary.gototrain"), 'r', encoding="utf-8")
txt = f.read()

bi = bigram(text = txt, papka_korpus = papka_korpus)

text = [bi.newlemm, bi.lastlemm]

BiTfIdf = bi_tf_idf(text = text, papka_train = papka_train)
bi_tf = BiTfIdf.bi_tf_esepteu()
bi_idf = BiTfIdf.bi_idf_esepteu()
bi_tfidf = BiTfIdf.bi_tf_idf_esepteu()


#sozderdin tf korsetkiwi
print(head("tf"))
for x in bi_tf:
    print(x.ljust(50,' ')+"~"+str(bi_tf[x]))

#sozderdin idf korsetkiwi
print(head("idf"))
for x in bi_idf:
    print(x.ljust(50,' ')+"~"+str(bi_idf[x]))

#sozderdin tf_idf korsetkiwi
print(head("tf-idf"))
for x in bi_tfidf:
    print(x.ljust(50,' ')+"~"+str(bi_tfidf[x]))
print(head("end."))