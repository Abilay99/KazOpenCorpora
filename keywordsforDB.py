from CorporaDB import corporaDB
from tqdm import tqdm
from time import monotonic, sleep
from datetime import timedelta
import os, re, glob
import collections
import math
papka_korpus = os.path.dirname(__file__)

class tf_idf(object):
    def __init__(self, text, len_corp, objectCorporaDB, length_keywords = 15):
        self.__tf = collections.Counter(text[0])
        for i in range(len(text[0])):
            if len(str(text[0][i])) < 2:
                del self.__tf[text[0][i]]
        self.__idf = {}
        self.__tf_idf = {}
        self.__len_text = len(text[0])
        self.__len_corp = float(len_corp)
        self.__length_keywords = length_keywords
        self.__obj = objectCorporaDB
        for i in range(len(text[1])):
            if str(text[1][i]) != str('<n>') and str(text[1][i]) != str('<np>'):
                del self.__tf[text[0][i]]

    #===tf===
    def tf_esepteu(self):
        for i in self.__tf:
            self.__tf[i] =  self.__tf[i] / float(self.__len_text)

        new_tf = dict()
        kol = 0
        sort = sorted(self.__tf, key=self.__tf.get, reverse=True)
        for w in sort:
            new_tf[w] = self.__tf[w]
            kol += 1
            if kol == self.__length_keywords:
                break
        return new_tf
        #{w:self.__tf[w] for w in sorted(self.__tf, key=self.__tf.get, reverse=True)}
    #===idf===
    def idf_esepteu(self):
        nf = self.__len_corp
        for i in self.__tf:
            res = self.__obj.for_count_lemmas(phrase=str(i))
            nft = float(res[0]['sany'])
            try:
                self.__idf[i] = math.log(nf/nft, 10)
            except ZeroDivisionError:
                self.__idf[i] = math.log(nf/1.0, 10)
        new_idf = dict()
        kol = 0
        sort = sorted(self.__idf, key=self.__idf.get, reverse=True)
        for w in sort:
            new_idf[w] = self.__idf[w]
            kol += 1
            if kol == self.__length_keywords:
                break
        return new_idf
        #{w:self.__idf[w] for w in sorted(self.__idf, key=self.__idf.get, reverse=True)}
    
    #===tf_idf===
    def tf_idf_esepteu(self):
        for i in self.__tf:
            self.__tf_idf[i] = self.__idf[i]*self.__tf[i]
        new_tf_idf = dict()
        kol = 0
        sort = sorted(self.__tf_idf, key=self.__tf_idf.get, reverse=True)
        for w in sort:
            new_tf_idf[w] = self.__tf_idf[w]
            kol += 1
            if kol == self.__length_keywords:
                break
        return new_tf_idf
        #{w:self.__tf_idf[w] for w in sorted(self.__tf_idf, key=self.__tf_idf.get, reverse=True)}
    
    
#------------------------------------------------------------------------------------------

