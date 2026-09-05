import os

from apify_client import ApifyClient


def main() -> None:
    client = ApifyClient(os.environ["APIFY_API_TOKEN"])
    for search_query in ["nike.com", "adidas.com"]:
        run = client.actor("datascraperes/google-ads-transparency-scraper").call(
            run_input={"searchQuery": search_query, "maxResults": 3}
        )
        for item in client.dataset(run["defaultDatasetId"]).iterate_items():
            print(item)


if __name__ == "__main__":
    main()
