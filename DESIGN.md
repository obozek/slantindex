# SlantIndex

SlantIndex sleduje, kdo dostává prostor ve vysílání jednotlivých rozhlasových stanic. Začínáme na ČRo Plus. Hlavní ukazatel váží veřejně doložené postoje minutami odvysílaného prostoru, včetně repríz. Vedle něj stojí počet původních dílů s danou osobou. Návštěvník tak rozliší **„je často slyšet“** od **„opakovaně dostává nový pořad nebo pozvání“**. Poslechovost ani přesvědčivost měřeny nejsou.

## Směr a pořadí dodávek

Cílem je profil každé sledované stanice: koho zve, kolik prostoru jednotlivé hlasy dostávají a jak se obě názorové osy vyvíjejí během dvou let. Čtenář si může ověřit výsledek až u zdrojového dílu. Níže uvedené kroky jsou postupné ukázky produktu. Po každé lze podle skutečných dat změnit pořadí dalších prací.

| Krok | Co už lze otevřít a ověřit |
|---|---|
| 1. Jeden pořad | Jeden týden *Pro a proti* na ČRo Plus. Jednoduchá stránka ukáže datum, díl, hosty a odkaz na originál. Prokliky lze ručně porovnat s programem. Stačí ručně spuštěný import do SQLite a lokální náhled. |
| 2. Čas a četnost | Za 30 dní postupně přidat další pořady Plusu. U osoby je vidět počet různých dílů a přidělené minuty. Na konkrétní repríze lze ověřit, že vzrostly jen minuty. U neúplných pořadů je vidět chybějící pokrytí. |
| 3. První názorový přehled | U nejčastěji zastoupených institucí doložit zařazení na osách. Návštěvník otevře podklady a uvidí rozložení i podíl zařazeného času. Když je splněn publikační práh, objeví se také index. |
| 4. Historie | Ověřit starší kontrolní týden, doplňovat historii po měsících a po každém doplnění prodloužit graf. Cíl pro Plus jsou všechny pořady a dva roky s vyznačenými mezerami. Denní import pak udržuje přehled aktuální. |
| 5. Další rádio | Až bude přehled Plusu použitelný, ověřit zdroj jedné další stanice. Podle jejího programu rozhodnout, co sdílet v importu. Porovnání dostane vlastní stránku až se skutečnými daty obou stanic. |

**Rozhodnutí pro první krok.** Každé odvysílání nese `station_id`. Zdrojové ID uchováváme spolu s jeho původem. Modul importu ČRo převádí jeho HTML/JSON na pořad, díl, odvysílání a účast osoby. Web i výpočet čtou tyto záznamy pro zvolenou stanici. Tím zůstává otevřená cesta k jinému zdroji. Potřebu registru adaptérů či konfiguračního souboru posoudíme u druhé integrace.

## Cílové pohledy

| Pohled | Výsledek |
|---|---|
| Úvodní stránka | Profil vybrané stanice ukáže obě osy za posledních 30 uzavřených dní, pokrytí a dvouletý trend. Úvodní stránka se otevře přímo na profilu Plusu. Každá zobrazovaná hodnota patří jedné stanici. |
| Stanice a pořad | Odvysílané minuty, premiéry a reprízy, počet původních dílů, unikátní osoby, podíl pěti nejčastěji slyšených osob na minutách a rozložení obou os. Výchozí okno pořadu 90 dní. |
| Osoba a redaktor | Role, pořady, doložené vazby a díly. U moderátora zvlášť hosté jeho dílů a jeho vlastní komentáře. Osobní hodnocení se zobrazuje podle publikačních pravidel níže. |
| Instituce | Zastoupené minuty a díly podle lidí a pořadů. Pravidelný pořad a hostování jinde lze porovnat. Samostatný filtr ukáže osoby s doloženou profesní vazbou. |

Proklik z bodu grafu zachová čas, role, žánr, stanici a způsob výpočtu. Detail ukáže zdroj, délku, přidělené minuty a podklad pro zařazení. Výchozí **externí hlasy** zahrnují hosty, komentátory i pravidelné externí spoluprůvodce. Další pohled přidá interní vystupující. Počet pouhých moderací a autorství webových článků je dostupný zvlášť. U politiků lze oddělit vládu, opozici a ostatní k datu vzniku dílu. Události v grafu (volby, nástup vlády) mají datum a zdroj.

[Pravidla indexu a kontrolní příklady](METHODOLOGY.md) · [Zdroje a plán ověření](SOURCES.md)

## Architektura

První ukázku tvoří import v Pythonu, SQLite a jedna stránka v Astro. Při prvním veřejném vydání přibude statický hosting na Cloudflare. Následující komponenty se zavádějí s funkcí, která je potřebuje.

