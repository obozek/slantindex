# Metodika SlantIndexu · návrh v1

## 1. Čas a četnost

**Hlavní váha je odvysílaný prostor přidělený osobě**, měřený v sekundách a zobrazovaný v minutách. Hodinový rozhovor s jediným hostem přidá hostovi 60 minut. Jeho úplná repríza přidá dalších 60. Jde o čas pořadu věnovaný hostovi, včetně otázek. Výpočet nepředpokládá, že host právě tolik minut mluvil.

| Situace | Pravidlo |
|---|---|
| Jeden či více hostů | Rozděl vysílání podle doložených úseků se známým obsazením. Jedinému hostu připadne celý úsek. Společný úsek více vystupujících rozděl rovným dílem a označ odhad. Čtyřicet minut dvou hostů znamená po 20 minutách. U zveřejněných údajů rozliš čas celého známého úseku a odhad podílu konkrétní osoby. |
| Smíšený pořad | Započítej doloženou část s hosty. Hudba, reklama, zprávy nebo další rozhovor mimo ni nedostanou váhu původního hosta. U neúplného obsazení nebo neznámé délky rozhovoru v magazínu ponech čas nepřiřazený. Celou stopáž lze použít u doloženého celodílového formátu. |
| Role a filtry | Pro každý úsek rozděl čas mezi všechny obsahově vystupující **před filtrováním**. Role téže osoby tvoří množinu. Vypnutí jednoho ze dvou hostů nezvýší váhu druhého. Čistě moderátorský čas tvoří samostatný pohled na vedení pořadů. Překryv s časem hostů se nesčítá. |
| Repríza, sestřih, souběh | Každá stanice vykáže každé své odvysílání. Sestřih používá vlastní délku a obsazení zachovaných úseků. Společná půlhodina přidá každé stanici 30 minut v jejím vlastním přehledu. Dosah v posluchačích neznáme. |
| Původní díly | Druhá metrika počítá osobu v jednom dílu jednou. Rozhoduje první odvysílání na sledované stanici. První převzetí staršího dílu jinou stanicí je v tomto pohledu výslovně označené. Neurčené první vysílání se vykazuje zvlášť. |

U nejisté reprízy mohou být doložené odvysílané minuty známé i při nejasném počtu původních dílů. Délka vychází ze začátku a konce skutečného odvysílání. Shodná verze s doloženou stopáží v archivu nebo údaj z programu jsou náhradní odhady s uvedeným původem. Mezery a překryvy se kontrolují po stanici; nadřazený blok a jeho dílčí pořady nesmějí vykázat stejné sekundy dvakrát. Na hranici okna se sekundy oříznou. Den se vymezuje v `Europe/Prague`, uplynulý čas se počítá z UTC. Repríza zachovává roli, příslušnost a zdroje hodnocení platné při vzniku záznamu (výchozí datum premiéry).

## Jak vznikne názorový profil

Názorový profil shrnuje veřejně zastávané postoje jedné osoby nebo jedné instituce. Na kartě jsou dva samostatné řádky: **ekonomika** (menší až větší role státu) a **kultura** (konzervativní až progresivní postoje).

| Stupeň | Ekonomická osa | Kulturní osa |
|---|---|---|
| −2 | Program rozsáhlého snížení celkových daní, veřejných výdajů a transferů. | Široké prosazování tradičních pravidel rodiny a veřejné morálky zákonem. |
| −1 | Dílčí snížení souhrnné zátěže nebo přerozdělování. | Zachování či cílené zpřísnění tradičních omezení v konkrétní oblasti. |
| 0 | Doložený střed nebo zdůvodněná kombinace opačných ekonomických priorit. | Doložený střed nebo kombinace protichůdných kulturních postojů. |
| +1 | Dílčí zvýšení souhrnného výběru nebo míry přerozdělování. | Dílčí rozšíření rovného zacházení či osobní volby, například práv partnerů. |
| +2 | Program podstatného zvýšení čistého daňového výběru a posílení přerozdělování. | Široké rozšíření osobní autonomie a rovnosti práv napříč více oblastmi. |

