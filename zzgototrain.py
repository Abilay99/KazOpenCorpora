import re
import os,glob
papka_korpus = os.path.dirname(__file__)
papka_outtexts = os.path.join(papka_korpus, "testouttexts")
papka_train = os.path.join(papka_korpus, "testtrain")
from tqdm import tqdm
from time import monotonic, sleep
from datetime import timedelta
def sozgebolu(text):
    sozder = re.split(r'[<]+\w+[>]+', text)
    for i in range(len(sozder)):
        sozder[i] = str(sozder[i]).lower()
        new = ""
        for j in sozder[i]:
            if j in "abcdefghigklmnopqrstuvwxyzаәбвгғдеёжзийкқлмнңоөпрстуұүфхһцчшщьыъіэюя1234567890- ":
                new += j
        sozder[i] = new
    if sozder[len(sozder)-1] == '':
        del sozder[len(sozder)-1]
    return sozder
f = open(os.path.join(os.path.dirname(__file__), "Global/MorfAnaliz/stopw.txt"), 'r', encoding="utf-8")
stxt = list(f.readlines())
for i in range(len(stxt)):
    l = "" 
    for j in range(len(stxt[i])):
        if stxt[i][j] != '\n':
            l += stxt[i][j]
    stxt[i] = l

files = glob.glob(os.path.join(papka_outtexts, "*.gt"))
length = len(files)
pbar = tqdm(files)
start_time = monotonic()
for fail in pbar:
    filename = fail[fail.rfind("/")+1:]
    pbar.set_description(f"Жасалуда {str(filename)}")
    with open(fail, 'r', encoding="utf-8") as f:
        inddot = filename.rfind(".")
        f2 = open(os.path.join(papka_train, filename[:inddot]+".tr"), 'w', encoding="utf-8")
        txt = f.read()
        soz = sozgebolu(txt)
        n = len(soz)
        i = 0
        while i < n:
            for j in stxt:
                if soz[i] == j:
                    soz.remove(j)
                    n -= 1
                    i -= 0 if i == 0 else 1
                    break
            i += 1
        sozd = " ".join(soz)
        f2.write(str(sozd))
        f2.close()
end_time = monotonic()
timedel = end_time - start_time 

print("Аяқталды! Барлығы {0} құжат. Жұмсалған уақыт: {1}".format(length, timedelta(seconds=timedel)))