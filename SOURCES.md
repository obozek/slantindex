# Broadcast sources and import

| Source | What it establishes |
|---|---|
| [Czech Radio schedule](https://program.rozhlas.cz/program/html) | The planned station, time, show and sometimes participants. Schedules can change. |
| [mujRozhlas episode archive](https://api.mujrozhlas.cz/episodes) | Show and episode IDs, descriptions, times and available recordings. A show’s station label alone cannot confirm a particular broadcast. |
| Episode page or recording | Who appeared, their role, whom they represented and sometimes the length of their segment. An article byline establishes authorship of the text. |

## Import

1. **Read the full schedule.** `import --station cro-plus --from YYYY-MM-DD --to YYYY-MM-DD` includes both dates. The importer records progress and errors per day, refreshes the last seven days for corrections and can rerun any older range.
2. **Match each broadcast to an episode.** Use an ID or link first. Otherwise compare show, time, duration and description, accepting only a unique match. Look before the requested window for a repeat’s first broadcast. Flag edits, ambiguous matches and unknown first-air dates.
3. **Record participants and roles.** Use structured credits first. Czech cues such as *hostem je* (“the guest is”) and *moderuje* (“hosted by”) help distinguish guests and presenters. Keep the passage and link for each assignment. An editor resolves ambiguous credits. Store genre on the show. For each appearance record the on-air role and the person’s capacity at the time, such as outside expert, staff journalist or politician. For politicians, record the party represented and government or opposition status where documented. Leave unknowns open.
4. **Keep enough to replay the import.** Store each distinct response privately with URL, retrieval time, HTTP status, content hash and parser version, subject to the retention policy. Use conditional requests, bounded concurrency and `Retry-After`. Check terms of use before bulk retrieval. Keep editorial corrections separately with a reason and source. They take precedence on rebuild and survive re-import.
5. **Measure coverage.** By station and genre, report schedule days and minutes recovered, broadcasts matched, episodes with known participants and durations estimated. Report rolling news blocks separately. Test on saved fixtures and investigate sudden drops before release.

The first release can extract explicit credits without a language model. Where a model proposes names from free text, an editor verifies the passage and role. From the first **scoring** release, a language model drafts a score or an unscored status for each axis, with its reasoning and exact source passages. An editor verifies the evidence, then accepts, changes or rejects the proposal. Store the input hash, model, prompt version, sources, confidence and editorial decision. Evaluate each model-assisted task on manually checked examples before using its output.

## Pilot checks

- **Two guests and a repeat.** The episode description names both guests and mentions an earlier premiere. Expect two appearances in one original episode and a separate broadcast for the repeat. [Pro a proti](https://plus.rozhlas.cz/dan-ze-slazenych-napoju-snizi-obezitu-soudi-ekonom-napoje-za-nemuzou-mini-9324188)
- **Guest versus article author.** The introduction on 25 November 2026 names Daniel Prokop. Three people signed the article. Use the introduction for the guest credit and the Plus schedule to verify whether this station aired it. [Život k nezaplacení](https://radiozurnal.rozhlas.cz/danime-praci-ale-majetek-temer-vubec-cesko-je-v-tom-vyjimecne-rika-sociolog-9658893)
- **Archive coverage.** Compare every Plus show in the last complete week and one week near the start of the two-year history. Report missing episodes, incorrect identities and timing errors by genre. The pilot is pending.

For another Czech Radio station, try the same import with its station ID. For a different broadcaster, check one episode against its schedule before adapting the importer. Radio Prostor lists broadcast slots. Guest segment lengths and historical archive coverage still need verification. After adding a station, verify that the Plus results are unchanged. [Radio Prostor schedule](https://www.radioprostor.cz/program)
