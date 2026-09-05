# Google Ads Transparency Center scraper

Run the hosted [Google Ads Transparency Scraper on Apify](https://apify.com/datascraperes/google-ads-transparency-scraper?fpr=edudata) without writing scraping code, or integrate it with Python, JavaScript, or cURL to collect structured public advertiser creatives.

[Browse the technical examples and sample Dataset](https://github.com/datacrawler-edu/google-ads-transparency-scraper-examples)

This repository contains executable API examples, verified sample input, realistic Dataset output, and a CSV export. It documents the public integration surface without exposing the Actor's private implementation, proxy configuration, or credentials.

## What this repository helps you do

- Search public Google Ads Transparency Center creatives by website domain, advertiser name, or advertiser ID.
- Filter by Google platform, ad format, country, and inclusive date range.
- Inspect deduplicated advertiser/creative records with IDs, active dates, and public URLs.
- Optionally enrich selected creatives with observable preview text and asset URLs.
- Export results to JSON or CSV for research and reporting.

## Example result

The complete verified sample is available in [`data/sample-output.json`](data/sample-output.json), with the same fields in [`data/sample-output.csv`](data/sample-output.csv).

```json
{
  "advertiserId": "AR16832577870747402241",
  "advertiserName": "NIKE GLOBAL TRADING B.V. SINGAPORE BRANCH",
  "creativeId": "CR05650980632755437569",
  "adFormat": "text",
  "firstShown": "2026-09-03",
  "lastShown": "2026-09-05",
  "approxDaysShown": 3,
  "matchedDomain": "nike.com",
  "previewFetched": true
}
```

The fixture proves the output contract; public advertising records and preview availability can change over time.

## Run without code

Open the [hosted Actor](https://apify.com/datascraperes/google-ads-transparency-scraper?fpr=edudata), enter a domain such as `nike.com` in **Website, advertiser name or ID**, adjust filters if needed, and click **Start**. Open the **Dataset** tab when the run finishes to inspect rows or export JSON and CSV.

## Try it with Apify's free plan

Apify currently includes $5 of monthly prepaid usage for new and eligible users. Check the [current pricing details](https://apify.com/pricing?fpr=edudata) before running a large search.

## Quick start for developers

### Python

#### 1. Install the client

```bash
pip install -r examples/python/requirements.txt
```

#### 2. Set your Apify token

Set `APIFY_API_TOKEN` to a token from your Apify account.

#### 3. Run the example

```bash
python examples/python/search_creatives.py
```

## Input example

The complete tested payload is in [`data/sample-input.json`](data/sample-input.json). `searchQuery` accepts a domain, website URL, advertiser name, or advertiser ID. `maxResults` limits unique creatives; `includeDetails` enables optional preview enrichment.

## Request examples

### cURL

See [`examples/curl-request.md`](examples/curl-request.md).

### Python

[`examples/python/search_creatives.py`](examples/python/search_creatives.py) runs the sample input. [`examples/python/batch_search_creatives.py`](examples/python/batch_search_creatives.py) runs separate searches for multiple domains, and [`examples/python/export_ads_csv.py`](examples/python/export_ads_csv.py) converts the checked-in sample output to CSV.

### JavaScript

See [`examples/javascript/request.mjs`](examples/javascript/request.mjs).

## Output fields

| Field | Meaning |
| --- | --- |
| `advertiserId` | Public Google advertiser identifier. |
| `advertiserName` | Public advertiser name when available. |
| `creativeId` | Public creative identifier. |
| `adFormat` | Creative format returned by the source. |
| `firstShown`, `lastShown` | Inclusive dates observed by the source. |
| `approxDaysShown` | Approximate number of days shown. |
| `adUrl`, `previewUrl` | Public creative or preview URLs. |
| `matchedDomain` | Domain used to match the result. |
| `previewFetched`, `previewText`, `previewAssetUrls` | Optional enrichment fields when preview retrieval returns usable data. |

The Actor also writes a run-level `SUMMARY` record to the default Key-Value Store. See [`docs/output-reference.md`](docs/output-reference.md).

## Common use cases

- Build a dated creative reference library for campaign research.
- Compare public ad activity across advertisers, platforms, and countries.
- Monitor creative formats and publication dates used by competitors.
- Export ad records for downstream analysis in Python or spreadsheets.

## Export Google Ads Transparency Center creatives to CSV

Use [`examples/python/export_ads_csv.py`](examples/python/export_ads_csv.py) for the checked-in sample, or run the Actor and export its Dataset as CSV from Apify Console. The same workflow is available through the API examples for scheduled data pipelines.

## Find advertiser ads by domain and date

Set `searchQuery` to a domain such as `nike.com` and use `dateFrom`, `dateTo`, `region`, and `platform` to narrow the public creative records returned by the Actor.

## FAQ

See [`docs/faq.md`](docs/faq.md) for answers about filters, empty results, enrichment, and limits.

## Limits and pricing

The Actor charges for successful `ad-result` events and charges the optional `ad-enrichment` event only when enrichment returns usable data. Tier pricing is configured in Apify; the current public configuration is approximately $0.75-$1.00 per 1,000 events depending on tier. Review the Actor's Pricing tab before large runs.

## Hosted version

Use the [Google Ads Transparency Scraper on Apify](https://apify.com/datascraperes/google-ads-transparency-scraper?fpr=edudata) to run it without maintaining infrastructure.

## Responsible use

Use only public data, respect applicable law and the Google Ads Transparency Center terms, and avoid collecting or inferring sensitive personal information. Apply the filters and limits needed for your use case.

## Support

Open an [issue](https://github.com/datacrawler-edu/google-ads-transparency-scraper-examples/issues) for problems with these examples, or use the [Actor support page](https://apify.com/datascraperes/google-ads-transparency-scraper?fpr=edudata).

## License

MIT. See [`LICENSE`](LICENSE).
