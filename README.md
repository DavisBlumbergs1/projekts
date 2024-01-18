# projekts

#Projekta mērķis
Sākotnējais programmas mērķis bija pavisam savādāks 
1. programmas iterācijā bija domāts savākt datus no “nodarbibas.rtu.lv” un to ievadīt Excel(bija pārāk grūti ar WebScraping).

2. iterācijā mērķis bija darīt to pašu bet ar “screenshot” un tad bildi aizsūtīt man pašam uz e-mail (nepietika laika, varbūt nākonē bija divi plāni 1. izmantot(simple mail transfer protocol) 2. ar webscraping atrast vienreizējo e-mail adressi un aizsūtīt no tās uz manu e-mail(“✉ Guerrilla Mail - Disposable Temporary E-Mail Address ”)).

3. Iterācija izdevās. Sākotnējais mērķis tād pats kā 2, iterācijai bet neko nedara ar bildi. Pēc tam to var izmantot kā grib.

Es šo progrmmu izveidoju divu iemslu dēļ. Pirmais mērķis bija iemācīties par WebScraping jo nebija nekāds mājas darbs par šo tēmu tāpēc gribēju ar to iepazīties. Otrais mērķis bija man atvieglot paskatīites Lekciju srakstu es pats vienmēr izmantoju “nodarbibas.rtu.lv” bet tas sarežģīj procesu, jo katru reizi nepieciešams veikt vairākas darbības bezjēdzīgi ar šo programmu es spēju katru mēnesi iegūt pilnu Lekciju srakstu un tad to aizsūīt uz savu mobīlo ierīči kur to var viegli apskatī kā bildi.


Izmantotās Bibliotēkas – selenium,time, PTL, io.

Kā izmantot Programmu -  Programu izmanto palaižot “source.py” izmantojot “Visual Baisc” vai citveidīgu programmu. Programa tad palaidīsies, atvērs Chrome lapu kur veiks darbības lai izveidotu bildi kas ir saglabāta šajā Folderī ar nosaukumu “stitched_screenshot.png” 

Programa var nestrāāt ja lēns internets vai dators, to var risināt atverot programmu un noaimnot mainīgo emergency_pause = 0 uz lielāku skaitli.

Kā strādā programa - 

1. import visas bilbotiekas.
2. sagatavo programu webscraping.
3. Programa atver Chrome mājaslapu “nodarbibas.rtu.lv”.
4. Atrod lapā “Studijju Programmu” izvelni un izvēlās “Automātika un Datorthenika”
5. Kad ir izvēlēta Studiju Programma parāās divi lodziņi “Kurss” un “Grupa”
6.Atrod lapā “Kurss” izvelni un  nospiež “1” lai izvēlētos “Pirmo Kursu”. Programma nospiež “Enter” lai saglabātu savu izvēli.
7.To pašu izdara ar “Grupu” un izvēlas “10”
10. Parādāš jauns lodzīņš ar Lekcijusarakstu.
11. Progrmma atrod šī lodziņa atiecīgo vietu mājaslapā
12. Izmēra šī lodziņa augstumu un platumu.
13.Veic pirmo “Screenshot” tad to sagriež pareizajā lielumā un ievieto mainīgajā stiched_image
14. programma patin uz leju un veic velvienu “Screenshot” ko pievieno mainīgajam stiched_image. Šis atkārotjas līz stiched image ir pilns.
15. stiched_image saglabā un programma aizverās.
