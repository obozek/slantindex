# SlantIndex

SlantIndex studies who gets airtime on Czech Radio Plus. The first working slice measures schedule coverage. It imports planned broadcasts into SQLite, precomputes daily counts and renders a static site for Cloudflare.

[Architecture](ARCHITECTURE.md) · [Product design](DESIGN.md) · [Archive pilot](docs/archive-pilot.md) · [Methodology](METHODOLOGY.md)

## Run a synthetic example

Use Python 3.11+ with the IANA timezone database, Node.js 24 and npm. Run from the repository root.

```sh
python3 -m unittest discover -s tests -v
python3 -m slantindex --db build/demo.sqlite import --fixtures tests/fixtures --from 2026-11-22 --to 2026-11-22
python3 -m slantindex --db build/demo.sqlite export --from 2026-11-16 --to 2026-11-22 --out site/src/generated/schedule.json
cd site
npm install
npm run build
npm run preview
```

The fixture yields three slots, one scheduled repeat and 45 covered minutes on 22 November. The six preceding days are marked missing. The sample label appears on every build containing fixture data.

## Import the Plus schedule

The command below bootstraps a real 30-day window in a separate database. Both dates are inclusive.

```sh
python3 -m slantindex import --station cro-plus --from 2026-10-29 --to 2026-11-27
python3 -m slantindex export --from 2026-10-29 --to 2026-11-27 --out site/src/generated/schedule.json
```

For subsequent runs, `python3 -m slantindex import` refreshes the last seven complete Prague days. An export without date arguments covers the last 30. Use the exit status to gate publication. Re-run a failed range to retry it. The source API can revise old dates.

## Publish to Cloudflare

Run the Astro build after generating the desired export. Inspect the HTML and its linked JSON using `npm run preview`. From `site/`, an authenticated Cloudflare CLI can publish the finished directory with `cf deploy ./dist`. The project name is `slantindex`. CI builds and checks the fixture site. Production publication is a separate operation. [Cloudflare deployment reference](https://developers.cloudflare.com/cf/projects/#deploy-a-static-assets-directory)
