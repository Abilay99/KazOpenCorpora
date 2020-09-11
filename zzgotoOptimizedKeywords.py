import re
import os, glob
papka_korpus = os.path.dirname(__file__)
f = open(os.path.join(papka_korpus, "keywords.txt"), 'r', encoding="utf-8")

keywords = f.read()
keywords = re.split(r"\.\n", keywords)
if keywords[len(keywords)-1] == '':
    del keywords[len(keywords)-1]
title_keywords = []

f.close()

for i in range(len(keywords)):
    title_keywords.extend(re.findall(r"%.+?%", keywords[i]))
    keywords[i] = re.sub(r"%.+?% ", '', keywords[i])
    keywords[i] = re.split(r" \| ", keywords[i])
    title_keywords[i] = re.sub(r"%", '', title_keywords[i])

ni = len(keywords)
ii = 0
while ii < ni:
    k = 15
    onekeywords = keywords[ii][:15]
    twokeywords = keywords[ii][15:]
    newkeywords = []
    twokeywordsstr = " ".join(twokeywords)
    nj = len(onekeywords)
    jj = 0
    while jj < nj:
        if onekeywords[jj] in twokeywordsstr:
            del onekeywords[jj]
            k -= 1
            nj -= 1
            jj -= 1
        jj += 1
    newkeywords.extend(onekeywords)
    newkeywords.extend(twokeywords)
    keywords[ii] = newkeywords
    ii += 1
for i in range(len(title_keywords)):
    with open(os.path.join(papka_korpus, "OptimizedKeywords\\"+title_keywords[i]+".txt"), 'w', encoding="utf-8") as fw:
        for j in range(len(keywords[i])):
            fw.write(str(keywords[i][j])+"\n")