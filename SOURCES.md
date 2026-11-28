# Zdroje a ověření importu

## ČRo Plus

| Zdroj | Co převzít | Omezení |
|---|---|---|
| [Program ČRo](https://program.rozhlas.cz/program/html) | Stanice, den, čas, název a anotace jednotlivých vysílání. | Plán může předcházet programové změně. Obecný několikahodinový blok nedokládá hosta po celou svou délku. Chybějící den je mezera v datech. |
| [API mujRozhlas](https://api.mujrozhlas.cz/episodes) | Stránkované epizody, ID dílu a pořadu, popis, časy a dostupná metadata audia. | Pole `relationships.stations` může odkazovat na stanice pořadu. Každé konkrétní odvysílání musí doložit program či záznam. Stopáž archivní verze se může lišit od vysílání. |
| Stránka dílu a případně záznam vysílání | Role, jména, instituce, údaj o repríze, skutečná délka nebo hranice úseku. | Podpis může označovat redaktora webu. Samotná shoda jména v titulku průkaznou účast nezakládá. |

## Import a dohledatelnost

1. Příkaz `import --station cro-plus --from YYYY-MM-DD --to YYYY-MM-DD` zahrnuje oba krajní dny; ID stanice vybere položku katalogu. Ruční import lze spustit i pro pilotní stanici. Denní úloha zpracuje všechny publikované stanice, postup i chyby vede po stanici a dni. Výpadek jednoho zdroje neblokuje ostatní. Opakované načtení posledních sedmi dnů zachytí změny. Starší interval lze přehrát samostatně.
2. Páruj přednostně přes ID epizody či kanonický odkaz. Náhradní vazbu podle pořadu, času, délky a anotace dovol jen při jediném přesvědčivém kandidátovi. Reprízy starších pořadů hledej i před importovaným obdobím. Sporné shody, odlišné sestřihy a neznámý počátek historie mají zvláštní stav.
3. Každé různé tělo odpovědi ulož soukromě podle hashe spolu s URL, časem, HTTP stavem, verzí parseru a dostupnými hlavičkami pro podmíněné načtení. Souběh omez podle hostitele, respektuj pravidla zdroje, `Retry-After` a odklad opakovaných pokusů. Před hromadným importem ověř přístupové a užívací podmínky. Ve veřejném výstupu používej vlastní strukturovaná fakta, nezbytné doklady a odkazy.
4. Parser čte strukturovaná pole a vzory typu „moderuje“, „hostem je“, „debatovali“. U volného textu vytvoří kandidáta pravidlo nebo editor. Volitelný jazykový model může návrh doplnit o výřez dokladu. Ukládej model/verzi, verzi pokynu, vstupní hash a jistotu. Návrh názorového profilu připraví editor z dohledaných primárních zdrojů (program, podepsaný text, přímý veřejný výrok); u stran lze importovat datovanou expertní studii. Případný model pouze předvyplní návrh. Nejasné extrakce a všechna hodnocení před publikací schvaluje editor. Pokyny a validační vzorek verzuj před zapnutím modelu. Z první verze nevzniká závislost na placeném API.
5. Ověřuj import podle stanice **i žánru**. Počítej získané stanico-dny, pokryté sekundy vůči době dostupného programu, míru spárování dílů, úplnost obsazení a podíl času s doloženou/odhadnutou délkou. Proudové vysílání vykazuj zvlášť. Testy přehrávají uložené vstupy; náhlý pokles pokrytí proti poslednímu srovnatelnému období vyvolá kontrolu před vydáním.

## Ověřené případy a hranice pilotu

- *Pro a proti*, daň ze slazených nápojů. Stránka dokládá účast obou diskutujících a výslovně připomíná starší premiéru. Import získá hosty z úvodu a druhé vysílání připojí ke stejnému obsahu. [Díl na ČRo Plus](https://plus.rozhlas.cz/dan-ze-slazenych-napoju-snizi-obezitu-soudi-ekonom-napoje-za-nemuzou-mini-9324188)
- *Život k nezaplacení*, 25. 11. 2026. V úvodu je Daniel Prokop uveden jako účastník, v podpisu jsou tři položky. Text dokládá účast, podpis autorství. U sdíleného pořadu je pro zahrnutí do Plusu potřeba doložit konkrétní vysílání v programu Plusu. [Díl na Radiožurnálu](https://radiozurnal.rozhlas.cz/danime-praci-ale-majetek-temer-vubec-cesko-je-v-tom-vyjimecne-rika-sociolog-9658893)
- Pilot má pokrýt sedm dní na začátku dvouletého období a posledních sedm uzavřených dní na ČRo Plus. Ulož vstupy nebo povolené minimalizované vzorky, označ role a časové úseky v kontrolním vzorku a změř přesnost i podíl nalezených vystoupení. U délek porovnej zdroj odhadu a absolutní chybu proti ručně ověřeným minutám. Uveď velikost vzorku a výsledky po žánrech. **Dvoutýdenní měření zatím neproběhlo.**

## Přidání stanice

1. **Zapiš stanici do `stations.toml`.** Ukázka vstupní konfigurace pro ověřovací import:

   ```toml
   [[stations]]
   id = "cro-plus"
   name = "ČRo Plus"
   broadcaster = "cro"
   adapter = "cro"
   source_namespace = "mujrozhlas"
   source_key = "plus"
   status = "pilot"
   ```

   `id` je stálý klíč pro URL a historická data. `source_key` vybírá kanál u zdroje. `source_namespace` určuje, kde platí externí identifikátory; dva nezávislé archivy mohou používat tentýž parser i stejná čísla dílů. U další stanice již podporovaného zdroje, například Radiožurnálu, stačí odpovídající záznam.
2. **Nový formát zdroje potřebuje jeden adaptér a jeho vzorky.** Společné rozhraní má dvě operace: `schedule(station, from_date, to_date)` vrátí odvysílání s časy a odkazy na obsah; `episode(station, ref)` vrátí dostupná metadata dílu, role, úseky a zdrojové doklady. Neznámé hodnoty zůstanou označené. Adaptér se registruje pod klíčem `adapter`. Párování, deduplikaci, přidělení minut, SQLite a web zajišťuje společná část aplikace.
3. **Ověř a publikuj.** Na dvou kontrolních týdnech prověř obsazení, délky a reprízy. Při úspěchu nastav `status = "published"` a vydej data. Veřejný katalog obsahuje stanice v tomto stavu s úspěšně vydanými daty. Uvádí skutečně dostupné období každé stanice.
4. **Akceptační test rozšiřitelnosti.** Ke vzorku stanice A přidej pouze konfiguraci stanice B podporované stejným adaptérem. Importuj tytéž lokální ID z různých archivů a reprízu na B. Ověř izolaci ID a počtů, shodné výsledky A před a po importu, vlastní stránku B a její výběr v porovnání. Test s jiným zdrojovým formátem smí navíc přidat adaptér, jeho registraci a vzorky. V obou případech zůstávají schéma SQLite, výpočet a frontend společné.

**Kandidát na druhou stanici: Radio Prostor.** Veřejný program uvádí pořady, časy a u části bloků moderátory. Tříhodinový blok s hosty vyžaduje další zdroj pro délku samotného rozhovoru. Dostupnost dvouleté programové historie ani přesnost párování s publikovanými rozhovory zatím nejsou ověřené. [Program Radia Prostor](https://www.radioprostor.cz/program)
