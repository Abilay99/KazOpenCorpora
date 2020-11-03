import os, glob

papka_korpus = os.path.dirname(__file__)
papka_apertium = os.path.join(papka_korpus, "testApertium")
from tqdm import tqdm
from time import monotonic, sleep
from datetime import timedelta
global_katolog = "/media/gpu2/59f87a06-90bf-49c9-a6c0-34f26ab5287c/SEproject/corporaD/testbasictexts/" 
files = glob.glob(global_katolog+"*.txt")
f = open("/media/gpu2/59f87a06-90bf-49c9-a6c0-34f26ab5287c/SEproject/corporaD/errors/error.log", 'a+', encoding="utf-8")
length = len(files)
pbar = tqdm(files)
start_time = monotonic()
for fail in pbar:
    filename = fail[fail.rfind("/")+1:]
    pbar.set_description(f"Жасалуда {str(filename)}")
    try:
        os.system('''cd $HOME/sources/apertium-kaz-rus\ncat "{0}" | apertium -n -d. kaz-rus-tagger > "{1}"'''.format(fail, os.path.join(papka_apertium, filename)))
    except:
        f.write(fail+"\n")
end_time = monotonic()
timedel = end_time - start_time 
print("Аяқталды! Барлығы {0} құжат. Жұмсалған уақыт: {1}".format(length, timedelta(seconds=timedel)))
f.close()