**Postup pro každou osu**

1. Najdi veřejný výrok, který lze přímo připsat hodnocenému. U člověka použij jeho vlastní slova, podepsaný text nebo návrh, který veřejně podpořil. U instituce použij oficiální stanovisko, program či reformu, kterou doporučuje. Zaměstnání člověka dokládá profesní vazbu.
2. Urči, co konkrétně prosazuje. V ekonomice zohledni čistý dopad na výběr daní, výdaje a přerozdělování. V kultuře například postoj k právům partnerů, reprodukčním otázkám nebo prosazování tradice zákonem. Porovnej relevantní výroky, včetně těch, které prvnímu závěru odporují.
3. Vyber stupeň podle tabulky. Na kartě zveřejni **hodnotu, proč odpovídá právě tomuto stupni, a krátké přesné citace**. U každé citace uveď mluvčího či autora, název zdroje, datum a odkaz na konkrétní pasáž (strana PDF nebo čas audia, pokud existuje). Číslo je úsudek SlantIndexu. Citace umožňuje tento úsudek zkontrolovat.
4. Když zdroj nestačí nebo zůstává rozpor, napiš „nezařazeno“ a důvod. Nula vyjadřuje doložený střed či smíšený postoj. Jistotu uveď zvlášť. U změny uchovej předchozí hodnocení, důvod změny, datum platnosti a schvalujícího editora.

**Ukázky odůvodnění.** Jde o příklady práce s konkrétním podkladem. Úplný profil zohlední i další relevantní zdroje.

