# Jak SlantIndex počítá výsledky

## Jak číst index stanice

Index je průměrné skóre hostů vážené jejich vysílacím časem. Počítáme ho zvlášť pro každou stanici, období a osu. Příklad pro ekonomickou osu za 30 dní:

| Host | Čas | Výsledek hodnocení |
|---|---:|---|
| A | 60 min | +1 |
| B | 20 min | −1 |
| C | 10 min | Podklady jsme prošli, ale odporují si. |
| D | 10 min | Podklady jsme ještě neprošli. |

- **Index +0,5.** Skóre známe u A a B. Výpočet je `(60 × 1 + 20 × (−1)) / 80 = +0,5`. A měl třikrát více času než B, proto má trojnásobnou váhu.
- **Zařazeno 80 %.** Ze 100 minut přiřazených hostům má 80 minut známé skóre. Zbývajících 20 minut do průměru nevstoupí.
- **Zkontrolováno 90 %.** Prošli jsme podklady k A, B i C. Zbývá prověřit D.
- **Podle počtu dílů vyjde 0**, pokud každý host vystoupil v jednom původním dílu. A i B pak mají stejnou váhu: `(1 − 1) / 2 = 0`. Čtenář tak vidí rozdíl mezi počtem pozvání a délkou prostoru.

Vedle průměru zobrazíme minuty v každém stupni škály, důvody nezařazení a podíl odhadnutého času. Rozhovor, u kterého neznáme hosta nebo délku, mezi těmi 100 minutami vůbec není. Zvlášť proto uvedeme, kolik programu jsme dohledali a u kolika dílů známe obsazení.

**Kdy ukázat číslo.** Navržené minimum pro zvolenou osu jsou tři různé osoby se známým skóre, 10 různých zařazených dvojic osoba–původní díl a alespoň 60 % zařazené váhy (minut nebo vystoupení podle zvoleného pohledu). Repríza další dvojici nevytváří. Malý příklad výše vysvětluje výpočet. Na webu by se u něj zobrazily jen minuty, počty a důvod chybějícího indexu. Hranice ověříme na skutečných datech.

**Jak moc záleží na chybějících skóre?** V příkladu by při skóre −2 u C i D vyšel index 0. Při +2 u obou by vyšel +0,8. Tak zobrazíme možné rozpětí. Čas výslovně označený „osa se netýká“ do tohoto odhadu nevstupuje.

## Jak započítáme vysílací čas

- **Rozhovor.** Jedinému hostovi připadne celý rozhovor včetně otázek. Pokud dva hosté společně diskutují 40 minut a přesnější rozdělení neznáme, připíšeme každému 20 minut a označíme odhad. Filtr jednoho hosta jeho podíl nezvětší. Moderování sledujeme zvlášť. Dvě role téže osoby ve stejném úseku jí další čas nepřidají.
- **Magazín.** Započítáme jen úsek věnovaný hostovi. Bez doložené délky nebo při neúplném obsazení zůstane úsek nepřiřazený. Přednost má skutečný čas odvysílání. Délku převzatou z programu či shodné archivní verze označíme jako odhad.
- **Repríza.** Přičteme znovu odvysílané minuty. U sestřihu pouze zachované úseky. Použijeme roli a hodnocení platné při vzniku dílu, obvykle k datu premiéry. V počtech dílů se host započítá jednou při prvním vysílání dílu na dané stanici. Převzatý díl a neznámé datum prvního vysílání označíme zvlášť.
- **Období.** Graf končí posledním uzavřeným dnem v pásmu Praha. Čas měříme v sekundách podle UTC a zobrazujeme v minutách. Z pořadu na hranici období patří do výsledku jen příslušná část. Překrývající se záznamy sloučíme. Pro 90denní přehled pořadu načteme i 89 dní před začátkem grafu.
- **Další stanice.** Společné vysílání si každá započítá do vlastního přehledu. Při porovnání použijeme stejné období, délku okna, filtry a metodiku. Mezeru v archivu vyznačíme v grafu.

