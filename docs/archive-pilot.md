# ČRo Plus schedule pilot

Observed on 28 November 2026. Both samples cover Monday through Sunday. Every day returned a nonempty JSON schedule for Plus with timestamps on the requested Prague date.

| Week | Days returned | Schedule entries | Marked repeats | Entries without a show ID | Scheduled minutes recovered | Share of week |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 2–8 December 2024 | 7/7 | 612 | 179 | 157 | 9,747.23 | 96.7% |
| 16–22 November 2026 | 7/7 | 601 | 184 | 140 | 9,928.00 | 98.5% |

The denominator is 10,080 elapsed minutes per sampled week. Each numerator is the union of scheduled intervals clipped to the local day. The uncovered 332.77 and 152 minutes describe gaps in the published schedule. They could include junctions, short bulletins or rounding. Actual time off air cannot be inferred.

On 22 November 2026 the 09:00 bulletin runs until 09:07 and the following item begins at 09:05. Adding their durations would count two minutes twice. Several “Zprávy v půl” bulletins have an empty edition array. They remain valid slots. A schedule ID identifies an individual transmission. Its edition link identifies a show. Neither identifies a specific archive episode. [Inspect the source day](https://api.rozhlas.cz/data/v2/schedule/day/2026/11/22/plus.json).

## Reproduce

Run the import and export commands in the README for each date range. For each export, sum `slots`, `repeatSlots`, `missingShowId` and `coveredSeconds`; divide the last sum by 60 for minutes. Upstream schedules may be revised. [Earlier sample, first day](https://api.rozhlas.cz/data/v2/schedule/day/2024/12/02/plus.json) · [Recent sample, first day](https://api.rozhlas.cz/data/v2/schedule/day/2026/11/16/plus.json)

The episode and participant audit is still open. For each genre in these samples, measure the share of broadcasts with a confirmed episode, then compare a sample of the credited people and roles against the episode introduction. Inspect news blocks separately. The schedule coverage percentages above cannot establish guest coverage.
