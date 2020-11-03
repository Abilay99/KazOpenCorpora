from PyQt5 import QtWidgets, QtCore, QtGui
from interfaceForm import Ui_MainWindow
import sys
from time import sleep
import os
import glob
from CorporaDB import corporaDB
from subprocess import PIPE, run
import collections, re
import math
papka_korpus = os.path.dirname(__file__)
from sys import platform
OS = "unknown"
__sep = "\\"
if platform == "linux" or platform == "linux2":
    OS = "Linux"
    __sep = "/"
elif platform == "darwin":
    OS = "MacOS"
    __sep = "/"
elif platform == "win32" or platform == "win64":
    OS = "Windows"
    __sep = "\\"

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

#db connect
ob = corporaDB()

lencorp = int(ob.Count_corpora()[0]['sany'])

class EditedApertium_DB():
    def __init__(self, text, apertium):
        self.text = text
        self.apertium = apertium
        np = []
        unknown = []
        soilemder = self.soilemgebolu(self.text)
        self.txttest = str(self.apertium)
        testtxt = re.findall(r"\*\w+\$", self.txttest)
        testtxt = "".join(testtxt)
        testtxt = re.findall(r"\w+", testtxt)
        for soilem in soilemder:
            sozder = self.sozgebolu(soilem)
            for i in range(1,len(sozder)):
                if str(sozder[i][0]).isupper() and sozder[i] in testtxt:
                    np.append(str(sozder[i]))
                elif sozder[i] in testtxt:
                    unknown.append(str(sozder[i]))
        for w in np:
            self.txttest = re.sub(r'\*'+w, w+'<np>', self.txttest)
        for w in unknown:
            self.txttest = re.sub(r'\*'+w, w+'<unknown>', self.txttest)
    def sub(self, newtext):
        newtext = re.sub(r'[.]+([.]|[,]|[!]|[?])+', '. ', newtext)
        newtext = re.sub(r'[,]+([.]|[,]|[!]|[?])+', ', ', newtext)
        newtext = re.sub(r'[?]+([.]|[,]|[!]|[?])+', '? ', newtext)
        newtext = re.sub(r'[!]+([.]|[,]|[!]|[?])+', '! ', newtext)
        newtext = re.sub(r'[.]+', '. ', newtext)
        newtext = re.sub(r'[,]+', ', ', newtext)
        newtext = re.sub(r'[?]+', '? ', newtext)
        newtext = re.sub(r'[!]+', '! ', newtext)
        newtext = re.sub(r'[ ]+\.', '.', newtext)
        newtext = re.sub(r'[ ]+\,', ',', newtext)
        newtext = re.sub(r'[ ]+\?', '?', newtext)
        newtext = re.sub(r'[ ]+\!', '!', newtext)
        newtext = re.sub(r'[" "]+', ' ', newtext)
        return newtext
    def soilemgebolu(self, text):
        res = re.split(r"[.]|[?]|[!]", text)
        if res[len(res)-1] == '':
            del res[len(res)-1]
        return res

    def sozgebolu(self, text):
        return re.findall(r"\w+", text)
    def __str__(self):
        return self.txttest

class outtexts_DB():
    def __init__(self, aptext):
        txtmas = re.findall(r"[\w+|\w|\s|(\w\-\w)]+[<]+\w+[>]|[,|\.|\?|!]+[<]+\w+[>]|[«]+[<]+\w+[>]|[»]+[<]+\w+[>]|[\"]+[<]+\w+[>]|[\"]+[<]+\w+[>]|[\']+[<]+\w+[>]|[\']+[<]+\w+[>]|\n|\n+|[ ]+|[\"]+[<]+\w+[>]|.{1}[<]+lquot+[>]|.{1}[<]+rquot+[>]", aptext)
        self.newtext = ""
        for i in txtmas:
            self.newtext += str(i).replace("^","").replace("<cm>","").replace("<sent>","").replace("<lquot>","").replace("<rquot>","").replace("е<cop>", "")
        self.newtext = re.sub(r'[.]+([.]|[,]|[!]|[?])+', '. ', self.newtext)
        self.newtext = re.sub(r'[,]+([.]|[,]|[!]|[?])+', ', ', self.newtext)
        self.newtext = re.sub(r'[?]+([.]|[,]|[!]|[?])+', '? ', self.newtext)
        self.newtext = re.sub(r'[!]+([.]|[,]|[!]|[?])+', '! ', self.newtext)
        self.newtext = re.sub(r'[.]+', '. ', self.newtext)
        self.newtext = re.sub(r'[,]+', ', ', self.newtext)
        self.newtext = re.sub(r'[?]+', '? ', self.newtext)
        self.newtext = re.sub(r'[!]+', '! ', self.newtext)
        self.newtext = re.sub(r'[ ]+\.', '.', self.newtext)
        self.newtext = re.sub(r'[ ]+\,', ',', self.newtext)
        self.newtext = re.sub(r'[ ]+\?', '?', self.newtext)
        self.newtext = re.sub(r'[ ]+\!', '!', self.newtext)
        self.newtext = re.sub(r'[" "]+', ' ', self.newtext)
    def __str__(self):
        return self.newtext
