# SlantIndex

Kdo dostává prostor na ČRo Plus a jak se složení hostů mění v čase? Hlavní stránka ukáže ekonomickou a kulturní osu stanice za posledních 30 dní a pod nimi vývoj za dva roky. Z grafu lze přejít na pořad, osobu či instituci a dohledat díly a podklady pro její zařazení.

## Tři části aplikace

| Část | Úloha |
|---|---|
| Import v Pythonu | Pro zadané období projde všechny pořady ČRo Plus a jejich dostupné stránky dílů. Uloží časy vysílání, reprízy, osoby, jejich role a odkaz na zdroj. |
| SQLite | Uchová pořady, díly, jednotlivá odvysílání, osoby, instituce a doložená hodnocení na obou osách. Každé odvysílání má `station_id`. |
| Web v Astro na Cloudflare | Zobrazí přehledy vypočtené ze SQLite, pokrytí dat a odkazy na originály. U chyby půjde navrhnout opravu ke schválení. |

## Co je názorový profil

Osoba i instituce mají vlastní kartu. Karta odpovídá na dvě otázky: **Jaké ekonomické postoje veřejně prosazuje? Jaké kulturní postoje veřejně prosazuje?** Na každou odpovídá zvlášť hodnotou od −2 do +2, jednou větou zdůvodnění a krátkou citací s odkazem na originál. Kde podklady chybějí, zobrazuje se „nezařazeno“. Člověka hodnotíme podle jeho vlastních výroků a návrhů. Organizaci podle jejích oficiálních stanovisek, programů a doporučení. [Stupnice a příklady citací](METHODOLOGY.md#jak-vznikne-názorový-profil)

**Čí skóre se započítá?** Když host vystupuje za instituci, použijeme její skóre. Když vystupuje sám za sebe, použijeme jeho osobní skóre. Pokud zvolený profil nemá hodnocení na konkrétní ose, minuty na této ose označíme jako nezařazené.

**Výpočet.** Čas se počítá pro každou stanici zvlášť. Hodinový rozhovor s jedním hostem a jeho úplná repríza znamenají 120 minut a jeden původní díl. U více hostů se použijí známé úseky nebo označený odhad. U indexu je vždy vidět, jaká část času má doložené zařazení. [Metodika](METHODOLOGY.md)

**První použitelná verze.** Za posledních 30 dní projít celý program ČRo Plus a zobrazit, kdo vystoupil, kolikrát a v kterých dílech. Kde hosta nelze z dostupných údajů určit, označit chybějící údaj. Dalšími přírůstky jsou minuty, hodnocení a delší historie. Osobní politické profily vyžadují posouzení podkladů a oprávnění ke zveřejnění. Stažení hodnocení se musí promítnout i do publikovaných dat a grafů.

**Další rádia.** Specifika webu ČRo patří do importu. Až přidáme jinou stanici, její import uloží údaje ve stejném tvaru. Výpočet i web už vybírají data podle `station_id`. [Zdroje](SOURCES.md)
