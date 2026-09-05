# cURL request

```bash
curl -X POST "https://api.apify.com/v2/acts/datascraperes~google-ads-transparency-scraper/runs?token=$APIFY_API_TOKEN" \
  -H "Content-Type: application/json" \
  --data @data/sample-input.json
```

Use the returned run dataset ID to read the results through the Apify API.
