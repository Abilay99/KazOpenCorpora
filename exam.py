import os, glob, re
from tqdm import tqdm
from time import monotonic
from datetime import timedelta

corpus_mynzhan_corp = "/media/gpu2/59f87a06-90bf-49c9-a6c0-34f26ab5287c/Abilay-Mynzhan/MynzhanCorp/corpus"
contentcorpus_mynzhan_corp = "/media/gpu2/59f87a06-90bf-49c9-a6c0-34f26ab5287c/Abilay-Mynzhan/MynzhanCorp/contentcorpus"
def forwrite(path):
    for pathtext in path:
        print(pathtext)
        utechka = glob.glob(pathtext+"/*")
        pbar = tqdm(utechka)
        start_time = monotonic()
        for files in pbar:
            filename = files[files.rfind('/')+1:]
            pbar.set_description("Жасалуда %s" % str(filename))
            with open(files, 'r', encoding="utf-8") as f:
                text = f.readlines()
                length = len(text)
                tekseru = True
                for i in range(length-1, 0, -1):
                    if re.match(r"https://", text[i]):
                        with open(pathtext+'-new/' + filename + '.url', 'w', encoding="utf-8") as f_url:
                            f_url.write(text[i])
                        del text[i]
                        tekseru = False
                        break
                if tekseru:
                    with open(pathtext+'-new/' + filename + '.url', 'w', encoding="utf-8") as f_url:
                        pass
                with open(pathtext+'-new/' + filename + '.txt', 'w', encoding="utf-8") as f_out:
                    f_out.writelines(text)
                
        end_time = monotonic()
        print("Аяқталды! Барлығы {0} құжат. Жұмсалған уақыт: {1}".format(len(utechka), timedelta(seconds=end_time - start_time)))

forwrite([corpus_mynzhan_corp, contentcorpus_mynzhan_corp])
