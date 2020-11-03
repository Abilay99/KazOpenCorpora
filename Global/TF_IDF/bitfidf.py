import collections
import os,glob
import fnmatch
import math
class bi_tf_idf(object):
    def __init__(self, text, papka_train, length_keywords = 15):
        self.__bi_tf = collections.Counter(text[0])
        for i in range(len(text[0])):
            if len(str(text[0][i])) < 2:
                del self.__tf[text[0][i]]
        self.__bi_idf = {}
        self.__bi_tf_idf = {}
        self.__len_text = len(text[1])
        self.__papka = papka_train
        self.__length_keywords = length_keywords

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
        nf = len(glob.glob(os.path.join(self.__papka, '*.tr')))
        for i in self.__bi_tf:
            nft = 0
            for filename in glob.glob(os.path.join(self.__papka, '*.tr')):
                with open(filename, 'r', encoding="utf-8") as f:
                    text1 = str(f.read())
                    if i in text1.lower():
                        nft += 1
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