| Karta a osa | Co může čtenář ověřit |
|---|---|
| PAQ Research · ekonomika | **Návrh +1.** PAQ se spoluautory doporučuje reformu, která ulevuje části pracujících a v součtu zvyšuje daňový výběr. Autoři píší: „Navrhovaná reforma by mohla vybrat do veřejných rozpočtů o 73 mld. Kč navíc vůči roku 2024.“ Dílčí zvýšení celkového výběru odpovídá +1. Samotná daňová studie nedokládá kulturní postoj. [PAQ Research, Centrum veřejných financí a IDEA, *Chytřejší daně*, 2025, oddíl 1.5.4, s. 50](https://chytrejsidane.cz/Studie_Chytrejsi_dane.pdf#page=51) |
| Jsme fér · kultura | **Návrh +1.** Iniciativa požaduje rozšíření jednoho konkrétního práva na stejnopohlavní páry. Její výzva zní „JE ČAS NA MANŽELSTVÍ PRO VŠECHNY PÁRY“. To odpovídá +1 v otázce rodinného práva. Pro +2 by byly potřeba doklady o širším programu napříč tématy. [Jsme fér, úvodní výzva, ověřeno 28. 11. 2026](https://www.jsmefer.cz/) |

Nejdřív zpracuj dosud nehodnocené profily s největším vysílacím časem. Čas určuje jejich váhu v přehledu stanice. **Skóre profilu určují pouze doložené postoje.** Pro výpočet pokrytí uchovej stav každé osy: `nehodnoceno / nedostatek důkazů / sporné / netýká se / zařazeno`. Číselnou hodnotu má pouze stav „zařazeno“.

### Čí profil použít při vystoupení

Osobní profil a profil instituce zůstávají oddělené. Při výpočtu výsledku stanice záleží na tom, v jaké roli člověk v daném dílu vystupoval.

| Vysílací role | Výchozí přiřazení po jednotlivých osách |
|---|---|
| Mluvčí nebo formální zástupce | Výslovně zastupovaná organizace, poté schválený a publikovatelný osobní profil. |
| Politik ve funkci | Při stranickém vystoupení strana. Při výkonu veřejné funkce schválený osobní profil, případně doložená tehdejší strana **jako označená náhradní hodnota**. Nominace bez členství nestačí. Nestraník bez hodnocení zůstane v počtech a minutách. |
| Výzkumník, analytik, komentátor | Schválený publikovatelný osobní profil, případně výslovně zastupovaná instituce s hodnocením. Pouhé pracoviště je pouze profesní vazba. Pokud publikace osobního profilu není povolena, tato větev se přeskočí. |

Přepínač **bez náhradních hodnot** vyloučí výplň chybějícího skóre institucí či stranou; jmenovatel všech přidělených minut se nezmění. V porovnání **osoba / instituce** lze nad stejnou množinou samostatně zobrazit obě čisté varianty včetně jejich pokrytí. Chybějící hodnota nepřejímá znaménko druhé osy. Doložený spor nelze skrýt automatickým přechodem na náhradní zdroj.

Pro kalibraci politických stran lze použít [CHES Europe](https://www.chesdata.eu/ches-europe/). Proměnné LRECON (0 levice, 10 pravice) a GALTAN (0 libertariánská, 10 tradiční) mají opačnou orientaci vůči našim osám. Návrh převodu pro obě: `z = 2 − 0,4 × x`, zaokrouhlení na celé číslo, přesnou polovinu od nuly. Test `0 → +2, 5 → 0, 10 → −2`. Zachovat ročník, původní hodnotu a zdroj. CHES hodnotí stranické vedení.

## 3. Výpočet a publikovatelnost

Pro jednu **stanici**, osu a zvolené okno: **index = Σ(sekundy × skóre) / S**, kde `S` jsou zařazené sekundy. `T` jsou všechny přidělené sekundy ve výběru, `R` z nich mají redakčně posouzený stav (včetně sporných). Zobraz `R/T` zkontrolováno, `S/T` zařazeno, rozložení minut v pěti stupních, rozpad stavů, podíl odhadovaných minut a rozsah nevyřešených bloků. Pokrytí programu a obsazení je samostatné měřítko. Četnost původních dílů používá stejný výpočet s jednotkovou vahou.

**Počáteční publikační práh:** nejméně 10 různých zařazených dvojic osoba–původní díl, alespoň 3 různé zařazené osoby a pokrytí vah alespoň 60 %. Reprízy zvyšují váhu, počet různých dvojic nezvýší. Pod prahem zobraz četnosti, minuty a důvod potlačení. Prahy jsou parametry metodiky k revizi po pilotu. Graf končí posledním uzavřeným dnem. Importuje se dalších 89 dní pro úplné počáteční okno pořadů.

Vliv nezařazených minut ukaž jako **rozsah citlivosti**. Pro vážený součet `B` a `U` minut s neznámým postojem jsou krajní hodnoty `(B ± 2U)/(S+U)`; všechny veličiny musí mít shodnou časovou jednotku. Minuty označené „netýká se“ leží mimo tento výpočet. Interval popisuje možné hodnoty u nepokrytých postojů. Neúplně zachycené vysílání vyžaduje samostatný údaj o pokrytí.

**Porovnání stanic.** Použij společné dostupné období, stejnou délku okna, role, žánrový filtr a revizi metodiky. Každá stanice má vlastní jmenovatel, pokrytí a publikační práh. Výpadek archivu zobraz jako mezeru. Přidání stanice B samo o sobě nesmí změnit hodnoty stanice A.

## 4. Referenční příklady

- Na A má host +2 hodinový díl a jeho hodinovou reprízu. Jiný host −1 má půlhodinu. A vykáže 150 přiřazených minut. Interní výpočet dá `(120×2 − 30)/150 = 1,4`; podle dvou původních dílů `(+2 − 1)/2 = 0,5`. Titulní index je v obou případech pod publikačním prahem.
- Stanice B odvysílá první hodinový díl jen jednou. B vykáže 60 minut, jeden původní díl a interní výsledek +2 (pod publikačním prahem). Stanice A má stále 150 minut a výsledek +1,4. Platí i při souběžné premiéře.
- Ve společném 40minutovém úseku je externí host +1 a interní expert s nehodnocenou osou. Celkem 40 minut, z toho 20 zařazených. Filtr externích ukáže 20 z 20 minut. Druhá role stejného hosta ani opakovaný import žádnou minutu nepřidá.
