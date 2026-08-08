---
type: workflow
lineage: imported
maturity: standard
---

# Enrichment Techniques

*A technique reference extending `workflows/enrichment.md`. That file says what to enrich and
in what order; this one is the mechanic's manual — how to run an enrichment platform cheaply,
how to wire in anything it doesn't natively do, and how to scrape the sources that aren't in
any database.*

Techniques here are platform-agnostic. Named tools are examples of a category, never a
requirement — "a data orchestration platform such as Clay" means any platform of that shape.

---

## 1. The cost model — four classes of action

Everything an orchestration platform does falls into one of four cost classes. Knowing which
class an action belongs to, before running it on ten thousand rows, is the whole game:

| Class | What it is | Cost |
|---|---|---|
| **Free normalizers** | Built-in formatting actions — normalize a URL, clean a company name | Free |
| **Free functions** | No-code logic and AI-assisted transforms — classify, extract, reformat, filter columns, derive a website from an email domain | Free |
| **Platform credits** | The platform's marketplace of integrations, metered per row at the platform's markup | The expensive path |
| **Your own API key** | The same underlying providers (or any provider), called directly with a key you hold | Provider's raw price |

**The decision rule: for any per-row action at volume, route through your own API key rather
than platform credits whenever both paths exist.** Credits are a convenience markup, and at
list scale the markup dominates the bill — an AI classification pass paid in credits can cost
one to two orders of magnitude more than the identical pass billed directly to an LLM
provider's API. The multiple changes as pricing changes; the direction has not. Do the
arithmetic (rows × per-row cost, both paths) before any run above a few hundred rows.

Where credits *are* reasonable: one-off runs, small tables, and integrations whose direct API
has no self-serve access.

---

## 2. The minimal-stack pattern

The corollary of the cost model: **a very small fixed stack covers the large majority of
enrichment tables without spending a credit.**

- **One LLM API key** — powers both plain AI prompts and the platform's agentic
  research/scraping actions
- **One contact-data API key** — a provider (such as Lead Magic) covering work-email finding,
  email validation, and person/company enrichment from a profile URL
- **The platform's free functions** — classification, keyword search, column filtering,
  format conversions

Before paying for any integration, ask in order: can a free function do this? Can an LLM
prompt over data already in the row do this? Can the contact-data key do this? Only then look
at the credit marketplace — and if the credit price is high, check section 3 first, because
the provider behind the integration may sell direct API access for less.

*Needs operator input:* the source material demonstrates its free-function recipes (keyword
finding, column filtering, email-domain-to-website) on video only; rebuild them from the
platform's current function library rather than from any written recipe here.

---

## 3. The generic HTTP request pattern

When an integration is missing from the platform's catalog, or present but credit-priced
beyond reason, it is not actually missing: **any documented HTTP API can become an enrichment
column** through the platform's generic HTTP request action.

This does not require knowing how to code. It requires three things:

1. **Read the provider's API documentation** — find the endpoint, the authentication header,
   and the request body it expects
2. **Map row fields into the request** — the platform substitutes column values into the URL
   or body per row
3. **Parse the response** — the platform unpacks the returned JSON into new columns; trial
   and error on a five-row test table gets the mapping right before the full run

Treat "the platform can't do X" as unverified until the HTTP pattern has been tried. If data
is openly reachable on the web or sold through any API, an orchestration platform can ingest
it.

---

## 4. The webhook intake pattern

The HTTP pattern *pulls*; a webhook *listens*. A webhook is not an enrichment — it is a
**source**: rows arrive whenever an external system fires.

Mechanics: create a new table whose source is a webhook column, copy the generated URL, and
paste it into the emitting platform's outbound-webhook setting. From then on, every event the
emitter fires becomes a row, and enrichment columns run on arrival.

Use it for any tool that observes events you want to sell against — the canonical category is
website-visitor de-anonymization (tools such as RB2B), which turns anonymous site traffic
into identified companies streamed straight into an enrichment table. The same pattern fits
form fills, product signups, and any SaaS with an outbound-webhook setting.

---

## 5. Scraping patterns

