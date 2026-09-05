# Google Ads Transparency Center scraper

## What this repository helps you do

Search public Google Ads Transparency Center creatives by website domain, advertiser name, or advertiser ID. Filter by platform, format, country, and dates, then inspect deduplicated ad records in JSON or CSV.

## Example result

The [sample dataset](data/sample-output.json) contains advertiser and creative IDs, active dates, ad URLs, the matched domain, and optional preview enrichment. The [CSV sample](data/sample-output.csv) can be opened directly in a spreadsheet.

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

See [`examples/python/search_creatives.py`](examples/python/search_creatives.py).

### JavaScript

See [`examples/javascript/request.mjs`](examples/javascript/request.mjs).

## Output fields

Each Dataset item may include advertiser and creative IDs, advertiser name, ad format, first and last shown dates, approximate days shown, ad and preview URLs, matched domain, original search query, scrape timestamp, and optional `previewFetched`, `previewText`, and `previewAssetUrls` fields.

## Common use cases

- Build a dated creative reference library for campaign research.
- Compare public ad activity across advertisers, platforms, and countries.
- Monitor creative formats and publication dates used by competitors.
- Export ad records for downstream analysis in Python or spreadsheets.

## Export Google Ads Transparency Center creatives to CSV

Run the Actor with `data/sample-input.json`, open the Dataset, and choose CSV export. The same workflow is available through the API examples, which let scheduled jobs save the returned items into a data pipeline.

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
