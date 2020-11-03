import re
import os
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
                if j in "abcdefghigklmnopqrstuvwxyzаәбвгғдеёжзийкқлмнңоөпрстуұүфхһцчшщьыъіэюя1234567890-":
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
            elif str(res[i][0]).lower() not in "abcdefghigklmnopqrstuvwxyzаәбвгғдеёжзийкқлмнңоөпрстуұүфхһцчшщьыъіэюя1234567890-":
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