class train_DB():
    def sozgebolu(self, text):
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
                if j in "abcdefghigklmnopqrstuvwxyzаәбвгғдеёжзийкқлмнңоөпрстуұүфхһцчшщьыъіэюя1234567890-":
                    new += j
            sozder[i] = new
        if sozder[len(sozder)-1] == '':
            del sozder[len(sozder)-1]
        return sozder
    def __init__(self, outtexts):
        f = open(os.path.join(os.path.dirname(__file__), "Global/MorfAnaliz/stopw.txt"), 'r', encoding="utf-8")
        self.stxt = list(f.readlines())
        for i in range(len(self.stxt)):
            l = "" 
            for j in range(len(self.stxt[i])):
                if self.stxt[i][j] != '\n':
                    l += self.stxt[i][j]
            self.stxt[i] = l
        txt = outtexts
        soz = self.sozgebolu(txt)
        n = len(soz)
        i = 0
        while i < n:
            for j in self.stxt:
                if soz[i] == j:
                    soz.remove(j)
                    n -= 1
                    i -= 0 if i == 0 else 1
                    break
            i += 1
        self.sozd = " ".join(soz)
    def __str__(self):
        return self.sozd

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
                    if soz[i] == j:
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

def out(command):
    result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
    return result.stdout
class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.clickbtn)
        self.ui.pushButton_3.clicked.connect(self.reload)
        self.ui.actionOpen.triggered.connect(self.openFileNameDialog)
        self.ui.actionSave.triggered.connect(self.saveFileDialog)
        self.tfidf = {}
        self.bi_tfidf = {}
    def openFileNameDialog(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "","Text Files (*.txt);;All Files (*)", options=options)
        if fileName:
            with open(fileName, 'r', encoding="utf-8") as f:
                self.ui.plainTextEdit.setPlainText(f.read())
    def saveFileDialog(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","<filename>-keywords", "Text Files (*.txt);;All Files (*)", options=options)
        if fileName:
            with open(fileName+".txt", 'w', encoding="utf-8") as f:
                for x in self.tfidf:
                    f.write(str(x)+"\n")
                for x in self.bi_tfidf:
                    f.write(str(x)+"\n") 
    def reload(self):
        if self.ui.rettext() != "":
            self.ui.pushButton.setVisible(False)
            self.ui.progressBar.setVisible(True)
            self.ui.pushButton_2.setVisible(False)
            self.ui.pushButton_3.setVisible(False)
            with open(os.path.join(papka_korpus,'tmp/text.tmp'),'w', encoding="utf-8") as f:
                f.write(self.ui.rettext())
            os.system('''cd $HOME/sources/apertium-kaz-rus\ncat "{0}" | apertium -n -d. kaz-rus-tagger > "{1}"'''.format(os.path.join(papka_korpus,'tmp/text.tmp'), os.path.join(papka_korpus,'tmp/app.tmp')))
            apertium = open(os.path.join(papka_korpus,'tmp/app.tmp'),'r',encoding="utf-8").read()
            eadb = EditedApertium_DB(text = self.ui.rettext(), apertium = apertium)
            editedapertium = str(eadb)
            outtexts = str(outtexts_DB(aptext = editedapertium))
            train = str(train_DB(outtexts = outtexts))
            txt = outtexts
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
            #bigram klasssyndagy konstruktordy qoldanyluy
            bi = bigram(text = txt, papka_korpus = papka_korpus)
            text = [bi.newlemm, bi.lastlemm]

            #TF_IDF klasssyndagy konstruktordy qoldanyluy
            TfIdf = tf_idf(text = soz, len_corp = lencorp, objectCorporaDB = ob)

            #esepteuler
            tf = TfIdf.tf_esepteu()
            self.ui.progressBar.setValue(16)
            idf = TfIdf.idf_esepteu()
            self.ui.progressBar.setValue(32)
            self.tfidf = TfIdf.tf_idf_esepteu()
            self.ui.progressBar.setValue(48)

            #bigram TF_IDF klasssyndagy konstruktordy qoldanyluy
            BiTfIdf = bi_tf_idf(text = text, len_corp = lencorp, objectCorporaDB = ob)
            bi_tf = BiTfIdf.bi_tf_esepteu()
            self.ui.progressBar.setValue(64)
            bi_idf = BiTfIdf.bi_idf_esepteu()
            self.ui.progressBar.setValue(80)
            self.bi_tfidf = BiTfIdf.bi_tf_idf_esepteu()
            self.ui.progressBar.setValue(100)

            row = 1
            col = 0
            font = QtGui.QFont()
            font.setPointSize(12)
            font.setFamily("Times New Roman")
            for x in tf:
                item = QtWidgets.QTableWidgetItem()
                item.setBackground(QtGui.QColor(192,254,255))
                item.setFont(font)
                item.setText(str(x))
                self.ui.tableWidget.setItem(row, col, item)
                item = QtWidgets.QTableWidgetItem()
                item.setBackground(QtGui.QColor(192,254,255))
                item.setFont(font)
                item.setText(str(round(tf[x], 5)))
                self.ui.tableWidget.setItem(row, col+1, item)
                row += 1
            for x in bi_tf:
                item = QtWidgets.QTableWidgetItem()
                item.setBackground(QtGui.QColor(192,254,255))
                item.setFont(font)
                item.setText(str(x))
                self.ui.tableWidget.setItem(row, col, item)
                item = QtWidgets.QTableWidgetItem()
                item.setBackground(QtGui.QColor(192,254,255))
                item.setFont(font)
                item.setText(str(round(bi_tf[x], 5)))
                self.ui.tableWidget.setItem(row, col+1, item)
                row += 1

            row = 1
            col = 2
            for x in idf:
                item = QtWidgets.QTableWidgetItem()
                item.setBackground(QtGui.QColor(192,254,255))
                item.setFont(font)
                item.setText(str(x))
                self.ui.tableWidget.setItem(row, col, item)
                item = QtWidgets.QTableWidgetItem()
                item.setBackground(QtGui.QColor(192,254,255))
                item.setFont(font)
                item.setText(str(round(idf[x], 5)))
                self.ui.tableWidget.setItem(row, col+1, item)
                row += 1
            for x in bi_idf:
                item = QtWidgets.QTableWidgetItem()
                item.setBackground(QtGui.QColor(192,254,255))
                item.setFont(font)
                item.setText(str(x))
                self.ui.tableWidget.setItem(row, col, item)
                item = QtWidgets.QTableWidgetItem()
                item.setBackground(QtGui.QColor(192,254,255))
                item.setFont(font)
                item.setText(str(round(bi_idf[x], 5)))
                self.ui.tableWidget.setItem(row, col+1, item)
                row += 1

            row = 1
            col = 4
            for x in self.tfidf:
                item = QtWidgets.QTableWidgetItem()
                item.setBackground(QtGui.QColor(192,254,255))
                item.setFont(font)
                item.setText(str(x))
                self.ui.tableWidget.setItem(row, col, item)
                item = QtWidgets.QTableWidgetItem()
                item.setBackground(QtGui.QColor(192,254,255))
                item.setFont(font)
                item.setText(str(round(self.tfidf[x], 5)))
                self.ui.tableWidget.setItem(row, col+1, item)
                row += 1
            for x in self.bi_tfidf:
                item = QtWidgets.QTableWidgetItem()
                item.setBackground(QtGui.QColor(192,254,255))
                item.setFont(font)
                item.setText(str(x))
                self.ui.tableWidget.setItem(row, col, item)
                item = QtWidgets.QTableWidgetItem()
                item.setBackground(QtGui.QColor(192,254,255))
                item.setFont(font)
                item.setText(str(round(self.bi_tfidf[x], 5)))
                self.ui.tableWidget.setItem(row, col+1, item)
                row += 1
            if self.ui.progressBar.value() == int(100):
                self.ui.clearbar()
    def clickbtn(self):
        if self.ui.rettext() != "":
            self.ui.pushButton.setVisible(False)
            self.ui.progressBar.setVisible(True)
            with open(os.path.join(papka_korpus,'tmp/text.tmp'),'w', encoding="utf-8") as f:
                f.write(self.ui.rettext())
            os.system('''cd $HOME/sources/apertium-kaz-rus\ncat "{0}" | apertium -n -d. kaz-rus-tagger > "{1}"'''.format(os.path.join(papka_korpus,'tmp/text.tmp'), os.path.join(papka_korpus,'tmp/app.tmp')))
            apertium = open(os.path.join(papka_korpus,'tmp/app.tmp'),'r',encoding="utf-8").read()
            eadb = EditedApertium_DB(text = self.ui.rettext(), apertium = apertium)
            editedapertium = str(eadb)
            outtexts = str(outtexts_DB(aptext = editedapertium))
            train = str(train_DB(outtexts = outtexts))
            txt = outtexts
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
            #bigram klasssyndagy konstruktordy qoldanyluy
            bi = bigram(text = txt, papka_korpus = papka_korpus)
            text = [bi.newlemm, bi.lastlemm]

            #TF_IDF klasssyndagy konstruktordy qoldanyluy
            TfIdf = tf_idf(text = soz, len_corp = lencorp, objectCorporaDB = ob)

            #esepteuler
            tf = TfIdf.tf_esepteu()
            self.ui.progressBar.setValue(16)
            idf = TfIdf.idf_esepteu()
            self.ui.progressBar.setValue(32)
            self.tfidf = TfIdf.tf_idf_esepteu()
            self.ui.progressBar.setValue(48)

            #bigram TF_IDF klasssyndagy konstruktordy qoldanyluy
            BiTfIdf = bi_tf_idf(text = text, len_corp = lencorp, objectCorporaDB = ob)
            bi_tf = BiTfIdf.bi_tf_esepteu()
            self.ui.progressBar.setValue(64)
            bi_idf = BiTfIdf.bi_idf_esepteu()
            self.ui.progressBar.setValue(80)
            self.bi_tfidf = BiTfIdf.bi_tf_idf_esepteu()
            self.ui.progressBar.setValue(100)

            row = 1
            col = 0
            font = QtGui.QFont()
            font.setPointSize(12)
            font.setFamily("Times New Roman")
            for x in tf:
                item = QtWidgets.QTableWidgetItem()
                item.setBackground(QtGui.QColor(192,254,255))
                item.setFont(font)
                item.setText(str(x))
                self.ui.tableWidget.setItem(row, col, item)
                item = QtWidgets.QTableWidgetItem()
                item.setBackground(QtGui.QColor(192,254,255))
                item.setFont(font)
                item.setText(str(round(tf[x], 5)))
                self.ui.tableWidget.setItem(row, col+1, item)
                row += 1
            for x in bi_tf:
                item = QtWidgets.QTableWidgetItem()
                item.setBackground(QtGui.QColor(192,254,255))
                item.setFont(font)
                item.setText(str(x))
                self.ui.tableWidget.setItem(row, col, item)
                item = QtWidgets.QTableWidgetItem()
                item.setBackground(QtGui.QColor(192,254,255))
                item.setFont(font)
                item.setText(str(round(bi_tf[x], 5)))
                self.ui.tableWidget.setItem(row, col+1, item)
                row += 1

            row = 1
            col = 2
            for x in idf:
                item = QtWidgets.QTableWidgetItem()
                item.setBackground(QtGui.QColor(192,254,255))
                item.setFont(font)
                item.setText(str(x))
                self.ui.tableWidget.setItem(row, col, item)
                item = QtWidgets.QTableWidgetItem()
                item.setBackground(QtGui.QColor(192,254,255))
                item.setFont(font)
                item.setText(str(round(idf[x], 5)))
                self.ui.tableWidget.setItem(row, col+1, item)
                row += 1
            for x in bi_idf:
                item = QtWidgets.QTableWidgetItem()
                item.setBackground(QtGui.QColor(192,254,255))
                item.setFont(font)
                item.setText(str(x))
                self.ui.tableWidget.setItem(row, col, item)
                item = QtWidgets.QTableWidgetItem()
                item.setBackground(QtGui.QColor(192,254,255))
                item.setFont(font)
                item.setText(str(round(bi_idf[x], 5)))
                self.ui.tableWidget.setItem(row, col+1, item)
                row += 1

            row = 1
            col = 4
            for x in self.tfidf:
                item = QtWidgets.QTableWidgetItem()
                item.setBackground(QtGui.QColor(192,254,255))
                item.setFont(font)
                item.setText(str(x))
                self.ui.tableWidget.setItem(row, col, item)
                item = QtWidgets.QTableWidgetItem()
                item.setBackground(QtGui.QColor(192,254,255))
                item.setFont(font)
                item.setText(str(round(self.tfidf[x], 5)))
                self.ui.tableWidget.setItem(row, col+1, item)
                row += 1
            for x in self.bi_tfidf:
                item = QtWidgets.QTableWidgetItem()
                item.setBackground(QtGui.QColor(192,254,255))
                item.setFont(font)
                item.setText(str(x))
                self.ui.tableWidget.setItem(row, col, item)
                item = QtWidgets.QTableWidgetItem()
                item.setBackground(QtGui.QColor(192,254,255))
                item.setFont(font)
                item.setText(str(round(self.bi_tfidf[x], 5)))
                self.ui.tableWidget.setItem(row, col+1, item)
                row += 1
            
            self.ui.label_2.setVisible(True)
            self.ui.tabledsgn()
            self.ui.resizewin()
            if self.ui.progressBar.value() == int(100):
                self.ui.clearbar()
    
    




if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    app.setApplicationName("Кілттік сөз")
    app.setApplicationVersion("0.0.1")
    application = mywindow()
    application.show()
    sys.exit(app.exec())
    