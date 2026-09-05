import csv
import json
from pathlib import Path


def main() -> None:
    root = Path(__file__).parents[2]
    rows = json.loads((root / "data" / "sample-output.json").read_text(encoding="utf-8"))
    output_path = root / "data" / "exported-ads.csv"
    fieldnames = list(rows[0]) if rows else []
    with output_path.open("w", newline="", encoding="utf-8") as output:
        writer = csv.DictWriter(output, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {len(rows)} rows to {output_path}")


if __name__ == "__main__":
    main()