| Součást | Rozhodnutí |
|---|---|
| Sběr a redakce | Python CLI pro import z programu a archivu ČRo. Historii lze doplnit na notebooku. Po zavedení denních aktualizací spouští přírůstky `systemd.timer` na Linuxu. |
| Hlavní úložiště | SQLite na SSD, cizí klíče, WAL, `busy_timeout`, krátké zapisovací transakce. Import a editor mohou pracovat souběžně. Zdroje a schválené opravy jsou oddělené vrstvy. |
| Web a distribuce | Astro + TypeScript na Cloudflare Workers Static Assets. Python předpočítá titulní přehled. U vlastních filtrů prohlížeč čte měsíční balíčky po stanicích, sjednotí role podle ID osoby v úseku a sečte váhy. Stejná sada příkladů ověří oba výpočty. |
| Vydání veřejných profilů s hodnocením | Balíčky v neveřejném R2. Worker vydává jen data aktuální revize podle jediného ukazatele v D1. Při změně revize během načítání klient zahodí rozpracovaný výpočet a obnoví výběr. Jmenná data a skóre mají `Cache-Control: no-store`; do statických assetů patří pouze rozhraní. |
| Cena | Cíl 0 Kč za hosting při využití bezplatných kvót. Dynamické dotazy na data spotřebovávají kvóty Workeru, D1 a R2. Soubory se sdružují po měsících, katalog po blocích. Build hlídá velikost i počet assetů. [Limity Workers](https://developers.cloudflare.com/workers/platform/limits/) · [D1](https://developers.cloudflare.com/d1/platform/pricing/) · [R2](https://developers.cloudflare.com/r2/pricing/) |

## Datový model

Tabulky přibývají po krocích. První migrace pokryje stanici, pořad, díl, odvysílání, osobu, její roli a zdroj. Úseky s přiděleným časem vzniknou ve druhém kroku, hodnocení a jejich podklady ve třetím.

| Entity | Klíče a obsah |
|---|---|
| `broadcaster, station, show, episode, broadcast, segment` | Stanice má vlastní ID a vazbu na provozovatele; externí klíč tvoří jmenný prostor zdroje, typ entity a její zdrojové ID. Stanice si ponechá interní ID i při změně webu či adaptéru. Žánr pořadu, identita obsahu a premiéra. Odvysílání je konkrétní výskyt na stanici (unikátní stanice + začátek), s koncem, původem délky a typem premiéra / repríza / neurčeno. Nepřekrývající se úseky připojují skutečnou odvysílanou verzi k obsahu. |
| `person, organization, affiliation, capacity` | Stabilní ID, potvrzené aliasy, instituce/strana, druh osoby, funkce, vláda/opozice a jejich intervaly platnosti. U vystoupení uchovej tehdejší roli, výslovné zastoupení a redakční vztah k vysílající stanici či jejímu provozovateli (interní/externí/neurčeno). |
| `appearance, segment_person, article_credit` | Unikátní díl–osoba pro počty původních dílů. Úsek–osoba nese množinu rolí a způsob přidělení času. Samostatná vazba autor–článek. |
| `source_snapshot, proposal, override` | URL, čas a hash soukromého snímku. Návrh extrakce nebo hodnocení má cíl, původce, verzi pravidla, doklad ve zdroji, jistotu a rozhodnutí. Ruční oprava překrývá výsledek parseru a přežije nový import. |
| `assessment, evidence, publication_rule` | Subjekt, osa, stav, hodnota, jistota, zdroje, editor, revize a časová platnost. Platné schválené intervaly pro subjekt a osu se nepřekrývají. Publikační oprávnění je zvlášť od hodnocení. |
| `import_run, correction, release` | Pokrytí podle stanice/dne/žánru, rozhodnutí k podnětům a konzistentní vydání se zdrojovou i metodickou revizí. D1 uchovává frontu a aktivní vydání, hlavní SQLite schválený stav. |

## Provoz veřejné verze

- **Podnět:** formulář u osoby, instituce či dílu odešle ID cíle, revizi, změnu, důvod a volitelný zdroj. Worker ověří vstup a token Turnstile, omezí četnost a velikost. Přijaté rozhodnutí editor uloží transakčně pod unikátním ID, pak potvrdí podnět v D1. Veřejný je výsledek a redakční odůvodnění. Surová podání zůstávají neveřejná. Provozní návrh: smazat text a případný kontakt 90 dní po uzavření, ponechat ID, rozhodnutí a minimální auditní stopu.
- **Publikační úrovně:** u institucí a stran lze vydat zdůvodněná hodnocení. U veřejných politických představitelů vyžaduje jmenné hodnocení individuální redakční a právní posouzení. U ostatních osob včetně zaměstnanců sledovaných rádií publikuje první verze doložené role, četnost, čas a výslovně zastupovanou instituci. Soukromé politické skóre se pro ně nevytváří ani nepřenáší klientovi. Skóre instituce je tak označeno i u konkrétního vystoupení. Před spuštěním dokumentovat oprávnění a dobu uchování pro každou třídu údajů. [GDPR, čl. 6, 9 a 85](https://eur-lex.europa.eu/legal-content/CS/TXT/?uri=CELEX:32016R0679)
- **Stažení:** editor označí dotčený údaj jako neveřejný. U naléhavé žádosti Worker do přepočtu dočasně zablokuje dotčené datové balíčky a závislé souhrny. Nové vydání odstraní údaj z karet, vyhledávání, řádků, agregací a veřejné historie. Staré datové verze ani náhledy nesmějí obejít Worker. Otestovat i přímou starou URL. Neveřejný seznam stažení se znovu aplikuje před vydáním z obnovené zálohy.
- **Vydání a obnova:** nahraj kompletní data, ověř počty, odkazy a srovnání klientského a referenčního výpočtu, teprve pak přepni revizi. Při neúspěchu zůstává předchozí vydání s datem aktualizace, s výjimkou zablokovaných údajů. Denní záloha SQLite přes Backup API do neveřejného R2, pravidelná zkouška obnovy včetně překryvů a stažení.
- **Ověření po krocích:** pro seznam dílů porovnej výstup parseru s uloženým vzorkem. Pro zveřejnění skóre ověř reprodukovatelnost z detailu a stažení údajů. Před rozšířením historie ověř starší formát archivu. Licenci kódu a podmínky dalšího šíření zdrojových dat vyřeš před veřejným vydáním.
