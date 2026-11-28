# Jak zjistíme, kdo vystoupil

| Odkud čerpáme | Co zjistíme |
|---|---|
| [Program ČRo](https://program.rozhlas.cz/program/html) | Co měla stanice daný den vysílat, v kolik a s kým. Program se může změnit. |
| [Archiv mujRozhlas](https://api.mujrozhlas.cz/episodes) | ID pořadu a dílu, popis, čas a dostupnou nahrávku. Uvedení stanice u celého pořadu ještě nepotvrzuje odvysílání konkrétního dílu. |
| Stránka dílu nebo nahrávka | Kdo vystoupil, v jaké roli, za kterou instituci a jak dlouho. Podpis pod článkem dokládá autorství textu. |

## Postup importu

1. **Projdi celý program stanice.** Příkaz `import --station cro-plus --from YYYY-MM-DD --to YYYY-MM-DD` zahrnuje oba krajní dny. Po každém dni ulož postup a případnou chybu. Opravám programu se přizpůsob opětovným načtením posledních sedmi dní. Starší období lze načíst znovu samostatně.
2. **Najdi díl v archivu.** Spoj záznamy podle ID nebo odkazu. Pokud chybí, porovnej pořad, čas, délku a anotaci. Záznamy spoj jen při jednoznačné shodě. U reprízy hledej premiéru i před začátkem období. Označ sestřih, nejasnou shodu nebo neznámé datum prvního vysílání.
3. **Zapiš jména, role a zdroj.** Pomohou údaje jako „hostem je“, „moderuje“ a „debatovali“. Nejasný případ zkontroluje člověk. U každého přiřazení uchovej odkaz a pasáž, ze které vychází. Žánr ulož u pořadu. U vystoupení rozliš roli v dílu (host, moderátor, autor komentáře) a postavení osoby v té době (např. politik, externí odborník, redaktor stanice). U politika dolož tehdy zastupovanou stranu a případně její účast ve vládě či opozici. Neznámý údaj nech otevřený.
4. **Uchovej vstupy pro opravy.** Každou odlišnou odpověď zdroje ulož neveřejně s URL, časem, stavem HTTP, otiskem obsahu a verzí parseru. Při dalším stahování využij podmíněné požadavky, omez počet souběžných spojení a respektuj pokyn serveru `Retry-After`. Před hromadným stažením ověř podmínky užití. Ruční opravu ulož zvlášť s důvodem a zdrojem. Při sestavení přehledu má přednost před výsledkem importu a přežije další načtení téhož dílu. Na webu zveřejni zjištěná fakta, potřebné citace a odkazy.
5. **Ověř úplnost podle stanice a žánru.** Kolik dní a minut programu máme? Kolik odvysílání jsme spojili s dílem? Kde známe obsazení a kde délku pouze odhadujeme? Dlouhé bloky průběžného vysílání vyhodnoť zvlášť. Parser testuj na uložených vstupech. Náhlý pokles úspěšnosti prověř před vydáním.

První verze může použít pravidla a ruční kontrolu. Pokud později zapojíme jazykový model, ke každému návrhu uchováme doklad, model, verzi zadání, otisk vstupu a jistotu. Před nasazením jej otestujeme na ručně ověřených případech. V první verzi s názorovými profily editor navrhne skóre, připojí citace a zaznamená schválení.

## Co ověříme na skutečných dílech

- **Hosté a reprízy.** Anotace debaty o slazených nápojích jmenuje oba hosty a uvádí, že premiéra proběhla dříve. Očekáváme dvě účasti ve stejném dílu a další odvysílání. [Pro a proti](https://plus.rozhlas.cz/dan-ze-slazenych-napoju-snizi-obezitu-soudi-ekonom-napoje-za-nemuzou-mini-9324188)
- **Autor článku a host.** Úvod dílu z 25. 11. 2026 uvádí Daniela Prokopa, pod článkem jsou tři podpisy. Pro účast hosta použijeme úvod. Vysílání na Plusu ověříme v programu této stanice. [Život k nezaplacení](https://radiozurnal.rozhlas.cz/danime-praci-ale-majetek-temer-vubec-cesko-je-v-tom-vyjimecne-rika-sociolog-9658893)
- **Kontrola archivu.** Porovnáme všechny pořady Plusu v posledním uzavřeném týdnu a v týdnu ze začátku dvouleté historie. Po žánrech uvedeme nedohledané díly a chyby v osobách či délkách. Tato kontrola zatím neproběhla.

U další stanice ČRo nejprve vyzkoušíme stejný import s jiným ID stanice. U jiného rádia ověříme jeden díl proti jeho programu a podle výsledku doplníme načítání zdroje. Třeba Radio Prostor zveřejňuje časy vysílacích bloků, ale z délky bloku nelze určit čas jednoho hosta. Rozsah jeho historického archivu zatím neznáme. Po přidání rádia ověříme, že se údaje Plusu nezměnily. [Program Radia Prostor](https://www.radioprostor.cz/program)
