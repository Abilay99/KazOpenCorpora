from CorporaDB import corporaDB
import os, re,
papka_korpus = os.path.dirname(__file__)
ob = corporaDB()

lencorp = int(ob.Count_corpora()[0]['sany'])
lengen = int(ob.Count_genres()[0]['sany'])
print(lencorp, lengen)
with open("analyze.txt", 'w', encoding="utf-8") as f:
    f.write("Mikrotema atauy".ljust(30,' ')+"Mikrotemadagy jalpy sozder sany".ljust(40,' ')+"Mikrotemadagy jalpy matinder sany\r\n")
    alllen = 0
    for i in range(1, lengen+1):
        SozderSanyBirMikrotemada = 0
        results = ob.SelectsForAnalyze(gid = i)
        MatinSanyBirMikrotemada = len(results)
        MikrotemaAtauy = str(results[0]['kz'])
        for j in range(MatinSanyBirMikrotemada):
            txt = str(results[j]['text'])
            words = re.findall(r"\w+", txt)
            SozderSanyBirMikrotemada += len(words)
        alllen += SozderSanyBirMikrotemada
        f.write(str(MikrotemaAtauy).ljust(30,' ')+str(SozderSanyBirMikrotemada).ljust(40,' ')+str(MatinSanyBirMikrotemada)+"\r\n")
    f.write("\nKorpustagy jalpy matinder sany: "+str(lencorp)+"\tKorpustagy jalpy mikrotemalar sany: "+str(lengen)+"\tKorpustagy jalpy sozder sany: "+str(alllen))