# SlantIndex

SlantIndex měří, **koho a jak často je slyšet v Českém rozhlase**. Pokrývá všechny pořady všech celoplošných i regionálních stanic za poslední dva roky. Jednotkou je člověk v konkrétním dílu. Jeho váhu určuje počet vystoupení. Tón rozhovoru, délka projevu a odmítnutá pozvání do výpočtu nevstupují.

## 1. Co uvidí čtenář

| Pohled | Obsah |
|---|---|
| Přehled ČRo | Řádek za každou stanici: obě osy za posledních 30 dní, počet vystoupení a pokrytí. Pod tabulkou dvouletý graf vybrané stanice, při otevření za celý ČRo. |
| Stanice a pořad | Trend, rozložení po stupních škály a seznam osob s počtem vystoupení. Kliknutí na bod nebo sloupec otevře přesné díly zahrnuté do hodnoty. |
| Redaktor | Hosté v dílech, které moderoval. Vlastní komentáře a moderátorské vstupy mají samostatný přehled. |
| Osoba | Role, pořady, instituce v době vystoupení, obě hodnocení, zdůvodnění, odkazy a historie oprav. |
| Instituce | Vystoupení zástupců podle pořadu a období. Odděleně pravidelná rubrika a ostatní pořady. Přepínač rozšíří seznam na všechny tehdejší spolupracovníky. |

Filtry pro období a role se zachovají při prokliku. Karta hodnocení i jednotlivé vystoupení mají vlastní odkaz a tlačítko **Navrhnout opravu**.

## 2. Co se počítá

- **Jeden člověk × jeden původní díl = jeden hlas.** Tři hosté znamenají tři hlasy. Stejný spoluprůvodce ve třiceti dílech má třicet hlasů. Repríza pouze přidá záznam o odvysílání. Společná premiéra dvou stanic patří jednou každé stanici a jednou celému ČRo. Datum hlasu určuje premiéra, včetně premiér před začátkem sledovaného období.
- **Role.** Výchozí výběr zahrnuje hosty, interní experty, komentátory a pravidelné spoluprůvodce. Moderátory a redaktory lze zahrnout přepínačem. Při více vybraných rolích se dvojice člověk–díl započítá jednou. Podpis webového článku evidujeme jako autorství. Do ukazatele vstupuje až doložená vysílací role.
- **Osy.** Ekonomická jde od nízkých daní, menšího státu a přerozdělování (−) k vyšším daním, většímu státu a přerozdělování (+). Kulturní od konzervativní (−) k progresivní (+). Stupnice −2, −1, 0, +1, +2. Znaménko určuje směr, 1 dílčí či mírnou preferenci, 2 výraznou a soustavně doloženou preferenci. Nula vyžaduje doloženou středovou či smíšenou pozici. Nedostatek důkazů má hodnotu `NULL` pro každou osu zvlášť.
- **Přiřazení.** Pro doložené vystoupení jménem instituce použij její hodnocení platné v den premiéry. V ostatních případech použij veřejně doložený profil osoby. Pouhé zaměstnání zakládá vazbu na instituci. Každé publikované hodnocení schvaluje editor podle verzované metodiky a dokládá konkrétním veřejným stanoviskem, programem či návrhem. U sporných os může ponechat nezařazeno.
- **Výpočet.** Pro osu a vybraný soubor vystoupení je index `Σ skóre / K`, kde `K` je počet zařazených a `N` počet všech doložených vystoupení ve výběru. Zobraz průměr, četnosti všech pěti stupňů a `K/N`. Při `K = 0` zobraz „bez dat“. Souhrn ČRo počítej z vystoupení po odstranění duplicit. Chybějící obsazení dílů vykazuj zvlášť, protože počet chybějících osob neznáme.
- **Čas.** Každý den grafu končí posledním dnem svého 30denního okna v pásmu `Europe/Prague`. Titulní hodnoty a pravý okraj grafu používají stejný poslední uzavřený den a verzi dat. Import načte i 29 dní před začátkem grafu.

## 3. Architektura a uložení

