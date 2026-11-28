# SlantIndex

SlantIndex ukáže, kdo dostává prostor na ČRo Plus a jaké veřejně doložené postoje tito lidé nebo zastupované instituce prosazují. Čtenář uvidí ekonomické a kulturní skóre stanice za posledních 30 dní, dvouletý trend a díly, ze kterých výsledek vychází.

## Co dodáme postupně

1. **Kdo vystoupil.** Projdeme všechny pořady ČRo Plus za posledních 30 dní. Web ukáže osoby, role, počty dílů a odkazy na originály. U dílu s neznámým obsazením to uvede.
2. **Kolik prostoru dostal.** Přidáme odvysílané minuty včetně repríz. Hodinový rozhovor odvysílaný dvakrát dá hostovi 120 minut a jeden původní díl.
3. **Jaké postoje dostávají prostor.** Přidáme karty osob a institucí se skóre, důvodem a citacemi. U každého vystoupení ukážeme, zda jsme použili skóre osoby, strany nebo instituce. Čtenář může navrhnout opravu. [Jak skóre počítáme](METHODOLOGY.md)
4. **Jak se výběr mění.** Historii doplníme po měsících až na dva roky. Graf půjde rozkliknout podle pořadu, redaktora, osoby a instituce.

## Jak web funguje

Python načte program a stránky dílů. SQLite uloží díly, jejich odvysílání, účastníky, role a hodnocení se zdroji. Astro zveřejní přehledy na Cloudflare. Každé odvysílání má `station_id`, takže další rádio může používat stejný výpočet i web. [Jak získáme a ověříme data](SOURCES.md)

První implementační PR přidá migraci SQLite, vzorky pro testy a výsledek kontroly dvou týdnů podle [popisu zdrojů](SOURCES.md). První verze je hotová, když web zobrazí celý dostupný program za 30 dní, označí mezery a opakovaný import stejných dat nezmění počty ani ruční opravy.

## Co zveřejníme

První verze ukáže jména, role a zdroje. Při zavedení skóre zveřejníme profily institucí a stran. U politiků a dalších veřejných činitelů editor jednotlivě posoudí podklady a oprávnění zveřejnit osobní skóre. U ostatních osob standardně zobrazíme jen doložená vystoupení. U každého převzatého skóre pojmenujeme stranu nebo instituci, které patří.

Před vydáním osobních profilů popíšeme v `PRIVACY.md`, podle čeho o zveřejnění rozhodujeme, jak požádat o opravu či stažení a jak dlouho uchováváme podněty. Při stažení odstraníme osobní skóre i z veřejné historie, exportů a dříve vydaných stránek a přepočítáme dotčené grafy.
