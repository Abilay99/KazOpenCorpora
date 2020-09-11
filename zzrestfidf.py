import re
from Global import (TF_IDF, tf_idf)
import os
papka_korpus = os.path.dirname(__file__)
papka_train = os.path.join(os.path.dirname(__file__), "train")
#TF_IDF jaily aqparat
print(TF_IDF.__doc__)

#-------------------------------------------------------------------------------------------------
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


def sozgebolu(text):
    tag = re.findall(r'[<]+\w+[>]+', text)
    sozder = re.split(r'[<]+\w+[>]+', text)
    if sozder[0][0] == '\ufeff':
        sozder[0] = sozder[0][1:]
    for i in range(len(sozder)):
        sozder[i] = str(sozder[i]).lower()
        new = ""
        for j in sozder[i]:
            if j in "abcdefghigklmnopqrstuvwxyzаәбвгғдеёжзийкқлмнңоөпрстуұүфхһцчшщьыъіэюя1234567890":
                new += j
        sozder[i] = new
    if sozder[len(sozder)-1] == '':
        del sozder[len(sozder)-1]
    return [sozder, tag]
#----------------------------------------------------------------------------------------------------
fl = open(os.path.join(os.path.join(papka_korpus, "outtexts"), "Elbasy kitaptary.gototrain"), 'r', encoding="utf-8")
txt = fl.read()

f = open(os.path.join(papka_korpus,"Global/MorfAnaliz/stopw.txt"), 'r', encoding="utf-8")
stxt = list(f.readlines())
for i in range(len(stxt)):
    l = "" 
    for j in range(len(stxt[i])):
        if stxt[i][j] != '\n':
            l += stxt[i][j]
    stxt[i] = l
#failda berilgen matinnen tek sozderdi wygaryp beredi
soz = sozgebolu(txt)
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
tf = TfIdf.tf_esepteu()
idf = TfIdf.idf_esepteu()
tfidf = TfIdf.tf_idf_esepteu()

#sozderdin tf korsetkiwi
print(head("tf"))
for x in tf:
    print(x.ljust(50,' ')+"~"+str(tf[x]))

#sozderdin idf korsetkiwi
print(head("idf"))

for x in idf:
    print(x.ljust(50,' ')+"~"+str(idf[x]))

#sozderdin tf_idf korsetkiwi
print(head("tf-idf"))
for x in tfidf:
    print(x.ljust(50,' ')+"~"+str(tfidf[x]))
print(head("end."))