class bi_tf_idf(object):
    def __init__(self, text, len_corp, objectCorporaDB, length_keywords = 15):
        self.__bi_tf = collections.Counter(text[0])
        for i in range(len(text[0])):
            if len(str(text[0][i])) < 2:
                del self.__tf[text[0][i]]
        self.__bi_idf = {}
        self.__bi_tf_idf = {}
        self.__len_text = len(text[1])
        self.__len_corp = float(len_corp)
        self.__length_keywords = length_keywords
        self.__obj = objectCorporaDB

    #===tf===
    def bi_tf_esepteu(self):
        for i in self.__bi_tf:
            self.__bi_tf[i] =  self.__bi_tf[i] / float(self.__len_text)
        
        new_bi_tf = dict()
        kol = 0
        sort = sorted(self.__bi_tf, key=self.__bi_tf.get, reverse=True)
        for w in sort:
            new_bi_tf[w] = self.__bi_tf[w]
            kol += 1
            if kol == self.__length_keywords:
                break
        return new_bi_tf
        #{w:self.__bi_tf[w] for w in sorted(self.__bi_tf, key=self.__bi_tf.get, reverse=True)}
    
    #===idf===
    def bi_idf_esepteu(self):
        nf = self.__len_corp
        for i in self.__bi_tf:
            res = self.__obj.for_count_lemmas(phrase=str(i))
            nft = float(res[0]['sany'])
            try:
                self.__bi_idf[i] = math.log(nf/nft, 10)
            except ZeroDivisionError:
                self.__bi_idf[i] = math.log(nf/1.0, 10)

        new_bi_idf = dict()
        kol = 0
        sort = sorted(self.__bi_idf, key=self.__bi_idf.get, reverse=True)
        for w in sort:
            new_bi_idf[w] = self.__bi_idf[w]
            kol += 1
            if kol == self.__length_keywords:
                break
        return new_bi_idf
        #{w:self.__bi_idf[w] for w in sorted(self.__bi_idf, key=self.__bi_idf.get, reverse=True)}
    
    #===tf_idf===
    def bi_tf_idf_esepteu(self):
        for i in self.__bi_tf:
            self.__bi_tf_idf[i] = self.__bi_idf[i]*self.__bi_tf[i]
        new_bi_tf_idf = dict()
        kol = 0
        sort = sorted(self.__bi_tf_idf, key=self.__bi_tf_idf.get, reverse=True)
        for w in sort:
            new_bi_tf_idf[w] = self.__bi_tf_idf[w]
            kol += 1
            if kol == self.__length_keywords:
                break
        return new_bi_tf_idf
        #{w:self.__bi_tf_idf[w] for w in sorted(self.__bi_tf_idf, key=self.__bi_tf_idf.get, reverse=True)}
    
    
#------------------------------------------------------------------------------------------

class bigram(object):
    def __init__(self, text, papka_korpus):
        f = open(os.path.join(papka_korpus, "Global/MorfAnaliz/stopw.txt"), 'r', encoding="utf-8")
        stxt = list(f.readlines())
        for i in range(len(stxt)):
            l = "" 
            for j in range(len(stxt[i])):
                if stxt[i][j] != '\n':
                    l += stxt[i][j]
            stxt[i] = l
        soilemder = self.soilemgebolu(text)
        self.newlemm = []
        self.lastlemm = []
        for soilem in soilemder:
            soz_tag = self.sozgebolu(soilem)
            soz = soz_tag[0]
            tag = soz_tag[1]
            n = len(soz)
            i = 0
            while i < n:
                for j in stxt:
                    if soz[i] == j or len(soz[i]) < 2:
                        soz.remove(j)
                        try:
                            del tag[i]
                        except IndexError:
                            pass
                        n -= 1
                        i -= 1
                        break
                    if len(soz[i]) < 2:
                        try:
                            del soz[i]
                            del tag[i]
                        except IndexError:
                            pass
                        n -= 1
                        i -= 1
                        break
                i += 1
            m = len(tag)
            bigrm = self.bigrams(soz, tag, m)
            qq = map(' '.join, bigrm)
            self.newlemm.extend(list(qq))
            self.lastlemm.extend(soz)
    def sozgebolu(self, text):
        tag = re.findall(r'[<]+\w+[>]+', text)
        sozder = re.split(r'[<]+\w+[>]+', text)
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
    def utir(self, args):
        hist = []
        for i in range(len(args)):
            if r"," == args[i]:
                hist.append(i)
        return hist
    def kombinacia(self, args):
        if len(args) == 0:
            args.append(-1)
            args.append(-1)
            yield tuple(args)
        elif len(args) == 1:
            args.append(-1)
            yield tuple(args)
        else:
            args = iter(args)
            hist = []
            hist.append(next(args))
            for i in args:
                hist.append(i)
                yield tuple(hist)
                del hist[0]
    def soilemgebolu(self, text):
        res = re.split(r"[.]|[?]|[!]", text)
        if res[len(res)-1] == '':
            del res[len(res)-1]
        n = len(res)
        i = 0
        while i < n:
            mas1 = self.utir(res[i])
            next_utir = list(self.kombinacia(mas1))
            for j in range(len(next_utir)):
                x = next_utir[j][0]
                y = next_utir[j][1]
                if x != -1 and y != -1:
                    pvk = res[i][x+1:y]
                    kol = pvk.count(r" ")
                    if kol >= 2:
                        res.insert(i+1, res[i][x+1:])
                        res[i] = res[i][:x]
                        n += 1
                        break
                elif x != -1 and y == -1:
                    res.insert(i+1, res[i][x+1:])
                    res[i] = res[i][:x]
                    n += 1
            i += 1
        i = 0
        length = len(res)
        while i < length:
            if res[i] == '':
                del res[i]
                length -= 1
                i -= 1
            elif str(res[i][0]).lower() not in "abcdefghigklmnopqrstuvwxyzаәбвгғдеёжзийкқлмнңоөпрстуұүфхһцчшщьыъіэюя1234567890":
                res[i] = res[i][1:]
            i += 1
        return res
    def bigrams(self, arr, tag, m):
        UaqytAtaulary = ['ғасыр', 'ғ', 'жыл', 'жылы', 'ай', 'күн', 'апта', 'қаңтар', 'ақпан', 'наурыз', 'сәуір', 'мамыр', 'маусым', 'шілде', 'тамыз', 'қыркүйек', 'қазан', 'қараша', 'желтоқсан']
        for i in range(m-1):
            if tag[i] == str(r'<adj>') and tag[i+1] == str(r'<n>'):
                yield tuple([arr[i], arr[i+1]])
            elif tag[i] == str(r'<n>') and tag[i+1] == str(r'<n>'):
                yield tuple([arr[i], arr[i+1]])
            elif tag[i] == str(r'<n>') and tag[i+1] == str(r'<v>'):
                yield tuple([arr[i], arr[i+1]])
            elif tag[i] == str(r'<np>') and tag[i+1] == str(r'<n>'):
                yield tuple([arr[i], arr[i+1]])
            elif tag[i] == str(r'<np>') and tag[i+1] == str(r'<np>'):
                yield tuple([arr[i], arr[i+1]])
            elif tag[i] == str(r'<num>') and arr[i+1] in UaqytAtaulary:
                yield tuple([arr[i], arr[i+1]])

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
f = open(os.path.join(os.path.dirname(__file__),"Global/MorfAnaliz/stopw.txt"), 'r', encoding="utf-8")
stxt = list(f.readlines())
for i in range(len(stxt)):
    l = "" 
    for j in range(len(stxt[i])):
        if stxt[i][j] != '\n':
            l += stxt[i][j]
    stxt[i] = l
