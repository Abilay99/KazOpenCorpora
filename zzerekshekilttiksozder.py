import os
import re
papka_korpus = os.path.dirname(__file__)
f = open(os.path.join(os.path.join(papka_korpus, "testbasictexts"), "Elbasy kitaptary.txt"), 'r', encoding="utf-8")
txt = f.read()

text = re.findall(r"[«]+.+?[»]|[\']+.+[\']|[\"]+.+[\"]|[“]+.+[”]", txt)
for i in range(len(text)):
    text[i] = re.sub(r"[«»]|[\']|[\"]|[“”]","", text[i])
for i in range(len(text)):
    text[i] = re.sub(r"^\W+","", text[i])
new = []
for i in text:
    kol = i.count(r" ")
    if kol <= 4 and kol > 1:
        new.append(i)
print(new)