import re, os, glob
papka_korpus = os.path.dirname(__file__)
papka_editedapertium = os.path.join(papka_korpus, "testEditedApertium")
papka_apertium = os.path.join(papka_korpus, "testApertium")
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
global_katolog = "/media/gpu2/59f87a06-90bf-49c9-a6c0-34f26ab5287c/SEproject/corporaD/testbasictexts/" 
files = glob.glob(global_katolog+"*.txt")
length = len(files)
pbar = tqdm(files)
start_time = monotonic()
for fail in pbar:
    filename = fail[fail.rfind("/")+1:]
    pbar.set_description(f"Жасалуда {str(filename)}")
    np = []
    unknown = []
    with open(fail, 'r', encoding="utf-8") as f:
        text = f.read()
        text = sub(text)
        soilemder = soilemgebolu(text)
        try:
            testfile = open(os.path.join(papka_apertium, filename),'r',encoding="utf-8")
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
                    np.append(str(sozder[i]))
                elif sozder[i] in testtxt:
                    unknown.append(str(sozder[i]))
        newfile = open(os.path.join(papka_editedapertium, filename), 'w', encoding="utf-8")
        npf = open(os.path.join(papka_editedapertium+'/np', filename), 'w', encoding="utf-8")
        unknownf = open(os.path.join(papka_editedapertium+'/unknown', filename), 'w', encoding="utf-8")
        np = set(np)
        for w in np:
            txttest = re.sub(r'\*'+w, w+'<np>', txttest)
            npf.write(w+'\n')
        unknown = set(unknown)
        for w in unknown:
            txttest = re.sub(r'\*'+w, w+'<unknown>', txttest)
            unknownf.write(w+'\n')
        newfile.write(txttest)
        testfile.close()
        newfile.close()
        unknownf.close()
        npf.close()
end_time = monotonic()
timedel = end_time - start_time 

    
print("Аяқталды! Барлығы {0} құжат. Жұмсалған уақыт: {1}".format(length, timedelta(seconds=timedel)))