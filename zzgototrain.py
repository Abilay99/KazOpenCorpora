import re
import os,glob
papka_korpus = os.path.dirname(__file__)
from tqdm import tqdm
from time import monotonic, sleep
from datetime import timedelta
def sozgebolu(text):
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
f = open(os.path.join(os.path.dirname(__file__), "Global/MorfAnaliz/stopw.txt"), 'r', encoding="utf-8")
stxt = list(f.readlines())
for i in range(len(stxt)):
    l = "" 
    for j in range(len(stxt[i])):
        if stxt[i][j] != '\n':
            l += stxt[i][j]
    stxt[i] = l

global_katolog = "/media/gpu2/59f87a06-90bf-49c9-a6c0-34f26ab5287c/SEproject/corporaD/outtexts/" 
podkotologs = glob.glob(global_katolog+"*")
globaltime = 0
globalfiles = 0
for podkotolog in podkotologs:
    outdirectory = str(podkotolog).replace('outtexts', 'train')
    os.system('mkdir "{0}"'.format(outdirectory))
    utechka = glob.glob(os.path.join(podkotolog, '*.gt'))
    length = len(utechka)
    pbar = tqdm(utechka)
    start_time = monotonic()
    kol = 1
    katologname = str(podkotolog).replace(global_katolog, '')
    for fail in pbar:
        filename = fail[fail.rfind("/")+1:]
        pbar.set_description(f"Жасалуда {katologname}/{str(filename)}")
        with open(fail, 'r', encoding="utf-8") as f:
            inddot = filename.rfind(".")
            f2 = open(os.path.join(outdirectory, filename[:inddot+1]+"tr"), 'w', encoding="utf-8")
            txt = f.read()
            soz = sozgebolu(txt)
            n = len(soz)
            i = 0
            while i < n:
                for j in stxt:
                    if soz[i] == j:
                        soz.remove(j)
                        n -= 1
                        i -= 1
                        break
                i += 1
            sozd = " ".join(soz)
            f2.write(str(sozd))
            f2.close()
        if(length == kol):
            end_time = monotonic()
            timedel = end_time - start_time 
            globaltime +=  timedel
            pbar.set_description(f"{katologname} ішкі папкасы aяқталды! Барлығы {length} құжат. Жұмсалған уақыт: {timedelta(seconds=timedel)}")
        kol += 1
    globalfiles += length

print("Аяқталды! Барлығы {0} құжат. Жұмсалған уақыт: {1}".format(globalfiles, timedelta(seconds=globaltime)))