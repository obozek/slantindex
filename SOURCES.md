# Zdroje a ověření importu

| Zdroj | Co převzít | Omezení |
|---|---|---|
| [Program ČRo](https://program.rozhlas.cz/program/html) | Stanice, den, čas, název a anotace jednotlivých vysílání. | Plán může předcházet programové změně. Obecný několikahodinový blok nedokládá hosta po celou svou délku. Chybějící den je mezera v datech. |
| [API mujRozhlas](https://api.mujrozhlas.cz/episodes) | Stránkované epizody, ID dílu a pořadu, popis, časy a dostupná metadata audia. | Pole `relationships.stations` může odkazovat na stanice pořadu. Každé konkrétní odvysílání musí doložit program či záznam. Stopáž archivní verze se může lišit od vysílání. |
| Stránka dílu a případně záznam vysílání | Role, jména, instituce, údaj o repríze, skutečná délka nebo hranice úseku. | Podpis může označovat redaktora webu. Samotná shoda jména v titulku průkaznou účast nezakládá. |

## Import a dohledatelnost

1. Příkaz `import --from YYYY-MM-DD --to YYYY-MM-DD [--station ID]` zahrnuje oba krajní dny a výchozí výběr všech stanic. Uloží seznam stanic platný pro dané období. Vede checkpoint po stanici a dni. Opakované načtení posledních sedmi dnů zachytí změny. Starší interval lze přehrát samostatně.
2. Páruj přednostně přes ID epizody či kanonický odkaz. Náhradní vazbu podle pořadu, času, délky a anotace dovol jen při jediném přesvědčivém kandidátovi. Reprízy starších pořadů hledej i před importovaným obdobím. Sporné shody, odlišné sestřihy a neznámý počátek historie mají zvláštní stav.
3. Každé různé tělo odpovědi ulož soukromě podle hashe spolu s URL, časem, HTTP stavem, verzí parseru a dostupnými hlavičkami pro podmíněné načtení. Souběh omez podle hostitele, respektuj pravidla zdroje, `Retry-After` a odklad opakovaných pokusů. Před hromadným importem ověř přístupové a užívací podmínky. Ve veřejném výstupu používej vlastní strukturovaná fakta, nezbytné doklady a odkazy.
4. Parser čte strukturovaná pole a vzory typu „moderuje“, „hostem je“, „debatovali“. U volného textu vytvoří kandidáta pravidlo nebo editor. Volitelný jazykový model může návrh doplnit o výřez dokladu. Ukládej model/verzi, verzi pokynu, vstupní hash a jistotu. Návrh názorového profilu připraví editor z dohledaných primárních zdrojů (program, podepsaný text, přímý veřejný výrok); u stran lze importovat datovanou expertní studii. Případný model pouze předvyplní návrh. Nejasné extrakce a všechna hodnocení před publikací schvaluje editor. Pokyny a validační vzorek verzuj před zapnutím modelu. Z první verze nevzniká závislost na placeném API.
5. Ověřuj import podle stanice **i žánru**. Počítej získané stanico-dny, pokryté sekundy vůči době dostupného programu, míru spárování dílů, úplnost obsazení a podíl času s doloženou/odhadnutou délkou. Proudové vysílání vykazuj zvlášť. Testy přehrávají uložené vstupy; náhlý pokles pokrytí proti poslednímu srovnatelnému období vyvolá kontrolu před vydáním.

## Ověřené případy a hranice pilotu

- *Pro a proti*, daň ze slazených nápojů. Stránka dokládá účast obou diskutujících a výslovně připomíná starší premiéru. Import získá hosty z úvodu a druhé vysílání připojí ke stejnému obsahu. [Díl na ČRo Plus](https://plus.rozhlas.cz/dan-ze-slazenych-napoju-snizi-obezitu-soudi-ekonom-napoje-za-nemuzou-mini-9324188)
- *Život k nezaplacení*, 25. 11. 2026. V úvodu je Daniel Prokop uveden jako účastník, v podpisu jsou tři položky. Text je jeden doklad jeho účasti, podpis samostatný doklad autorství. [Díl na Radiožurnálu](https://radiozurnal.rozhlas.cz/danime-praci-ale-majetek-temer-vubec-cesko-je-v-tom-vyjimecne-rika-sociolog-9658893)
- Pilot má pokrýt sedm dní na začátku dvouletého období a posledních sedm uzavřených dní na všech stanicích. Ulož vstupy nebo povolené minimalizované vzorky, označ role a časové úseky v kontrolním vzorku a změř přesnost i podíl nalezených vystoupení. U délek porovnej zdroj odhadu a absolutní chybu proti ručně ověřeným minutám. Uveď velikost vzorku a výsledky po stanicích a žánrech. **Dvoutýdenní měření zatím neproběhlo.**
