import re
from Global import (TF_IDF, tf_idf, bigram, bi_tf_idf)
import os,glob
from tqdm import tqdm
from time import monotonic
from datetime import timedelta


papka_korpus = os.path.dirname(__file__)
#TF_IDF jaily aqparat
print(TF_IDF.__doc__)
#-------------------------------------------------------------------------------------------------

def sozgebolu(text):
    tag = re.findall(r'[<]+\w+[>]+', text)
    sozder = re.split(r'[<]+\w+[>]+', text)
    try:
        if sozder[0][0] == '\ufeff':
        sozder[0] = sozder[0][1:]
    except IndexError:
        pass
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
podkotologs = glob.glob(global_katolog+"Басты жаңалықтар")
globaltime = 0
globalfiles = 0
for podkotolog in podkotologs:
    outdirectory = str(podkotolog).replace('outtexts', 'Keywords')
    os.system('mkdir "{0}"'.format(outdirectory))
    utechka = glob.glob(os.path.join(podkotolog, '*.gt'))
    length = len(utechka)
    pbar = tqdm(utechka)
    start_time = monotonic()
    kol = 1
    katologname = str(podkotolog).replace(global_katolog, '')
    for fail in pbar:
        filename = fail[fail.rfind("/")+1:]
        pbar.set_description(f"Жасалуда {katologname}/{str(filename)}")
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
            TfIdf = tf_idf(text = soz, papka_train = os.path.join(papka_korpus, "train/Басты жаңалықтар/"))

            #esepteuler
            tf = TfIdf.tf_esepteu()
            idf = TfIdf.idf_esepteu()
            tfidf = TfIdf.tf_idf_esepteu()

            #bigram klasssyndagy konstruktordy qoldanyluy
            bi = bigram(text = txt, papka_korpus = papka_korpus)
            text = [bi.newlemm, bi.lastlemm]

            #bigram TF_IDF klasssyndagy konstruktordy qoldanyluy
            BiTfIdf = bi_tf_idf(text = text, papka_train = os.path.join(papka_korpus, "train/Басты жаңалықтар/"))

            bi_tf = BiTfIdf.bi_tf_esepteu()
            bi_idf = BiTfIdf.bi_idf_esepteu()
            bi_tfidf = BiTfIdf.bi_tf_idf_esepteu()
            with open(os.path.join(outdirectory, str(filename[:inddot])+".kw"), 'w', encoding="utf-8") as out_keywords:
                spis = []
                for x in tfidf:
                    spis.append(str(x))
                for x in bi_tfidf:
                    spis.append(str(x))
                out_keywords.write("\n".join(spis))
        if(length == kol):
            end_time = monotonic()
            timedel = end_time - start_time 
            globaltime +=  timedel
            pbar.set_description(f"{katologname} ішкі папкасы aяқталды! Барлығы {length} құжат. Жұмсалған уақыт: {timedelta(seconds=timedel)}")
        kol += 1
    globalfiles += length

print("Аяқталды! Барлығы {0} құжат. Жұмсалған уақыт: {1}".format(globalfiles, timedelta(seconds=globaltime)))
        
