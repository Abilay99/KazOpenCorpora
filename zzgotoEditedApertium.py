import re, os, glob, collections
papka_korpus = os.path.dirname(__file__)
from tqdm import tqdm
from time import monotonic, sleep
from datetime import timedelta

def sub(newtext):
    newtext = re.sub(r'[.]+([.]|[,]|[!]|[?])+', '. ', newtext)
    newtext = re.sub(r'[,]+([.]|[,]|[!]|[?])+', ', ', newtext)
    newtext = re.sub(r'[?]+([.]|[,]|[!]|[?])+', '? ', newtext)
    newtext = re.sub(r'[!]+([.]|[,]|[!]|[?])+', '! ', newtext)
    newtext = re.sub(r'[.]+', '. ', newtext)
    newtext = re.sub(r'[,]+', ', ', newtext)
    newtext = re.sub(r'[?]+', '? ', newtext)
    newtext = re.sub(r'[!]+', '! ', newtext)
    newtext = re.sub(r'[" "]+', ' ', newtext)
    return newtext

def soilemgebolu(text):
    res = re.split(r"[.]|[?]|[!]", text)
    if res[len(res)-1] == '':
        del res[len(res)-1]
    return res

def sozgebolu(text):
    return re.findall(r"\w+", text)

global_katolog = "/media/gpu2/59f87a06-90bf-49c9-a6c0-34f26ab5287c/SEproject/corporaD/basictexts/" 
podkotologs = glob.glob(global_katolog+"*")
globaltime = 0
globalfiles = 0
for podkotolog in podkotologs:
    outdirectory = str(podkotolog).replace('basictexts', 'EditedApertium')
    apdir = str(podkotolog).replace('basictexts', 'Apertium')
    os.system('mkdir "{0}"'.format(outdirectory))
    utechka = glob.glob(os.path.join(podkotolog, '*.txt'))
    length = len(utechka)
    pbar = tqdm(utechka)
    start_time = monotonic()
    kol = 1
    katologname = str(podkotolog).replace(global_katolog, '')
    for fail in pbar:
        filename = fail[fail.rfind("/")+1:]
        pbar.set_description(f"Жасалуда {katologname}/{str(filename)}")
        np = []
        with open(fail, 'r', encoding="utf-8") as f:
            text = f.read()
            text = sub(text)
            soilemder = soilemgebolu(text)
            try:
                testfile = open(os.path.join(apdir, filename),'r',encoding="utf-8")
            except FileNotFoundError:
                continue
            txttest = str(testfile.read())
            testtxt = re.findall(r"\*\w+\$", txttest)
            testtxt = "".join(testtxt)
            testtxt = re.findall(r"\w+", testtxt)
            for soilem in soilemder:
                sozder = sozgebolu(soilem)
                for i in range(1,len(sozder)):
                    if str(sozder[i][0]).isupper() and sozder[i] in testtxt:
                        np.extend(sozder[i])
            newfile = open(os.path.join(outdirectory, filename), 'w', encoding="utf-8")
            np = collections.Counter(np)
            for w in np:
                txttest = re.sub(r'\*'+w, w+'<np>', txttest)
            newfile.write(txttest)
            testfile.close()
            newfile.close()
        if(length == kol):
            end_time = monotonic()
            timedel = end_time - start_time 
            globaltime +=  timedel
            pbar.set_description(f"{katologname} ішкі папкасы aяқталды! Барлығы {length} құжат. Жұмсалған уақыт: {timedelta(seconds=timedel)}")
        kol += 1
    globalfiles += length

print("Аяқталды! Барлығы {0} құжат. Жұмсалған уақыт: {1}".format(globalfiles, timedelta(seconds=globaltime)))