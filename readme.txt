Global --- negizgi tf-idf, bigram esepteushi bagdarlamalar jane morfanaliz(tolyq emes)
basictexts --- munda tekstter qory saqtalgan faildar iagny negizgi eshqandai analizsiz negizgi tekstter
Apertium --- munda "basictexts"tegi faildar Apertium komegimen analizdengen faildar
EditedApertium --- munda "Apertium"dagy faiyldar zzgotoEditedApertium.py komegimen analizdengen faildar
outtexts --- munda "EditedApertium"dagy faiyldar zzgotoouttext.py komegimen analizdengen faildar
train --- munda "outtexts"tagy faiyldar zzgototrain.py komegimen analizdengen faildar
Abstracts --- matinderdegi manyzdy soilemder

----------------------------------------------------------------------------------------------------

* - oryndaluy manyzdy janede 1,2,... rettiligi saqtalu qajet
* 1. zzgotoEditedApertium.py --- bul Apertiumdagy analizdengen teksterdegi analizdenbi qalgan sozder iagni zhalqy esimderdi tauyp olardy <np> tegin qosyp qaita saqtaidy. (Eskertu) interpretaciia jasaudan aldyn "Apertium" papkasyna nazar audarynyz onda faildar bar nemese joqtygyn tekseriniz eger onda faildar bolmasa onda Apertium(https://github.com/apertium) komegimen "basictexts" papkasyndagy faildardy analiz jasap olardy Apertium papkasyna zhukteniz.
* 2. zzgotoouttext.py --- bul EditedApertium papkasyndagy faildardagy tekstterdi algashqy tegimen "outtexts" papkasyna saqtaidy(mysaly: кітап<n> қызыл<adj> t.s.s).
* 3. zzgototrain.py --- bul "outtexts" papkasyndagy faildardagy tekstterdi tegtersiz jane bas arippen jazylgan sozderdi kishi ariptege auystyryp "train" papkasyna saqtaidy (bul bigramdyq kilttik sozderdi esepteu kezinde manyzy zor).
* 4. zzgotoexcel.py --- jogary koeficientti 15 bir sozdik (n|np) kilttik sozder jane jogary koeficientti 15 eki sozdik (adj&n|n&n|n&v|np&n|np&np|num&Uaqytataulary) kilttik sozderdi keywords.xls failyna saqtaidy
5. zzgotoexcel_tolyq.py --- manyzdy emes munda tolyq tekstegi kilttik sozder boluy mumkin sozder tizimin keywords_tolyq.xls failyna saqtaidy.
* 6. zzgotokeywordsplaintext.py --- bul keywords.xls failyndagy malimetterdi keywords.txt failyna saqtaidy.  
* 7. zzgotoAbstracts.py --- bul matinnin magynasyn tabuga komektesedi bukil kilttik sozderdin matindegi soilemderin AllSentenceFromKeyWords ishki papkasyna saqtaidy
* 8. zzgotoAbstracts2.py --- bul matinnin magynasyn tabuga komektesedi optimizatsialangan kilttik sozder matindegi soilemderde 2 nemese odan kop kezdesse gana sol soilemdi AllSentenceFromKeyWords2 ishki papkasyna saqtaidy.
* 9. zzgotoOptimizedKeywords.py --- bul kilttik sozderdi optimizatsialauga komektesedi iagni biz algashqyda 15 bir sozden jane 15 eki sozden quralgan kilttik sozderdi algan bolsaq endi sol bir sozdiktegi kilttik sozder eki sozden quralgan kilttik sozderde kezdesse olardy joiyp tastaimyzda ony OptimizedKeywords papkasyna saqtaidy.