| Součást | Implementace a odpovědnost |
|---|---|
| Import | Python CLI, HTTP klient a parser HTML. První import na notebooku, další denně přes `systemd.timer` na Raspberry Pi nebo jiném Linuxu. |
| Hlavní databáze | Soubor SQLite na trvalém disku, jeden zapisující proces, transakce, cizí klíče a SQL migrace v Gitu. Editor používá místní CLI. |
| Publikace | Python sestaví agregace a seznamy dílů. Astro + TypeScript vydá statický web a JSON dělený podle entity a období přes Cloudflare Workers Static Assets. Běžné čtení obslouží CDN. |
| Podněty | Cloudflare Worker přijímá formulář do D1. D1 uchovává frontu podnětů, hlavní SQLite schválené změny. Přístup editora je autentizovaný. |
| Obnova a cena | Denní konzistentní záloha přes SQLite Backup API do neveřejného R2 Standard. Hosting může při využití bezplatných kvót stát 0 Kč měsíčně. Vlastní doména, elektřina a redakční práce jsou samostatné náklady. [Static Assets](https://developers.cloudflare.com/workers/static-assets/billing-and-limitations/) · [D1](https://developers.cloudflare.com/d1/platform/pricing/) · [R2](https://developers.cloudflare.com/r2/pricing/) |

**Minimální datový model**

| Entity | Klíče a význam |
|---|---|
| `station`, `show`, `episode`, `broadcast` | Díl má pořad, původní datum a stabilní ID. Odvysílání má stanici, čas a typ premiéra / repríza / neurčeno. Unikátní dvojice stanice–začátek. |
| `person`, `organization`, `affiliation` | Stabilní ID, aliasy a časová platnost vazeb osoby k institucím. |
| `appearance`, `appearance_role`, `article_credit` | Unikátní dvojice díl–osoba, její vysílací role, případná zastupovaná instituce a zdroj. Podpis článku má vlastní záznam. |
| `assessment`, `evidence` | Osoba nebo instituce, osa, hodnota, zdůvodnění, zdrojová URL, interval platnosti, datum schválení a revize. U stejného subjektu a osy se schválené intervaly jedné revize nepřekrývají. |
| `import_run`, `correction`, `release` | Pokrytí podle data a stanice, původ změn, rozhodnutí editora a identifikátor vydané verze dat a metodiky. |

## 4. Import, vydání a opravy

1. **Import rozsahu.** `import --from YYYY-MM-DD --to YYYY-MM-DD [--station ID]` projde oba krajní dny, ve výchozím režimu všechny stanice. Soupis odvysílání vychází z [programu ČRo](https://program.rozhlas.cz/program/html), metadata dílů ze [stránkovaného API mujRozhlas](https://api.mujrozhlas.cz/episodes) a stránek epizod.
2. **Extrakce.** Z programu a anotace čti výslovně uvedené hosty, moderátory a komentátory. Detail dílu doplní role, instituci a podpis článku. Ulož URL, krátký doklad, čas načtení a verzi parseru. Jména spojuj přes zdrojové ID, profil nebo potvrzený alias. Shodná jména, nejasné reprízy a role jdou ke kontrole. Plošný přepis audia není součástí importu.
3. **Opakovatelnost a pokrytí.** Ukládej postup po stanici a dni, změněná metadata aktualizuj podle stabilních klíčů, zachovej ruční opravy. Denně znovu načti posledních sedm dní kvůli opožděným úpravám. Rozliš chybějící program, nedohledaný díl a díl s úplným, částečným, neznámým nebo doloženě prázdným obsazením.
4. **Podnět.** `POST /api/corrections` přijme ID cíle a revize, navrženou změnu, důvod a volitelný zdroj. Worker ověří vstup a omezí frekvenci podání. Editor rozhodne přijmout / zamítnout s odůvodněním. Přijatou změnu zapíše hlavní DB jednou pod ID podnětu, teprve poté se uzavře záznam v D1. Oprava omylu přepočítá dotčenou historii, změna postoje platí od doloženého data.
5. **Vydání.** Z jednoho konzistentního snímku vytvoř grafy i detaily, ověř počty a odkazy a publikuj je jako jednu verzi. Při selhání zůstane dostupná předchozí verze s datem aktualizace. Zveřejňuj schválené změny a jejich důvody, surová podání zůstávají neveřejná.

## 5. Ověření před spuštěním

- **Pokrytí zdrojů.** Na jednom týdnu ze začátku období a jednom současném týdnu ověř všechny stanice. Ručně porovnej vzorek jmen a rolí s díly. Zveřejni pokrytí po stanicích a zjištěné chyby. Úplnost dvouletého archivu je zatím otevřená.
- **Kontrolní výpočet.** Společná premiéra stanic A a B má hosty +2 a −1 a moderátora bez skóre. V základním pohledu mají obě stanice i celý ČRo index +0,5 a pokrytí 2/2. Po přidání moderátora je pokrytí 2/3. Repríza ani opakovaný import tyto výsledky nezmění.
- **Publikační kontrola.** Číslo v grafu musí jít reprodukovat ze zobrazených dílů. Vyzkoušej zpětnou opravu, změnu postoje od data a obnovu ze zálohy. Před publikací osobních politických profilů vyjasni podmínky zpracování těchto údajů. [GDPR, čl. 9 a 85](https://eur-lex.europa.eu/legal-content/CS/TXT/?uri=CELEX:32016R0679)
