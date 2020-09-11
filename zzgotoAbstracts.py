import os, glob, sys
from tqdm import tqdm
papka_korpus = os.path.dirname(__file__)
papka_abstracts = os.path.join(papka_korpus, "Abstracts")
from Global import summarizer
from time import monotonic
from datetime import timedelta

utechka = glob.glob(os.path.join(papka_korpus,"basictexts/*.txt")
pbar = tqdm(utechka)
start_time = monotonic()
for file in pbar:
    filenandext = file[file.rfind("/")+1:]
    pbar.set_description("Жасалуда %s" % str(filenandext))
    
    with open(file, 'r', encoding="utf-8") as f_in, open(os.path.join(papka_abstracts, filenandext), 'w', encoding="utf-8") as f_out:
        text = f_in.read()
        abstract = summarizer.summarize(text, words=200, ratio = 0.3, language="kazakh")
        f_out.write(abstract)
end_time = monotonic()
print("Аяқталды! Барлығы {0} құжат. Жұмсалған уақыт: {1}".format(len(utechka), timedelta(seconds=end_time - start_time))) 
        
                

                    


                    
                    