import collections
import os,glob
import fnmatch
import math
class tf_idf(object):
    def __init__(self, text, papka_train, length_keywords = 15):
        self.__tf = collections.Counter(text[0])
        for i in range(len(text[0])):
            if len(str(text[0][i])) < 2:
                del self.__tf[text[0][i]]
        self.__idf = {}
        self.__tf_idf = {}
        self.__len_text = len(text[0])
        self.__papka = papka_train
        self.__length_keywords = length_keywords
        for i in range(len(text[1])):
            if str(text[1][i]) != str('<n>') and str(text[1][i]) != str('<np>') and str(text[1][i]) != str('<unknown>'):
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
        nf = len(glob.glob(os.path.join(self.__papka, '*.tr')))
        for i in self.__tf:
            nft = 0
            for filename in glob.glob(os.path.join(self.__papka, '*.tr')):
                with open(filename, 'r', encoding="utf-8") as f:
                    text1 = str(f.read())
                    if i in text1.lower():
                        nft += 1
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