## Jak vznikne názorový profil

Osoba a instituce mají samostatné karty. Každá karta má dvě hodnocení:

| Skóre | Ekonomická osa | Kulturní osa |
|---|---|---|
| −2 | Rozsáhlé snížení daní, výdajů státu a přerozdělování | Prosazování tradičních pravidel zákonem napříč oblastmi života |
| −1 | Dílčí snížení celkového zdanění nebo přerozdělování | Zachování či zpřísnění tradičních pravidel v konkrétní oblasti |
| 0 | Doložený střed nebo kombinace opačných postojů | Doložený střed nebo kombinace opačných postojů |
| +1 | Dílčí zvýšení celkového zdanění nebo přerozdělování | Rozšíření práv či osobní volby v konkrétní oblasti |
| +2 | Výrazné zvýšení celkového zdanění a přerozdělování | Široké rozšíření osobní volby a rovných práv napříč oblastmi |

Nejdřív hodnotíme profily s nejvíce vysílacími minutami. U osoby vycházíme z jejích vlastních slov a veřejně podpořených návrhů. U instituce z oficiálních stanovisek a programů. Posoudíme i doklady, které navrženému skóre odporují. **Každé skóre musí mít důvod a přesnou citaci** s autorem, datem, odkazem a podle zdroje i stranou nebo časem v nahrávce.

Dokud skóre nelze určit, uvedeme důvod: zatím nehodnoceno, málo důkazů, sporné podklady nebo osa se netýká. Nulu použijeme jen pro doložený střed či smíšený postoj. U hodnocení evidujeme míru jistoty. U změny zaznamenáme původní hodnotu, kdo změnu schválil, proč a odkdy platí.

**Dva příklady zařazení podle konkrétního dokladu:**

- **PAQ Research, ekonomika, návrh +1.** Doporučená reforma ulevuje části pracujících, ale celkový výběr zvyšuje. Autoři píší: „Navrhovaná reforma by mohla vybrat do veřejných rozpočtů o 73 mld. Kč navíc vůči roku 2024.“ To dokládá dílčí zvýšení celkového zdanění. [PAQ Research, Centrum veřejných financí a IDEA, *Chytřejší daně*, 2025, s. 50](https://chytrejsidane.cz/Studie_Chytrejsi_dane.pdf#page=51)
- **Jsme fér, kultura, návrh +1.** Výzva „JE ČAS NA MANŽELSTVÍ PRO VŠECHNY PÁRY“ dokládá požadavek rozšířit jedno konkrétní právo. [Jsme fér, úvodní výzva, ověřeno 28. 11. 2026](https://www.jsmefer.cz/)

U stran lze využít [expertní průzkum CHES](https://www.chesdata.eu/ches-europe/). Jeho ekonomická (LRECON) a kulturní (GALTAN) škála mají vůči našim opačný směr. Obě převádíme podle `2 − 0,4 × původní hodnota`. Zaokrouhlujeme na celé číslo, poloviny od nuly. Hodnotám 0, 5 a 10 tedy odpovídá +2, 0 a −2. Uložíme i původní hodnotu a ročník průzkumu.

### Čí skóre použít u hosta

**Host zastupuje instituci:** použijeme její skóre, i kdyby měl jiné osobní skóre. Stačí, že ho pořad představí například jako „ekonoma PAQ Research“. Uložíme odkaz na toto představení. Údaj o zaměstnavateli nalezený jen v životopisu zastupování nedokládá.

**Host mluví za sebe:** použijeme jeho vlastní schválené skóre. Pokud výslovně uvede, že mluví za sebe, má to přednost před představením jeho zaměstnavatele.

**Chybí skóre nebo je role nejasná:** minuty vykážeme jako nezařazené pro příslušnou osu. Například 20 minut zástupce instituce s ekonomickým skóre +1 a nehodnocenou kulturou znamená 20 minut s +1 v ekonomice a 20 nezařazených minut v kultuře.