#print()
#db connect
ob = corporaDB()

start_with = 75
count = 25
lencorp = int(ob.Count_corpora()[0]['sany'])
while start_with < lencorp:
    results = ob.Selects(start_with = start_with, count_def = count)
    length = len(results)
    for kk in range(length):
        txt = results[kk]['outtext']
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
        TfIdf = tf_idf(text = soz, len_corp = lencorp, objectCorporaDB = ob)

        #esepteuler
        tf = TfIdf.tf_esepteu()
        idf = TfIdf.idf_esepteu()
        tfidf = TfIdf.tf_idf_esepteu()
        

        #bigram klasssyndagy konstruktordy qoldanyluy
        bi = bigram(text = txt, papka_korpus = papka_korpus)
        text = [bi.newlemm, bi.lastlemm]

        #bigram TF_IDF klasssyndagy konstruktordy qoldanyluy
        BiTfIdf = bi_tf_idf(text = text, len_corp = lencorp, objectCorporaDB = ob)
        bi_tf = BiTfIdf.bi_tf_esepteu()
        bi_idf = BiTfIdf.bi_idf_esepteu()
        bi_tfidf = BiTfIdf.bi_tf_idf_esepteu()
        spis = []
        for x in tfidf:
            spis.append(str(x))
        for x in bi_tfidf:
            spis.append(str(x))
        keywords = ", ".join(spis)
        ob.KESTENI_JANARTU(bagan_aty='keywords', bagan_mani=keywords, bagan_id=results[kk]['id'])
    start_with += 25
    if start_with + count > lencorp:
        count = lencorp - start_with
    
    print(f"Qazirge {start_with + count} matin daiyn!")
    
    