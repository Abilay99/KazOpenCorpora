import re
import os,glob
papka_korpus = os.path.dirname(__file__)
papka_editedapertium = os.path.join(papka_korpus, "testEditedApertium")
papka_outtexts = os.path.join(papka_korpus, "testouttexts")
from tqdm import tqdm
from time import monotonic, sleep
from datetime import timedelta
files = glob.glob(os.path.join(papka_editedapertium,"*.txt"))
length = len(files)
pbar = tqdm(files)
start_time = monotonic()
for fail in pbar:
    filename = fail[fail.rfind("/")+1:]
    pbar.set_description(f"Жасалуда {str(filename)}")
    with open(fail, 'r', encoding="utf-8") as f:
        inddot = filename.rfind(".")
        f2 = open(os.path.join(papka_outtexts, filename[:inddot]+".gt"), 'w', encoding="utf-8")
        txt = f.read()
        txtmas = re.findall(r"[\w+|\w|\s|(\w\-\w)]+[<]+\w+[>]|[,|\.|\?|!]+[<]+\w+[>]|[«]+[<]+\w+[>]|[»]+[<]+\w+[>]|[\"]+[<]+\w+[>]|[\"]+[<]+\w+[>]|[\']+[<]+\w+[>]|[\']+[<]+\w+[>]|\n|\n+|[ ]+|[\"]+[<]+\w+[>]|.{1}[<]+lquot+[>]|.{1}[<]+rquot+[>]", txt)
        newtext = ""
        for i in txtmas:
            newtext += str(i).replace("^","").replace("<cm>","").replace("<sent>","").replace("<lquot>","").replace("<rquot>","").replace("е<cop>", "")
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
        f2.write(newtext)
        f2.close()
end_time = monotonic()
timedel = end_time - start_time 
print("Аяқталды! Барлығы {0} құжат. Жұмсалған уақыт: {1}".format(length, timedelta(seconds=timedel)))