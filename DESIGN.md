# SlantIndex

SlantIndex ukáže, kdo dostává prostor na ČRo Plus a jaké veřejně doložené postoje tito lidé nebo zastupované instituce prosazují. Čtenář uvidí ekonomické a kulturní skóre stanice za posledních 30 dní, dvouletý trend a díly, ze kterých výsledek vychází.

## Co dodáme postupně

1. **Kdo vystoupil.** Projdeme všechny pořady ČRo Plus za posledních 30 dní. Web ukáže osoby, role, počty dílů a odkazy na originály. U dílu s neznámým obsazením to uvede.
2. **Kolik prostoru dostal.** Přidáme odvysílané minuty včetně repríz. Hodinový rozhovor odvysílaný dvakrát dá hostovi 120 minut a jeden původní díl.
3. **Jaké postoje dostávají prostor.** Přidáme karty osob a institucí se skóre, důvodem a citacemi. U hosta zastupujícího instituci platí její skóre. U hosta mluvícího za sebe platí jeho vlastní. Čtenář může navrhnout opravu. [Jak skóre počítáme](METHODOLOGY.md)
4. **Jak se výběr mění.** Historii doplníme po měsících až na dva roky. Graf půjde rozkliknout podle pořadu, redaktora, osoby a instituce.

## Jak web funguje

Python načte program a stránky dílů. SQLite uloží díly, jejich odvysílání, účastníky, role a hodnocení se zdroji. Astro zveřejní přehledy na Cloudflare. Každé odvysílání má `station_id`, takže další rádio může používat stejný výpočet i web. [Jak získáme a ověříme data](SOURCES.md)

Před zveřejněním politického profilu konkrétní osoby posoudíme podklady a oprávnění ke zveřejnění. Stažené hodnocení odstraníme i z veřejných dat a přepočítáme grafy.
