import os, glob
path_zhalgau = __file__[:__file__.rfind('/') + 1] + "zhalgau/"
def norm(text):
    l = ""
    for k in range(len(text)):
        if text[k] != '\n':
            l += text[k]
    if l != "":
        text = l
    return str(text)

def Stem(word):
    text2=""
    ltext4=""
    if(len(word) > 14):
        j = open("%s14zh.txt"%path_zhalgau, encoding="utf-8")
        i = 14
        while (i >= 0):
            if i == 13:
                j = open("%s13zh.txt"%path_zhalgau, encoding="utf-8")
            if i == 12:
                j = open("%s12zh.txt"%path_zhalgau, encoding="utf-8")
            if i == 11:
                j = open("%s11zh.txt"%path_zhalgau, encoding="utf-8")
            if i == 10:
                j = open("%s10zh.txt"%path_zhalgau, encoding="utf-8")                
            if i == 9:
                j = open("%s9zh.txt"%path_zhalgau, encoding="utf-8")
            if i == 8:
                j = open("%s8zh.txt"%path_zhalgau, encoding="utf-8")
            if i == 7:
                j = open("%s7zh.txt"%path_zhalgau, encoding="utf-8")
            if i == 6:
                j = open("%s6zh.txt"%path_zhalgau, encoding="utf-8")
            if i == 5:
                j = open("%s5zh.txt"%path_zhalgau, encoding="utf-8")
            if i == 4:
                j = open("%s4zh.txt"%path_zhalgau, encoding="utf-8")
            if i == 3:
                j = open("%s3zh.txt"%path_zhalgau, encoding="utf-8")
            if i == 2:
                j = open("%s2zh.txt"%path_zhalgau, encoding="utf-8")
            if i == 1:
                j = open("%s1zh.txt"%path_zhalgau, encoding="utf-8")
            if i == 0:
                text2 = word
                break
            h = 7
            ltext4 = word[len(word) - i:]
            ltext3 = j.readlines()
            for k in range(len(ltext3)):
                if norm(ltext3[k]) == ltext4:
                    h = 0
            if (h == 0 and i > 6):
                text2 = word[:len(word) - i]
                j.close()
                break
            elif (h == 0 and i < 7):
                k = word[:len(word) - i]
                text2 = k
                i = 0
            i -= 1
            j.close()
    else:
        j = open("%s14zh.txt"%path_zhalgau, encoding="utf-8")
        i = len(word) - 2
        while (i >= 0):
            if i == 14:
                j = open("%s14zh.txt"%path_zhalgau, encoding="utf-8")
            if i == 13:
                j = open("%s13zh.txt"%path_zhalgau, encoding="utf-8")
            if i == 12:
                j = open("%s12zh.txt"%path_zhalgau, encoding="utf-8")
            if i == 11:
                j = open("%s11zh.txt"%path_zhalgau, encoding="utf-8")
            if i == 10:
                j = open("%s10zh.txt"%path_zhalgau, encoding="utf-8")                
            if i == 9:
                j = open("%s9zh.txt"%path_zhalgau, encoding="utf-8")
            if i == 8:
                j = open("%s8zh.txt"%path_zhalgau, encoding="utf-8")
            if i == 7:
                j = open("%s7zh.txt"%path_zhalgau, encoding="utf-8")
            if i == 6:
                j = open("%s6zh.txt"%path_zhalgau, encoding="utf-8")
            if i == 5:
                j = open("%s5zh.txt"%path_zhalgau, encoding="utf-8")
            if i == 4:
                j = open("%s4zh.txt"%path_zhalgau, encoding="utf-8")
            if i == 3:
                j = open("%s3zh.txt"%path_zhalgau, encoding="utf-8")
            if i == 2:
                j = open("%s2zh.txt"%path_zhalgau, encoding="utf-8")
            if i == 1:
                j = open("%s1zh.txt"%path_zhalgau, encoding="utf-8")
            if i == 0:
                text2 = word
                break
            h = 7
            ltext4 = word[len(word) - i:]
            ltext3 = j.readlines()
            for k in range(len(ltext3)):
                if norm(ltext3[k]) == ltext4:
                    h = 0
            if (h == 0 and i > 6):
                text2 = word[:len(word) - i]
                j.close()
                break
            elif (h == 0 and i < 7):
                k = word[:len(word) - i]
                text2 = k
                i = 0
            i -= 1
        j.close()
    #return str(text2+"/"+ltext4)
    return str(text2)

def buttonClick(word):
    s = word
    kk = ""
    text4 =""
    for ff in range(len(s)):
        if (s[ff] != ' ' and s[ff] != '.' and s[ff] != ',' and s[ff] != '!' and s[ff] != '-' and s[ff] != "\n"):
            kk = kk + s[ff]
            if (ff == len(s) - 1):
                text4 += str(Stem(kk))
                kk = ''
        else:
            text4 += str(Stem(kk))
            kk = ''
    return str(text4)

#undestik = {"к":"г", "қ":"ғ", "п":"б", "п":"у"}
#print(buttonClick("араласатындарымыздың"))





