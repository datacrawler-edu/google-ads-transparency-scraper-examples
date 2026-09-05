import json
import os
from pathlib import Path

from apify_client import ApifyClient


def main() -> None:
    token = os.environ["APIFY_API_TOKEN"]
    input_path = Path(__file__).parents[2] / "data" / "sample-input.json"
    run_input = json.loads(input_path.read_text(encoding="utf-8"))
    client = ApifyClient(token)
    run = client.actor("datascraperes/google-ads-transparency-scraper").call(run_input=run_input)
    for item in client.dataset(run["defaultDatasetId"]).iterate_items():
        print(json.dumps(item, ensure_ascii=False))


if __name__ == "__main__":
    main()
