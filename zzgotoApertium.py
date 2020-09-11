import os, glob

papka_korpus = os.path.dirname(__file__)
papka_apertium = os.path.join(papka_korpus,"Apertium")
from tqdm import tqdm
from time import monotonic, sleep
from datetime import timedelta
global_katolog = "/media/gpu2/59f87a06-90bf-49c9-a6c0-34f26ab5287c/SEproject/corporaD/basictexts/" 
podkotologs = glob.glob(global_katolog+"*")
f = open("/media/gpu2/59f87a06-90bf-49c9-a6c0-34f26ab5287c/SEproject/corporaD/errors/error.log", 'a+', encoding="utf-8")
globaltime = 0
globalfiles = 0
for podkotolog in podkotologs:
    outdirectory = str(podkotolog).replace('basictexts', 'Apertium')
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
        try:
            os.system('''cd /media/gpu2/59f87a06-90bf-49c9-a6c0-34f26ab5287c/SEproject/Source/apertium-kaz\ncat "{0}" | apertium -n -d. kaz-tagger > "{1}"'''.format(fail, os.path.join(outdirectory, filename)))
        except:
            f.write(fail+"\n")
        if(length == kol):
            end_time = monotonic()
            timedel = end_time - start_time 
            globaltime +=  timedel
            pbar.set_description(f"{katologname} ішкі папкасы aяқталды! Барлығы {length} құжат. Жұмсалған уақыт: {timedelta(seconds=timedel)}")
        kol += 1
    globalfiles += length

print("Аяқталды! Барлығы {0} құжат. Жұмсалған уақыт: {1}".format(globalfiles, timedelta(seconds=globaltime)))
f.close()
