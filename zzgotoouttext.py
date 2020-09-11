import re
import os,glob
papka_korpus = os.path.dirname(__file__)
from tqdm import tqdm
from time import monotonic, sleep
from datetime import timedelta

global_katolog = "/media/gpu2/59f87a06-90bf-49c9-a6c0-34f26ab5287c/SEproject/corporaD/EditedApertium/" 
podkotologs = glob.glob(global_katolog+"*")
globaltime = 0
globalfiles = 0
for podkotolog in podkotologs:
    outdirectory = str(podkotolog).replace('EditedApertium', 'outtexts')
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
        with open(fail, 'r', encoding="utf-8") as f:
            inddot = filename.rfind(".")
            f2 = open(os.path.join(outdirectory, filename[:inddot+1]+".gt"), 'w', encoding="utf-8")
            txt = f.read()
            txtmas = re.findall(r"\*\w+|[\w+|\w|\s|(\w\-\w)]+[<]+\w+[>]|[,|\.|\?|!]+[<]+\w+[>]|[«]+[<]+\w+[>]|[»]+[<]+\w+[>]|[\"]+[<]+\w+[>]|[\"]+[<]+\w+[>]|[\']+[<]+\w+[>]|[\']+[<]+\w+[>]|\n|\n+|[ ]+|[\"]+[<]+\w+[>]|.{1}[<]+lquot+[>]|.{1}[<]+rquot+[>]", txt)
            newtext = ""
            for i in txtmas:
                newtext += str(i).replace("^","").replace("<cm>","").replace("<sent>","").replace("<lquot>","").replace("<rquot>","").replace(" е<cop>", "")
            newtext = re.sub(r'[.]+([.]|[,]|[!]|[?])+', '. ', newtext)
            newtext = re.sub(r'[,]+([.]|[,]|[!]|[?])+', ', ', newtext)
            newtext = re.sub(r'[?]+([.]|[,]|[!]|[?])+', '? ', newtext)
            newtext = re.sub(r'[!]+([.]|[,]|[!]|[?])+', '! ', newtext)
            newtext = re.sub(r'[.]+', '. ', newtext)
            newtext = re.sub(r'[,]+', ', ', newtext)
            newtext = re.sub(r'[?]+', '? ', newtext)
            newtext = re.sub(r'[!]+', '! ', newtext)
            newtext = re.sub(r'[" "]+', ' ', newtext)
            f2.write(newtext)
            f2.close()
        if(length == kol):
            end_time = monotonic()
            timedel = end_time - start_time 
            globaltime +=  timedel
            pbar.set_description(f"{katologname} ішкі папкасы aяқталды! Барлығы {length} құжат. Жұмсалған уақыт: {timedelta(seconds=timedel)}")
        kol += 1
    globalfiles += length

print("Аяқталды! Барлығы {0} құжат. Жұмсалған уақыт: {1}".format(globalfiles, timedelta(seconds=globaltime)))