# SlantIndex

Kdo dostává prostor na ČRo Plus a jak se složení hostů mění v čase? Hlavní stránka ukáže ekonomickou a kulturní osu stanice za posledních 30 dní a pod nimi vývoj za dva roky. Z grafu lze přejít na pořad, osobu či instituci a dohledat díly a podklady pro její zařazení.

## Tři části aplikace

| Část | Úloha |
|---|---|
| Import v Pythonu | Pro zadané období přečte program a stránky dílů ČRo Plus. Uloží časy vysílání, reprízy, osoby, jejich role a odkaz na zdroj. |
| SQLite | Uchová pořady, díly, jednotlivá odvysílání, osoby, instituce a doložená hodnocení na obou osách. Každé odvysílání má `station_id`. |
| Web v Astro na Cloudflare | Zobrazí přehledy vypočtené ze SQLite, pokrytí dat a odkazy na originály. U chyby půjde navrhnout opravu ke schválení. |

**Výpočet.** Čas se počítá pro každou stanici zvlášť. Hodinový rozhovor s jedním hostem a jeho úplná repríza znamenají 120 minut a jeden původní díl. U více hostů se použijí známé úseky nebo označený odhad. U indexu je vždy vidět, jaká část času má doložené zařazení. [Metodika](METHODOLOGY.md)

**První použitelná verze.** Z reálného programu Plusu zobrazit, kdo vystoupil, kolikrát a v kterých dílech. Dalšími přírůstky jsou minuty, hodnocení a delší historie. Osobní politické profily vyžadují posouzení podkladů a oprávnění ke zveřejnění. Stažení hodnocení se musí promítnout i do publikovaných dat a grafů.

**Další rádia.** Specifika webu ČRo patří do importu. Až přidáme jinou stanici, její import uloží údaje ve stejném tvaru. Výpočet i web už vybírají data podle `station_id`. [Zdroje](SOURCES.md)