For the markets that live outside the standard B2B databases (`workflows/tam-campaign.md`,
Stage 1). Four patterns, in rising order of creativity.

### 5a. Niche directories

Sometimes the best lead source is not a data platform at all but a vertical directory that
already collects exactly the companies you need: licensing registries, association member
lists, review and ranking sites, marketplace seller indexes, franchise locators.

- **Finding the directory is the hard part** — it takes deliberate, deep search ("[niche] +
  directory / registry / member list / database") and accumulates as experience. Record every
  directory that works in the account's `context/signal-library.md` or source notes; the
  directory list is proprietary advantage.
- **Scraping it is the easy part** — point the platform's AI scraping agent at the listing
  pages and extract name, domain, and location per entry, then enrich normally.

### 5b. Maps platforms (local businesses)

Local businesses — restaurants, gyms, clinics, trades — are enumerated best on maps.
Two routes:

| Route | Tradeoff |
|---|---|
| The platform's native maps integration | Convenient, but typically credit-per-row and capped in rows per pull — expensive and truncated for whole-market mapping |
| A search API (providers such as SerperDev) called via the HTTP pattern | Far cheaper at volume, uncapped, but you assemble the workflow yourself |

The workable shape for the search-API route is a **location × keyword** setup: one table
holds the locations and search keywords as inputs; a second table receives one business per
row — name, address, phone, and website — and feeds enrichment. Changing market means
changing two input cells, not rebuilding.

*Needs operator input:* the source material ships this as a downloadable pre-built workbook;
the internal column wiring is not captured. Rebuild from the search API's documentation using
the HTTP pattern in section 3.

### 5c. News and feeds

Some buying moments are visible in the news before they are visible anywhere else — a new
location opening, a launch, an expansion — and the company in the article is in a buying
window for everything that moment requires.

The pipeline:

1. **Define the event query** — keyword plus geography ("new [business type] opening" +
   city), tuned to the moment when the target has the need but not yet the vendor
2. **Monitor news search results / feeds** for the query on a schedule
3. **Stream matches into an orchestration table** (webhook or scheduled pull)
4. **Extract and enrich per article** — an LLM pass pulls the company name and domain from
   the article text; standard enrichment finds the owner and contact data
5. **Route to the seller immediately** — the entire value is freshness; these leads decay in
   days, and the point is reaching them before competitors know they exist

This is a standing signal source, not a one-off list build — once running, it feeds
`playbooks/new-signal-response.md` continuously.

### 5d. Ad libraries

The major ad platforms publish searchable libraries of every active ad. Active paid
advertising is a strong observable signal — a company spending on ads is spending on growth —
and the ads themselves are free competitive intelligence:

- **Whether they advertise at all** — the growth-intent filter
- **What kind of ads** — lead generation vs. awareness says how they acquire
- **What offer and funnel** — the front-end offer and landing flow are visible in the
  creative

The three main libraries (Meta's, Google's, and LinkedIn's ad transparency pages) are all
public and all scrapeable, but each is structured differently and needs its own extraction
approach — budget per-library setup time rather than assuming one recipe transfers.

*Needs operator input:* the source material distributes its three per-library scraping tables
as downloads; the per-library mechanics are not captured in text. Build each against the
library's current page structure, using the AI scraping agent or the HTTP pattern.

---

## Where the numbers live

Per-row cost ceilings, batch sizes, monitoring cadences, and any coverage threshold that
gates a paid run are account values — `accounts/<slug>/context/scoring-model.md` or
`accounts/<slug>/ACCOUNT.md`. This file carries the reasoning (do the two-path arithmetic;
pay only for the residue the free path missed); the account carries the numbers. Provider
prices quoted nowhere, deliberately: they change, and the decision rules don't.

---

## Related

- `workflows/enrichment.md` — what to enrich, the waterfall order, and the quality gates
- `workflows/tam-campaign.md` — the market-mapping stage these scraping patterns serve
- `playbooks/new-signal-response.md` — what to do when a news/feed signal fires
- `docs/standards.md` — the verification standard every scraped fact must meet before it
  appears in copy
