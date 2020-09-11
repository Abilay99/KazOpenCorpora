"""
КАЙ ЖАЛГАУДАН КЕЙЫН КАЙ ЖАЛГАУ

KT, TC, CJ, 
KC, TJ,  
KJ,  

KTC, KTJ, TCJ,
KCJ, 

KTCJ

"""
import os
path_jturi = __file__[:__file__.rfind('\\') + 1] + "jturi\\"
def Zat_esim_jalgaulary(word):
    for i in range(2,len(word),1):
        jalgau = word[i:]
        koptik = open(os.path.join(path_jturi,'koptik.txt'), encoding = 'UTF-8')
        k = koptik.readlines()
        zhiktik = open(os.path.join(path_jturi,'zhiktik.txt'), encoding = 'UTF-8')
        zh = zhiktik.readlines()
        septik = open(os.path.join(path_jturi,'septik.txt'), encoding = 'UTF-8')
        s = septik.readlines()
        taueldilik = open(os.path.join(path_jturi,'taueldilik.txt'), encoding = 'UTF-8')
        t = taueldilik.readlines()
        def tekseru(file):
            for i in range(len(file)):
                newText = ""
                for j in range(len(file[i])):
                    if file[i][j] != '\n':
                        newText += file[i][j]
                if newText != "":
                    file[i] = newText
            return file

        k = tekseru(k)
        zh = tekseru(zh)
        s = tekseru(s)
        t = tekseru(t)

        kf = False
        zhf = False
        sf = False
        tf = False

        subtxt = ""
        txt = ""
        l = len(jalgau)
        word2 = []
        word3 = []
        word4 = []
        """word5 = []
        word6 = []
        word7 = []
        word8 = []
        word9 = []
        word10 = []
        word11 = []
        word12 = []
        word13 = []
        word14 = []"""
        #region
        if l <= 2:
            for i in range(len(t)):
                if jalgau == t[i]:
                    tf = True
            if tf != True:  
                for i in range(len(zh)):
                    if jalgau == zh[i]:
                        zhf = True
            if zhf != True:
                for i in range(len(s)):
                    if jalgau == s[i]:
                        sf = True
                if tf:
                    word2.append("<taueldilik>")
                if sf:
                    word2.append("<septik>")
                if zhf:
                    word2.append("<zhiktik>")

        elif l == 3:
            for i in range(len(k)):
                if jalgau == k[i]:
                    kf = True
                    word3.append("<koptik>") 
            for i in range(len(t)):
                if jalgau == t[i]:
                    tf = True
                    word3.append("<taueldilik>")
            for i in range(len(s)):
                if jalgau == s[i]:
                    sf = True
                    word3.append("<septik>")
            for i in range(len(zh)):
                if jalgau == zh[i]:
                    zhf = True
                    word3.append("<zhiktik>") 
            if kf != True and tf != True and sf != True and zhf != True:
                for i in range(len(t)):
                    if jalgau[0] == t[i]:
                        tf = True
                        word3.append("<taueldilik>")         
                if tf:
                    for i in range(len(s)):
                        if jalgau[1:] == s[i]:
                            sf = True
                            word3.append("<septik>")         

        elif l == 4:
            for i in range(len(t)):
                if jalgau[0] == t[i]:
                    tf = True
                    word4.append("<taueldilik>") 
            for i in range(len(s)):
                if jalgau[0] == s[i]:
                    sf = True
                    word4.append("<septik>")
            if tf:
                for i in range(len(s)):
                    if jalgau[1:] == s[i]:
                        sf = True
                        word4.append("<septik>") 
                if sf != True:
                    for i in range(len(zh)):
                        if jalgau[1:] == zh[i]:
                            zhf = True
                            word4.append("<zhiktik>")
            if sf:
                for i in range(len(zh)):
                    if jalgau[1:] == zh[i]:
                        zhf = True
                        txt += jalgau[1:] + "<zhiktik> "
            if (sf != True and zhf != True) or (tf != True and zhf != True):
                txt = ""
                for i in range(len(t)):
                    if jalgau[:2] == t[i]:
                        tf = True
                        txt = jalgau[:2] + "<taueldilik> " 
                for i in range(len(s)):
                    if jalgau[:2] == s[i]:
                        sf = True
                        txt = jalgau[:2] + "<septik> "
                if tf:
                    for i in range(len(s)):
                        if jalgau[2:] == s[i]:
                            sf = True
                            txt += jalgau[2:] + "<septik> " 
                        if sf != True:
                            for i in range(len(zh)):
                                if jalgau[2:] == zh[i]:
                                    zhf = True
                                    txt += jalgau[2:] + "<zhiktik> "
                if sf:
                    for i in range(len(zh)):
                        if jalgau[2:] == zh[i]:
                            zhf = True
                            txt += jalgau[2:]+"<zhiktik> "
            if (tf == True and sf != True and zhf != True) or (sf == True and tf != True and zhf != True):
                txt = ""
                if sf:
                    sf = False
                if tf:
                    tf = False
                for i in range(len(k)):
                    if jalgau[:3] == k[i]:
                        kf = True
                        txt += jalgau[:3] + "<koptik> "
                if kf != True:
                    for i in range(len(t)):
                        if jalgau[:3] == t[i]:
                            tf = True
                            txt += jalgau[:3] + "<taueldilik> "
                    if tf != True:
                        for i in range(len(s)):
                            if jalgau[:3] == s[i]:
                                sf = True
                                txt += jalgau[:3] + "<septik> " 
                    else:
                        for i in range(len(s)):
                            if jalgau[3:] == s[i]:
                                txt += jalgau[3:] + "<septik> "
                                sf = True
                        if sf != True:
                            for i in range(len(zh)):
                                if jalgau[3:] == zh[i]:
                                    txt += jalgau[3:] + "<zhiktik> "
                                    zhf = True
                else:
                    for i in range(len(t)):
                        if jalgau[3:] == t[i]:
                            txt += jalgau[3:] + "<taueldilik> "
                            tf = True
                    if tf != True:
                        for i in range(len(s)):
                            if jalgau[3:] == s[i]:
                                txt += jalgau[3:] + "<septik> "
                                sf = True
                    if sf != True:
                        for i in range(len(zh)):
                            if jalgau[3:] == zh[i]:
                                txt += jalgau[3:] + "<zhiktik> "
                                zhf = True
            if sf != True and tf != True and zhf != True and kf != True:
                for i in range(len(t)):
                    if jalgau == t[i]:
                        txt += jalgau + "<taueldilik> "
                        tf = True
                    
        elif l == 5:
            txt = ""
            for i in range(len(t)):
                if jalgau[0] == t[i]:
                    txt = jalgau[0] + '<taueldilik> '
                    tf = True 
            if tf:
                for i in range(len(s)):
                    if jalgau[1] == s[i]:
                        txt += jalgau[1] + '<septik> '
                        sf = True
                if sf:
                    for i in range(len(zh)):
                        if jalgau[2:] == zh[i]:
                            txt += jalgau[2:] + '<zhiktik> '
                            zhf = True
            if zhf != True:
                for i in range(len(t)):
                    if jalgau[:2] == t[i]:
                        txt = jalgau[:2] + '<taueldilik> '
                        tf = True
                for i in range(len(s)):
                    if jalgau[:2] == s[i]:
                        txt += jalgau[:2] + '<septik> '
                        sf = True
                if tf:
                    tf = False
                    for i in range(len(zh)):
                        if jalgau[2:] == zh[i]:
                            txt += jalgau[2:] + '<zhiktik> '
                            zhf = True
                    for i in range(len(s)):
                        if jalgau[2:] == s[i]:
                            txt += jalgau[2:] + '<septik> '
                if sf:
                    sf = False
                    for i in range(len(zh)):
                        if jalgau[2:] == zh[i]:
                            txt += jalgau[2:] + '<zhiktik> '
                            zhf = True
            if zhf != True and sf != True:
                for i in range(len(k)):
                    if jalgau[:3] == k[i]:
                        txt = jalgau[:3] + '<koptik> '
                        kf = True
                for i in range(len(t)):
                    if jalgau[:3] == t[i]:
                        txt = jalgau[:3] + '<taueldilik> '
                        tf = True
                if kf:
                    for i in range(len(t)):
                        if jalgau[3:] == t[i]:
                            txt += jalgau[3:] + '<taueldilik> '
                            tf = True
                    for i in range(len(s)):
                        if jalgau[3:] == s[i]:
                            txt += jalgau[3:] + '<septik> '
                            sf = True
                if tf:
                    for i in range(len(s)):
                        if jalgau[3:] == s[i]:
                            txt += jalgau[3:] + '<septik> '
                            sf = True
            if zhf != True and sf != True:
                tf = False
                for i in range(len(t)):
                    if jalgau[:4] == t[i]:
                        txt = jalgau[:4] + '<taueldilik> '
                        tf = True
                if tf:
                    for i in range(len(s)):
                        if jalgau[4] == s[i]:
                            txt += jalgau[4] + '<septik> '
                            sf = True

        elif l == 6:
            for i in range(len(zh)):
                if jalgau == zh[i]:
                    txt = jalgau + '<zhiktik> '
                    zhf = True
            if True != zhf:
                for i in range(len(t)):
                    if jalgau[0] == t[i]:
                        txt = jalgau[0] + '<taueldilik> '
                        tf = True
                if tf:
                    for i in range(len(s)):
                        if jalgau[1:3] == s[i]:
                            txt += jalgau[1:3] + '<septik> '
                            sf = True
                    if sf:
                        for i in range(len(zh)):
                            if jalgau[3:] == zh[i]:
                                txt += jalgau[3:] + '<zhiktik> '
                                zhf = True
            if zhf != True:
                txt = ""
                tf = False
                for i in range(len(t)):
                    if jalgau[:2] == t[i]:
                        txt = jalgau[:2] + '<taueldilik> '
                        tf = True
                if tf:
                    for i in range(len(s)):
                        if jalgau[2] == s[i]:
                            txt += jalgau[2] + '<septik>1 '
                            sf = True
                    if sf:
                        for i in range(len(zh)):
                            if jalgau[3:] == zh[i]:
                                txt += jalgau[3:] + '<zhiktik> '
                                zhf = True
            if zhf != True:
                txt = ""
                for i in range(len(k)):
                    if jalgau[:3] == k[i]:
                        txt = jalgau[:3] + '<koptik> '
                        kf = True
                for i in range(len(t)):
                    if jalgau[:3] == t[i]:
                        txt = jalgau[:3] + '<taueldilik> '
                        tf = True
                for i in range(len(s)):
                    if jalgau[:3] == s[i]:
                        txt = jalgau[:3] + '<septik> '
                        sf = True
                if tf:
                    for i in range(len(s)):
                        if jalgau[3:] == s[i]:
                            txt += jalgau[3:] + '<septik> '
                            sf = True
                    for i in range(len(zh)):
                        if jalgau[3:] == zh[i]:
                            txt += jalgau[3:] + '<zhiktik> '
                            zhf = True            
                if sf:
                    for i in range(len(zh)):
                        if jalgau[3:] == zh[i]:
                            txt += jalgau[3:] + '<zhiktik> '
                            zhf = True
                if kf:
                    subtxt = txt
                    for i in range(len(t)):
                        if jalgau[3:] == t[i]:
                            txt += jalgau[3:] + '<taueldilik> '
                            tf = True
                    for i in range(len(s)):
                        if jalgau[3:] == s[i]:
                            txt += jalgau[3:] + '<septik> '
                            sf = True
                    if tf != True:
                        for i in range(len(zh)):
                            if jalgau[3:] == zh[i]:
                                txt += jalgau[3:] + '<zhiktik> '
                                zhf = True
                    if zhf != True and sf != True and tf != True:    
                        for i in range(len(t)):
                            if jalgau[3] == t[i]:
                                txt += jalgau[3] + '<taueldilik> '
                                tf = True
                        if tf:
                            for i in range(len(s)):
                                if jalgau[4:] == s[i]:
                                    txt += jalgau[4:] + '<septik> '
                                    sf = True
                        if sf != True:
                            sf = False
                            txt = subtxt
                            for i in range(len(t)):
                                if jalgau[3:5] == t[i]:
                                    txt += jalgau[3:5] + '<taueldilik> '
                                    tf = True
                            if tf:
                                for i in range(len(s)):
                                    if jalgau[5] == s[i]:
                                        txt += jalgau[5] + '<septik> '
                                        sf = True
            if zhf != True and sf != True:
                for i in range(len(t)):
                    if jalgau[:4] == t[i]:
                        txt += jalgau[:4] + '<taueldilik> '
                        tf = True
                if tf:
                    for i in range(len(s)):
                        if jalgau[4:] == s[i]:
                            txt += jalgau[4:] + '<septik> '
                            sf = True
                
        elif l == 7:
            for i in range(len(t)):
                if jalgau[0] == t[i]:
                    txt = jalgau[0] + '<taueldilik> '
                    tf = True
            for i in range(len(s)):
                if jalgau[0] == s[i]:
                    txt = jalgau[0] + '<septik> '
                    sf = True
            if tf:
                for i in range(len(s)):
                    if jalgau[1:4] == s[i]:
                        txt += jalgau[1:4] + '<septik> '
                        sf = True
                if sf:
                    for i in range(len(zh)):
                        if jalgau[4:] == zh[i]:
                            txt += jalgau[4:] + '<zhiktik> '
                            zhf = True
                if zhf != True:
                    for i in range(len(zh)):
                        if jalgau[1:] == zh[i]:
                            txt += jalgau[1:] + '<zhiktik> '
                            zhf = True
            if sf:
                for i in range(len(zh)):
                    if jalgau[1:] == zh[i]:
                        txt += jalgau[1:] + '<zhiktik> '
                        zhf = True
            if zhf != True:
                sf = False              # ZHOGARYDA OZGERUI MUMKIN 
                for i in range(len(t)):
                    if jalgau[:2] == t[i]:
                        txt = jalgau[:2] + '<taueldilik> '
                        tf = True
                if tf:
                    for i in range(len(s)):
                        if jalgau[2:4] == s[i]:
                            txt += jalgau[2:4] + '<septik> '
                            sf = True
                    if sf:
                        for i in range(len(zh)):
                            if jalgau[4:] == zh[i]:
                                txt += jalgau[4:] + '<zhiktik> '
                                zhf = True
            if zhf != True:
                for i in range(len(k)):
                    if jalgau[:3] == k[i]:
                        txt = jalgau[:3] + "<koptik> "
                        kf = True
                for i in range(len(t)):
                    if jalgau[:3] == t[i]:
                        txt = jalgau[3] + '<taueldilik> '
                        tf = True
                if tf:
                    for i in range(len(s)):
                        if jalgau[3] == s[i]:
                            txt += jalgau[3] + '<septik> '
                            sf = True
                    if sf:
                        for i in range(len(zh)):
                            if jalgau[4:] == zh[i]:
                                txt += jalgau[4:] + '<zhiktik> '
                                zhf = True
                if kf:
                    subtxt = txt
                    for i in range(len(s)):
                        if jalgau[3] == s[i]:
                            txt += jalgau[3] + '<septik> '
                            sf = True
                    for i in range(len(t)):
                        if jalgau[3] == t[i]:
                            txt += jalgau[3] + '<taueldilik> '
                            tf = True
                    if sf:
                        for i in range(len(zh)):
                            if jalgau[4:] == zh[i]:
                                txt += jalgau[4:] + '<zhiktik> '
                                zhf = True
                    if tf:
                        for i in range(len(s)):
                            if jalgau[4:] == s[i]:
                                txt += jalgau[4:] + '<septik> '
                                sf = True
                        for i in range(len(zh)):
                            if jalgau[4:] == zh[i]:
                                txt += jalgau[4:] + '<zhiktik> '
                                zhf = True
                    if zhf != True and sf != True:
                        txt = subtxt
                        for i in range(len(t)):
                            if jalgau[3:5] == t[i]:
                                txt += jalgau[3:5] + '<taueldilik> '
                                tf = True
                        if tf:
                            for i in range(len(s)):
                                if jalgau[5:] == s[i]:
                                    txt += jalgau[5:] + '<septik> '
                                    sf = True
                    if zhf != True and sf != True:
                        txt = subtxt
                        for i in range(len(t)):
                            if jalgau[3:] == t[i]:
                                txt += jalgau[3:] + '<taueldilik> '
                                tf = True
            if zhf != True and sf != True:
                for i in range(len(t)):
                    if jalgau[:4] == t[i]:
                        txt = jalgau[:4] + '<taueldilik> '
                        tf = True
                if tf:
                    for i in range(len(s)):
                        if jalgau[4:] == s[i]:
                            txt += jalgau[4:] + '<septik> '
                            sf = True
                    if sf != True:
                        for i in range(len(zh)):
                            if jalgau[4:] == zh[i]:
                                txt += jalgau[4:] + '<zhiktik> '
                                zhf = True

        elif l == 8:
            for i in range(len(t)):
                if jalgau[0] == t[i]:
                    txt = jalgau[0] + '<taueldilik> '
                    tf = True
            if tf:
                for i in range(len(s)):
                    if jalgau[1] == s[i]:
                        txt += jalgau[1] + '<septik> '
                        sf = True
                if sf:
                    for i in range(len(zh)):
                        if jalgau[2:] == zh[i]:
                            txt += jalgau[2:] + '<zhiktik> '
                            zhf = True
            if zhf != True:
                for i in range(len(t)):
                    if jalgau[:2] == t[i]:
                        txt = jalgau[:2] + '<taueldilik> '
                        tf = True
                for i in range(len(s)):
                    if jalgau[:2] == s[i]:
                        txt = jalgau[:2] + '<septik> '
                        sf = True
                if tf:
                    for i in range(len(s)):
                        if jalgau[2:5] == s[i]:
                            txt += jalgau[2:5] + '<septik> '
                            sf = True
                    if sf:
                        for i in range(len(zh)):
                            if jalgau[5:] == zh[i]:
                                txt += jalgau[5:] + '<zhiktik> '
                                zhf = True
                    if zhf != True:
                        for i in range(len(zh)):
                            if jalgau[2:] == zh[i]:
                                txt += jalgau[2:] + '<zhiktik> '
                                zhf = True
                if sf:
                    for i in range(len(zh)):
                        if jalgau[2:] == zh[i]:
                            txt += jalgau[2:] + '<zhiktik> '
                            zhf = True
            if zhf != True:
                for i in range(len(k)):
                    if jalgau[:3] == k[i]:
                        txt = jalgau[:3] + "<koptik> "
                        kf = True
                for i in range(len(t)):
                    if jalgau[:3] == t[i]:
                        txt = jalgau[:3] + '<taueldilik> '
                        tf = True
                if kf:
                    for i in range(len(t)):
                        if jalgau[3:5] == t[i]:
                            txt += jalgau[3:5] + '<taueldilik> '
                            tf = True
                    for i in range(len(s)):
                        if jalgau[3:5] == s[i]:
                            txt += jalgau[3:5] + '<septik> '
                            sf = True
                    if tf:
                        sf = False
                        for i in range(len(zh)):
                            if jalgau[5:] == zh[i]:
                                txt += jalgau[5:] + '<zhiktik> '
                                zhf = True
                        for i in range(len(s)):
                            if jalgau[5:] == s[i]:
                                txt += jalgau[5:] + '<septik> '
                    if sf:
                        for i in range(len(zh)):
                            if jalgau[5:] == zh[i]:
                                txt += jalgau[5:] + '<zhiktik> '
                                zhf = True
                    if zhf != True and sf != True:
                        tf = False
                        for i in range(len(t)):
                            if jalgau[3:7] == t[i]:
                                txt = jalgau[3:7] + '<taueldilik> '
                                tf = True
                        if tf:
                            for i in range(len(s)):
                                if jalgau[7] == s[i]:
                                    txt += jalgau[7] + '<septik> '
                                    sf = True
                if tf:
                    sf = False
                    for i in range(len(s)):
                        if jalgau[3:5] == s[i]:
                            txt += jalgau[3:5] + '<septik> '
                            sf = True
                    if sf:
                        for i in range(len(zh)):
                            if jalgau[5:] == zh[i]:
                                txt += jalgau[5:] + '<zhiktik> '
                                zhf = True
            if zhf != True and sf != True:
                zhf = False
                for i in range(len(t)):
                    if jalgau[:4] == t[i]:
                        txt = jalgau[:4] + '<taueldilik> '
                        tf = True
                if tf:
                    for i in range(len(s)):
                        if jalgau[4] == s[i]:
                            txt += jalgau[4] + '<septik> '
                            sf = True
                    if sf:
                        for i in range(len(zh)):
                            if jalgau[5:] == zh[i]:
                                txt += jalgau[5:] + '<zhiktik> '
                                zhf = True

        elif l == 9:
            for i in range(len(t)):
                if jalgau[0] == t[i]:
                    txt = jalgau[0] + "<taueldilik> "
                    tf = True
            if tf:
                for i in range(len(s)):
                    if jalgau[1:3] == s[i]:
                        txt += jalgau[1:3] + '<septik> '
                        sf = True
                if sf:
                    for i in range(len(zh)):
                        if jalgau[3:] == zh[i]:
                            txt += jalgau[3:] + '<zhiktik> '
                            zhf = True
            if zhf != True:
                tf = False
                for i in range(len(t)):
                    if jalgau[:2] == t[i]:
                        txt += jalgau[:2] + "<taueldilik> "
                        tf = True
                if tf:
                    for i in range(len(s)):
                        if jalgau[2] == s[i]:
                            txt += jalgau[2] + '<septik> '
                            sf = True
                    if sf:
                        for i in range(len(zh)):
                            if jalgau[3:] == zh[i]:
                                txt += jalgau[3:] + '<zhiktik> '
                                zhf = True 
            if zhf != True:
                for i in range(len(k)):
                    if jalgau[:3] == k[i]:
                        txt = jalgau[:3] + "<koptik> "
                        kf = True
                for i in range(len(t)):
                    if jalgau[:3] == t[i]:
                        txt = jalgau[:3] + "<taueldilik> "
                        tf = True
                for i in range(len(s)):
                    if jalgau[:3] == s[i]:
                        txt = jalgau[:3] + '<septik> '
                        sf = True
                if kf:
                    subtxt = txt
                    for i in range(len(t)):
                        if jalgau[3] == t[i]:
                            txt += jalgau[3] + "<taueldilik> "
                            tf = True
                    if tf:
                        for i in range(len(s)):
                            if jalgau[4:6] == s[i]:
                                txt += jalgau[4:6] + '<septik> '
                                sf = True
                        if sf:
                            for i in range(len(zh)):
                                if jalgau[6:] == zh[i]:
                                    txt += jalgau[6:] + '<zhiktik> '
                                    zhf = True
                    if zhf != True:
                        txt = subtxt
                        tf = False
                        for i in range(len(t)):
                            if jalgau[3:5] == t[i]:
                                txt += jalgau[3:5] + "<taueldilik> "
                                tf = True
                        if tf:
                            for i in range(len(s)):
                                if jalgau[5] == s[i]:
                                    txt += jalgau[5] + '<septik> '
                                    sf = True
                            if sf:
                                for i in range(len(zh)):
                                    if jalgau[6:] == zh[i]:
                                        txt += jalgau[6:] + '<zhiktik> '
                                        zhf = True
                    if zhf != True:
                        for i in range(len(t)):
                            if jalgau[3:6] == t[i]:
                                txt = jalgau[3:6] + "<taueldilik> "
                                tf = True
                        for i in range(len(s)):
                            if jalgau[3:6] == s[i]:
                                txt += jalgau[3:6] + '<septik> '
                                sf = True
                        if tf:
                            for i in range(len(s)):
                                if jalgau[6:] == s[i]:
                                    txt += jalgau[6:] + '<septik> '
                                    sf = True                        
                            for i in range(len(zh)):
                                if jalgau[6:] == zh[i]:
                                    txt += jalgau[6:] + '<zhiktik> '
                                    zhf = True
                        if sf:
                            for i in range(len(zh)):
                                if jalgau[6:] == zh[i]:
                                    txt += jalgau[6:] + '<zhiktik> '
                                    zhf = True
                    if zhf != True and sf != True:
                        txt = subtxt
                        for i in range(len(t)):
                            if jalgau[3:7] == t[i]:
                                txt += jalgau[3:7] + "<taueldilik> "
                                tf = True
                        if tf:
                            for i in range(len(s)):
                                if jalgau[7:] == s[i]:
                                    txt += jalgau[7:] + '<septik> '
                                    sf = True    
                    if zhf != True and sf != True:
                        for i in range(len(zh)):
                            if jalgau[3:] == zh[i]:
                                txt += jalgau[3:] + '<zhiktik> '
                                zhf = True
                if tf:
                    sf = False
                    for i in range(len(s)):
                        if jalgau[3:6] == s[i]:
                            txt += jalgau[3:6] + '<septik> '
                            sf = True
                    if sf:
                        for i in range(len(zh)):
                            if jalgau[6:] == zh[i]:
                                txt += jalgau[6:] + '<zhiktik> '
                                zhf = True
                    if zhf != True:
                        for i in range(len(zh)):
                            if jalgau[3:] == zh[i]:
                                txt += jalgau[3:] + '<zhiktik> '
                                zhf = True
                if sf:
                    for i in range(len(zh)):
                        if jalgau[3:] == zh[i]:
                            txt += jalgau[3:] + '<zhiktik> '
                            zhf = True
            if zhf != True and sf != True:
                for i in range(len(t)):
                    if jalgau[:4] == t[i]:
                        txt = jalgau[:4] + "<taueldilik> "
                        tf = True
                if tf:
                    for i in range(len(s)):
                        if jalgau[4:6] == s[i]:
                            txt += jalgau[4:6] + '<septik> '
                            sf = True
                    if sf:
                        for i in range(len(zh)):
                            if jalgau[6:] == zh[i]:
                                txt += jalgau[6:] + '<zhiktik> '
                                zhf = True

        elif l == 10:
            if tf != True:
                for i in range(len(k)):
                    if jalgau[:3] == k[i]:
                        txt += jalgau[:3] + "<koptik> "
                        kf = True
                if kf:
                    subtxt = txt
                    for i in range(len(t)):
                        if jalgau[3] == t[i]:
                            txt += jalgau[3] + '<taueldilik> '
                            tf = True
                    for i in range(len(s)):
                        if jalgau[3] == s[i]:
                            txt += jalgau[3] + '<septik> '
                            sf = True
                    if tf:
                        for i in range(len(zh)):
                            if jalgau[4:] == zh[i]:
                                txt += jalgau[4:] + '<zhiktik> '
                                zhf = True
                        if zhf != True:
                            for i in range(len(s)):
                                if jalgau[4:7] == s[i]:
                                    txt += jalgau[4:7] + '<septik> '
                                    sf = True
                            if sf:
                                for i in range(len(zh)):
                                    if jalgau[7:] == zh[i]:
                                        txt += jalgau[7:] + '<zhiktik> '
                                        zhf = True
                    if sf:
                        for i in range(len(zh)):
                            if jalgau[4:] == zh[i]:
                                txt += jalgau[4:] + '<zhiktik> '
                                zhf = True
                    if zhf != True:
                        txt = subtxt
                        for i in range(len(t)):
                            if jalgau[3:5] == t[i]:
                                txt += jalgau[3:5] + '<taueldilik> '
                                tf = True
                        if tf:
                            for i in range(len(s)):
                                if jalgau[5:7] == s[i]:
                                    txt += jalgau[5:7] + '<septik> '
                                    sf = True
                            if sf:
                                for i in range(len(zh)):
                                    if jalgau[7:] == zh[i]:
                                        txt += jalgau[7:] + '<zhiktik> '
                                        zhf = True
                    if zhf != True:
                        txt = subtxt
                        for i in range(len(t)):
                            if jalgau[3:6] == t[i]:
                                txt += jalgau[3:6] + '<taueldilik> '
                                tf = True
                        for i in range(len(s)):
                            if jalgau[3:6] == s[i]:
                                txt += jalgau[3:6] + '<septik> '
                                sf = True
                        if sf:
                            for i in range(len(zh)):
                                if jalgau[7:] == zh[i]:
                                    txt += jalgau[7:] + '<zhiktik> '
                                    zhf = True
                        if tf:
                            for i in range(len(s)):
                                if jalgau[6] == s[i]:
                                    txt += jalgau[6] + '<septik> '
                                    sf = True
                            if sf:
                                for i in range(len(zh)):
                                    if jalgau[7:] == zh[i]:
                                        txt += jalgau[7:] + '<zhiktik> '
                                        zhf = True
                    if zhf != True:
                        txt = subtxt
                        for i in range(len(t)):
                            if jalgau[3:7] == t[i]:
                                txt += jalgau[3:7] + '<taueldilik> '
                                tf = True
                        if tf:
                            for i in range(len(s)):
                                if jalgau[7:] == s[i]:
                                    txt += jalgau[7:] + '<septik> '
                                    sf = True
                        if sf != True:
                            for i in range(len(zh)):
                                    if jalgau[7:] == zh[i]:
                                        txt += jalgau[7:] + '<zhiktik> '
                                        zhf = True
            if kf != True:
                txt = ""
                for i in range(len(t)):
                    if jalgau[:4] == t[i]:
                        txt += jalgau[:4] + "<taueldilik> "
                        tf = True
                if tf:
                    for i in range(len(s)):
                        if jalgau[4:7] == s[i]:
                            txt += jalgau[4:7] + '<septik> '
                            sf = True
                    if sf:
                        for i in range(len(zh)):
                            if jalgau[7:] == zh[i]:
                                txt += jalgau[7:] + '<zhiktik> '
                                zhf = True
                    if zhf != True:
                        for i in range(len(zh)):
                            if jalgau[4:] == zh[i]:
                                txt += jalgau[4:] + '<zhiktik> '
                                zhf = True

        elif l == 11:
            if kf != True:
                for i in range(len(k)):
                    if jalgau[:3] == k[i]:
                        txt = jalgau[:3] + "<koptik> "
                        kf = True
                if kf:
                    subtxt = txt
                    for i in range(len(t)):
                        if jalgau[3] == t[i]:
                            txt += jalgau[3] + '<taueldilik> '
                            tf = True
                    if tf:                
                        for i in range(len(s)):
                            if jalgau[4] == s[i]:
                                txt += jalgau[4] + '<septik> '
                                sf = True
                        if sf:
                            for i in range(len(zh)):
                                if jalgau[5:] == zh[i]:
                                    txt += jalgau[5:] + '<zhiktik> '
                                    zhf = True
                    if zhf != True:
                        txt = subtxt
                        for i in range(len(t)):
                            if jalgau[3:5] == t[i]:
                                txt += jalgau[3:5] + '<taueldilik> '
                                tf = True
                        for i in range(len(s)):
                            if jalgau[3:5] == s[i]:
                                txt += jalgau[3:5] + '<taueldilik> '
                                sf = True
                        if tf:
                            for i in range(len(s)):
                                if jalgau[5:8] == s[i]:
                                    txt += jalgau[5:8] + '<septik> '
                                    sf = True
                            if sf:
                                for i in range(len(zh)):
                                    if jalgau[8:] == zh[i]:
                                        txt += jalgau[8:] + '<zhiktik> '
                                        zhf = True
                            if zhf != True:
                                for i in range(len(zh)):
                                    if jalgau[5:] == zh[i]:
                                        txt += jalgau[5:] + '<zhiktik> '
                                        zhf = True
                        if sf:
                            for i in range(len(zh)):
                                if jalgau[5:] == zh[i]:
                                    txt += jalgau[5:] + '<zhiktik> '
                                    zhf = True
                    if zhf != True:
                        txt = subtxt
                        for i in range(len(t)):
                            if jalgau[3:6] == t[i]:
                                txt += jalgau[3:6] + '<taueldilik> '
                                tf = True
                        for i in range(len(s)):
                            if jalgau[3:6] == s[i]:
                                txt += jalgau[3:6] + '<septik> '
                                sf = True
                        if sf:
                            for i in range(len(zh)):
                                if jalgau[6:] == zh[i]:
                                    txt += jalgau[6:] + '<zhiktik> '
                                    zhf = True
                        if tf:
                            for i in range(len(s)):
                                if jalgau[6:8] == s[i]:
                                    txt += jalgau[6:8] + '<septik> '
                                    sf = True
                            if sf:
                                for i in range(len(zh)):
                                    if jalgau[8:] == zh[i]:
                                        txt += jalgau[8:] + '<zhiktik> '
                                        zhf = True                
                    if zhf != True:
                        txt = subtxt
                        for i in range(len(t)):
                            if jalgau[3:7] == t[i]:
                                txt += jalgau[3:7] + '<taueldilik> '
                                tf = True
                        if tf:
                            for i in range(len(s)):
                                if jalgau[7] == s[i]:
                                    txt += jalgau[7] + '<septik> '
                                    sf = True
                            if sf == True:
                                for i in range(len(zh)):
                                    if jalgau[8:] == zh[i]:
                                        txt += jalgau[8:] + '<zhiktik> '
                                        zhf = True

        elif l == 12:
            if kf != True:
                for i in range(len(k)):
                    if jalgau[:3] == k[i]:
                        txt = jalgau[:3] + "<koptik> "
                        kf = True
                if kf:
                    subtxt = txt
                    for i in range(len(t)):
                        if jalgau[3] == t[i]:
                            txt += jalgau[3] + '<taueldilik> '
                            tf = True
                    if tf:                
                        for i in range(len(s)):
                            if jalgau[4:6] == s[i]:
                                txt += jalgau[4:6] + '<septik> '
                                sf = True
                        if sf:
                            for i in range(len(zh)):
                                if jalgau[6:] == zh[i]:
                                    txt += jalgau[6:] + '<zhiktik> '
                                    zhf = True
                    if zhf != True:
                        txt = subtxt
                        tf = False
                        for i in range(len(t)):
                            if jalgau[3:5] == t[i]:
                                txt += jalgau[3:5] + '<taueldilik> '
                                tf = True
                        if tf:
                            for i in range(len(s)):
                                if jalgau[5] == s[i]:
                                    txt += jalgau[5] + '<septik> '
                                    sf = True
                            if sf:
                                for i in range(len(zh)):
                                    if jalgau[6:] == zh[i]:
                                        txt += jalgau[6:] + '<zhiktik> '
                                        zhf = True
                    if zhf != True:
                        txt = subtxt
                        for i in range(len(t)):
                            if jalgau[3:6] == t[i]:
                                txt += jalgau[3:6] + '<taueldilik> '
                                tf = True
                        for i in range(len(s)):
                            if jalgau[3:6] == s[i]:
                                txt += jalgau[3:6] + '<septik> '
                                sf = True
                        if sf:
                            for i in range(len(zh)):
                                if jalgau[6:] == zh[i]:
                                    txt += jalgau[6:] + '<zhiktik> '
                                    zhf = True
                        if tf:
                            for i in range(len(s)):
                                if jalgau[6:9] == s[i]:
                                    txt += jalgau[6:9] + '<septik> '
                                    sf = True
                            if sf:
                                for i in range(len(zh)):
                                    if jalgau[9:] == zh[i]:
                                        txt += jalgau[9:] + '<zhiktik> '
                                        zhf = True
                            if zhf != True:
                                for i in range(len(zh)):
                                    if jalgau[6:] == zh[i]:
                                        txt += jalgau[6:] + '<zhiktik> '
                                        zhf = True
                    if zhf != True:
                        txt = subtxt
                        for i in range(len(t)):
                            if jalgau[3:7] == t[i]:
                                txt += jalgau[3:7] + '<taueldilik> '
                                tf = True
                        if tf:
                            for i in range(len(s)):
                                if jalgau[7:9] == s[i]:
                                    txt += jalgau[7:9] + '<septik> '
                                    sf = True
                            if sf == True:
                                for i in range(len(zh)):
                                    if jalgau[9:] == zh[i]:
                                        txt += jalgau[9:] + '<zhiktik> '
                                        zhf = True

        elif l == 13:
            if kf != True:
                for i in range(len(k)):
                    if jalgau[:3] == k[i]:
                        txt += jalgau[:3] + "<koptik> "
                        kf = True
                if kf:
                    subtxt = txt
                    for i in range(len(t)):
                        if jalgau[3] == t[i]:
                            txt += jalgau[3] + '<taueldilik> '
                            tf = True
                    if tf:                
                        for i in range(len(s)):
                            if jalgau[4:7] == s[i]:
                                txt += jalgau[4:7] + '<septik> '
                                sf = True
                        if sf:
                            for i in range(len(zh)):
                                if jalgau[7:] == zh[i]:
                                    txt += jalgau[:] + '<zhiktik> '
                                    zhf = True
                    if zhf != True:
                        txt = subtxt
                        for i in range(len(t)):
                            if jalgau[3:5] == t[i]:
                                txt += jalgau[3:5] + '<taueldilik> '
                                tf = True
                        if tf:
                            for i in range(len(s)):
                                if jalgau[5:7] == s[i]:
                                    txt += jalgau[5:7] + '<septik> '
                                    sf = True
                            if sf:
                                for i in range(len(zh)):
                                    if jalgau[7:] == zh[i]:
                                        txt += jalgau[7:] + '<zhiktik> '
                                        zhf = True
                    if zhf != True:
                        txt = subtxt
                        for i in range(len(t)):
                            if jalgau[3:6] == t[i]:
                                txt += jalgau[3:6] + '<taueldilik> '
                                tf = True
                        if tf:
                            for i in range(len(s)):
                                if jalgau[6] == s[i]:
                                    txt += jalgau[6] + '<septik> '
                                    sf = True
                            if sf:
                                for i in range(len(zh)):
                                    if jalgau[7:] == zh[i]:
                                        txt += jalgau[7:] + '<zhiktik> '
                                        zhf = True
                    if zhf != True:
                        txt = subtxt
                        for i in range(len(t)):
                            if jalgau[3:7] == t[i]:
                                txt += jalgau[3:7] + '<taueldilik> '
                                tf = True
                        if tf:
                            for i in range(len(s)):
                                if jalgau[7:10] == s[i]:
                                    txt += jalgau[7:10] + '<septik> '
                                    sf = True
                            if sf == True:
                                for i in range(len(zh)):
                                    if jalgau[10:] == zh[i]:
                                        txt += jalgau[10:] + '<zhiktik> '
                                        zhf = True
                            if zhf != True:
                                for i in range(len(zh)):
                                    if jalgau[7:] == zh[i]:
                                        txt += jalgau[7:] + '<zhiktik> '
                                        zhf = True

        elif l == 14:
            pass
        #endregion

    return txt