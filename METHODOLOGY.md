# How SlantIndex calculates a station score

## Reading the index

For one station, period and axis, the index is the average score weighted by credited airtime. Here is a 30-day example for the economic axis.

| Guest | Credited airtime | Assessment |
|---|---:|---|
| A | 60 min | +1 |
| B | 20 min | −1 |
| C | 10 min | Reviewed. The sources conflict about the guest’s position. |
| D | 10 min | Awaiting review. |

- **Index +0.5.** A and B account for 80 scored minutes. The calculation is `(60 × 1 + 20 × (−1)) / 80 = +0.5`.
- **80% scored, 90% reviewed.** C counts toward review coverage. Only A and B contribute to the average. D counts toward neither percentage’s numerator. Both percentages use all 100 credited minutes as their denominator.
- **Episode-weighted index 0.** If each guest appeared in one episode first aired on this station during the period, A and B each get one vote. Their average is `(1 − 1) / 2 = 0`.
- **Missing-score range 0 to +0.8.** Assigning −2 to both C and D gives 0 across all 100 minutes. Assigning +2 to both gives +0.8. Exclude cases explicitly marked “axis does not apply” from this sensitivity calculation.

Alongside the index show the number of guests, the largest individual share of airtime, minutes at each score, reasons for missing scores and the estimated share of credited airtime. Report schedule and participant coverage separately. A segment with unknown guests or duration never entered the 100 credited minutes.

**When to publish a number.** For the selected station, axis, roles and window, require at least three distinct scored guests, ten scored guest–episode appearances first aired on that station in the window, and scores for at least 60% of credited minutes (or 60% of appearances in the episode view). Two guests in one episode count as two appearances. A repeat alone cannot meet the ten-appearance threshold. The example above would show counts, minutes and the reason the index is unavailable. Validate these proposed thresholds on pilot data.

## Counting broadcasts and roles

- **Roles.** The default includes external guests and external commentators. Later views cover staff commentary and presenting separately. Filter the underlying records before counting. If one person matches two roles, count them once per episode and credit each overlapping segment once per broadcast.
- **Interview.** A sole guest receives the whole interview, including questions. If two guests share 40 minutes and the split is unknown, credit each with 20 estimated minutes. Filtering for one guest preserves that guest’s share.
- **Magazine show.** Credit only the guest’s segment. Leave it unassigned if duration or the participant list is unknown. Prefer actual broadcast timing. Mark durations taken from the schedule or a matching archive edit as estimates.
- **Repeat.** Credit airtime again using the original episode’s role and applicable score, usually as of its premiere. For an edited repeat count only the retained segments. A March premiere on Plus repeated on Plus in November contributes November minutes, zero November original appearances and zero toward November’s ten-appearance threshold. If November is its first broadcast on another station, it counts once there. Flag syndicated episodes and unknown first-air dates. Unverified first broadcasts contribute no original-episode count.
- **Window.** End the chart on the last complete day in Europe/Prague. Measure elapsed time in UTC seconds and display minutes. Clip broadcasts to the window and merge duplicate or overlapping records for the same airtime. A rolling 90-day show chart needs 89 days of history before its first plotted date.
- **Station comparisons.** Count a simulcast on each station that aired it. Compare matching periods, windows, filters and methodology. Mark archive gaps on the chart.

## Scoring a public position

Score the economic and cultural axes independently. Start with profiles that account for the most unscored airtime on that axis. Each published score needs a reason, an exact quotation, author, date, link and page or timestamp where available. Check contrary evidence. Use the person’s public statements or endorsed proposals and the institution’s official positions. Record confidence separately.

| Score | Economic axis | Cultural axis |
|---|---|---|
| −2 | Broad cuts to taxation, public spending and redistribution | Enforcing traditional rules in law across several areas of life |
| −1 | A limited reduction in overall taxation or redistribution | Preserving or tightening traditional rules in one area |
| 0 | Documented middle position on taxation or redistribution | Documented middle position on cultural policy |
| +1 | A limited increase in overall taxation or redistribution | Expanding rights or personal choice in one area |
| +2 | A substantial increase in overall taxation and redistribution | Broad expansion of choice and equal rights across several areas |

**Zero requires positive evidence.** A published proposal to keep the overall tax burden and redistribution steady can support 0 even if it shifts taxes between sources. Two conflicting accounts of whether the guest wants overall taxes raised or cut leave the position **disputed** until an editor can resolve them. Opposite statements alone do not average to zero. Other unscored statuses are **awaiting review**, **insufficient evidence** and **axis does not apply**.

**Two examples of proposed scores**

- **PAQ Research, economic +1.** The joint reform proposes lower taxes on labour and higher total revenue. The authors estimate “o 73 mld. Kč navíc vůči roku 2024” (CZK 73 billion more than in 2024). This supports a positive economic score for this proposal. An institutional profile also considers other evidence. [PAQ Research, Centre for Public Finance and IDEA, *Chytřejší daně*, 2025, p. 50](https://chytrejsidane.cz/Studie_Chytrejsi_dane.pdf#page=51)
- **Jsme fér, cultural +1.** Its call for “MANŽELSTVÍ PRO VŠECHNY PÁRY” (marriage for all couples) advocates extending one specific right. [Jsme fér, campaign homepage](https://www.jsmefer.cz/)

Party positions follow the same evidence rule. Editors may consult the Chapel Hill Expert Survey for context. A survey rating alone cannot establish a SlantIndex score. The first scoring release uses cited policy evidence for each party, so it requires neither a numerical conversion nor a current survey entry for every party. [CHES Europe](https://www.chesdata.eu/ches-europe/)

## Whose score applies?

- **Politician.** On each axis, use an explicitly approved, publishable personal score applicable when the episode was made. Otherwise use the published score of the party represented at that time, including for a minister. A minister with personal economic score −1 and only a party cultural score of +1 contributes −1 and +1 respectively. If neither a publishable personal score nor a documented party with a published score is available on an axis, leave that axis unscored.
- **Other guest.** Use the institution’s score when the guest represents it and the guest’s publishable personal score when speaking independently. Treat an introduction as an economist for a named institute as institutional representation unless the guest explicitly speaks in a personal capacity. Save the episode reference. A job listed only in a biography is insufficient.
- **Missing or private score.** Leave the axis unscored if the selected source lacks a publishable score or the role is unclear. A 20-minute interview for an institution scored +1 only on economics yields 20 minutes at +1 on economics and 20 unscored cultural minutes. Publish the credited time, role, applied score or status, profile source and episode reference for each contribution so readers can reproduce the result.

## When history changes

- **Better evidence.** Usually one score per axis suffices. If evidence found in November supports +2 since March where we previously used +1, recalculate the affected appearances and repeats. Log the old and new scores, applicable period, citation, reason, editor and revision date.
- **Change of institution.** Record representation per appearance. A repeat of a guest’s interview for institute A still belongs to A after the guest joins B.
- **Change of position.** Introduce separate periods on an axis only when a change is documented. Earlier episodes keep the score applicable when they were made.
