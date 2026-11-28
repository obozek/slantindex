# Zdroje a ověření importu

## ČRo Plus

| Zdroj | Co převzít | Omezení |
|---|---|---|
| [Program ČRo](https://program.rozhlas.cz/program/html) | Stanice, den, čas, název a anotace jednotlivých vysílání. | Plán může předcházet programové změně. Obecný několikahodinový blok nedokládá hosta po celou svou délku. Chybějící den je mezera v datech. |
| [API mujRozhlas](https://api.mujrozhlas.cz/episodes) | Stránkované epizody, ID dílu a pořadu, popis, časy a dostupná metadata audia. | Pole `relationships.stations` může odkazovat na stanice pořadu. Každé konkrétní odvysílání musí doložit program či záznam. Stopáž archivní verze se může lišit od vysílání. |
| Stránka dílu a případně záznam vysílání | Role, jména, instituce, údaj o repríze, skutečná délka nebo hranice úseku. | Podpis může označovat redaktora webu. Samotná shoda jména v titulku průkaznou účast nezakládá. |

## Import a dohledatelnost

1. Příkaz `import --station cro-plus --from YYYY-MM-DD --to YYYY-MM-DD` zahrnuje oba krajní dny; první implementace načítá ČRo Plus. Stav importu a chyby se evidují po stanici a dni. Výpadek jednoho zdroje neblokuje ostatní. Opakované načtení posledních sedmi dnů zachytí změny. Starší interval lze přehrát samostatně.
2. Páruj přednostně přes ID epizody či kanonický odkaz. Náhradní vazbu podle pořadu, času, délky a anotace dovol jen při jediném přesvědčivém kandidátovi. Reprízy starších pořadů hledej i před importovaným obdobím. Sporné shody, odlišné sestřihy a neznámý počátek historie mají zvláštní stav.
3. Každé různé tělo odpovědi ulož soukromě podle hashe spolu s URL, časem, HTTP stavem, verzí parseru a dostupnými hlavičkami pro podmíněné načtení. Souběh omez podle hostitele, respektuj pravidla zdroje, `Retry-After` a odklad opakovaných pokusů. Před hromadným importem ověř přístupové a užívací podmínky. Ve veřejném výstupu používej vlastní strukturovaná fakta, nezbytné doklady a odkazy.
4. Parser čte strukturovaná pole a vzory typu „moderuje“, „hostem je“, „debatovali“. U volného textu vytvoří kandidáta pravidlo nebo editor. Volitelný jazykový model může návrh doplnit o výřez dokladu. Ukládej model/verzi, verzi pokynu, vstupní hash a jistotu. Návrh názorového profilu připraví editor z dohledaných primárních zdrojů (program, podepsaný text, přímý veřejný výrok); u stran lze importovat datovanou expertní studii. Případný model pouze předvyplní návrh. Nejasné extrakce a všechna hodnocení před publikací schvaluje editor. Pokyny a validační vzorek verzuj před zapnutím modelu. Z první verze nevzniká závislost na placeném API.
5. Ověřuj import podle stanice **i žánru**. Počítej získané stanico-dny, pokryté sekundy vůči době dostupného programu, míru spárování dílů, úplnost obsazení a podíl času s doloženou/odhadnutou délkou. Proudové vysílání vykazuj zvlášť. Testy přehrávají uložené vstupy; náhlý pokles pokrytí proti poslednímu srovnatelnému období vyvolá kontrolu před vydáním.

## Ověřené případy a hranice pilotu

- *Pro a proti*, daň ze slazených nápojů. Stránka dokládá účast obou diskutujících a výslovně připomíná starší premiéru. Import získá hosty z úvodu a druhé vysílání připojí ke stejnému obsahu. [Díl na ČRo Plus](https://plus.rozhlas.cz/dan-ze-slazenych-napoju-snizi-obezitu-soudi-ekonom-napoje-za-nemuzou-mini-9324188)
- *Život k nezaplacení*, 25. 11. 2026. V úvodu je Daniel Prokop uveden jako účastník, v podpisu jsou tři položky. Text dokládá účast, podpis autorství. U sdíleného pořadu je pro zahrnutí do Plusu potřeba doložit konkrétní vysílání v programu Plusu. [Díl na Radiožurnálu](https://radiozurnal.rozhlas.cz/danime-praci-ale-majetek-temer-vubec-cesko-je-v-tom-vyjimecne-rika-sociolog-9658893)
- První ukázka ověří jeden pořad za sedm dní. Pro měření pokrytí celého Plusu přidej ostatní pořady z posledního uzavřeného týdne a před doplněním historie také sedm dní na začátku dvouletého období. Ulož vstupy nebo povolené minimalizované vzorky, označ role a časové úseky v kontrolním vzorku a změř přesnost i podíl nalezených vystoupení. U délek porovnej zdroj odhadu a absolutní chybu proti ručně ověřeným minutám. Uveď velikost vzorku a výsledky po žánrech. **Dvoutýdenní měření zatím neproběhlo.**

## Až přibude druhá stanice

U další stanice ČRo nejprve vyzkoušej, zda současnému importu stačí předat jinou stanici. U jiného provozovatele nejprve spáruj jeden skutečný díl s odvysíláním. Pokud má zdroj jiný formát, přidej malý modul, který naplní stejné záznamy ve SQLite. Teprve z obou fungujících importů odvoď společné rozhraní. Na stejném období ověř, že přidání stanice nemění minuty ani počet dílů Plusu.

**Kandidát na druhou stanici: Radio Prostor.** Veřejný program uvádí pořady, časy a u části bloků moderátory. Tříhodinový blok s hosty vyžaduje další zdroj pro délku samotného rozhovoru. Dostupnost dvouleté programové historie ani přesnost párování s publikovanými rozhovory zatím nejsou ověřené. [Program Radia Prostor](https://www.radioprostor.cz/program)
