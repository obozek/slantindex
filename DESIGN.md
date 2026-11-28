# SlantIndex

SlantIndex shows who gets airtime on Czech Radio Plus (ČRo Plus) and the publicly documented economic and cultural positions associated with those appearances. Readers can trace a station score back to the broadcasts, the people or institutions scored, and the evidence. The index describes the selection of voices. It does not measure what a guest said in a particular interview or how the interviewer treated them.

## Release plan

1. **Who appeared?** Cover every show on Plus over the last 30 complete days. Show names, roles, episode counts and source links. Mark gaps in the schedule and unknown guests. The first implementation PR includes the SQLite migration, parser fixtures and a two-week archive check. Importing identical data twice must preserve counts and manual corrections.
2. **How much airtime?** Add minutes for each broadcast, including repeats. A one-hour interview with one guest aired twice gives that guest 120 minutes and one original episode.
3. **Which positions received airtime?** Add the two station scores, evidence-backed profiles and a reader correction form. Each scored appearance identifies whose score it uses. [Scoring methodology](METHODOLOGY.md)
4. **How has the mix changed?** Extend coverage month by month to two years. Show a 30-day station trend and 90-day show trends. Add views by journalist, person and institution at this stage. A journalist’s guest list and their own on-air commentary answer different questions and appear separately.

## Data flow

Python imports the schedule, episodes, broadcasts and participants into SQLite. Each broadcast carries a station ID so another station can reuse the calculations. Astro builds the static site on Cloudflare. Role filters work from individual appearances and credited segments, so a guest with two selected roles counts once per episode. Overlapping minutes for that guest count once per broadcast. [Sources and import](SOURCES.md)

When the correction form launches, a Cloudflare Worker will validate and rate-limit submissions and store them privately in D1. An editor applies accepted corrections to the source SQLite database and rebuilds affected pages.

## Publication and corrections

- Before importing real personal data, document the purpose, lawful basis and retention for the fields collected. Before publishing the first named listing, publish a privacy notice and a working contact for corrections or removal. An email address is enough for the first release.
- Before recording or inferring political opinions about identifiable people, including sending identifiable material to a model for scoring, document the applicable legal basis and the conditions for that processing in `PRIVACY.md`. Development of the importer and scoring logic can use synthetic fixtures while that assessment is open. [GDPR, Articles 6 and 9](https://eur-lex.europa.eu/eli/reg/2016/679/)
- Publish institutional and party profiles with their sources. Assess personal profiles of politicians and other public officials individually. For other guests, the default is a sourced appearance record. Any institutional score shown belongs to the named institution. Every score used in a public index must be public and traceable.
- On withdrawal, remove the affected personal data from public pages, history, exports and earlier releases under our control. Rebuild the affected figures using the remaining publishable evidence. The notice explains how to request this and how long we keep submissions.
