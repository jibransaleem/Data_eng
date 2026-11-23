# """Module 1: download one month of NYC TLC data, sample it, save it."""

import argparse
import logging
from pathlib import Path

import pandas as pd
import requests

# # Check the TLC Trip Record Data page if this URL pattern ever changes.
# BASE_URL = "https://d37ci6vzurychx.cloudfront.net/trip-data"
RAW_DIR = Path("./data/raw")
# SAMPLE_SIZE = 200_000
# SEED = 42
# df = pd.read_parquet(RAW_DIR/"yellow_2024-01.parquet")
# print(df.head())
# logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
# log = logging.getLogger(__name__)


# def output_path(year: int, month: int, raw_dir: Path = RAW_DIR) -> Path:
#     return raw_dir / f"yellow_{year}-{month:02d}.parquet"


# def _download(url: str, dest: Path) -> None:
#     """Stream a file to disk."""
#     with requests.get(url, stream=True, timeout=60) as r:
#         r.raise_for_status()
#         with open(dest, "wb") as f:
#             for chunk in r.iter_content(chunk_size=1 << 20):
#                 f.write(chunk)


# def download_month(
#     year: int,
#     month: int,
#     raw_dir: Path = RAW_DIR,
#     sample_size: int = SAMPLE_SIZE,
#     seed: int = SEED,
#     force: bool = False,
# ) -> Path:
#     """Download one month, sample it reproducibly, write a single Parquet file.

#     Idempotent: if the output already exists, nothing happens (unless force=True).
#     """
#     raw_dir.mkdir(parents=True, exist_ok=True)
#     out = output_path(year, month, raw_dir)

#     if out.exists() and not force:
#         log.info("Already exists, skipping: %s", out)
#         return out

#     url = f"{BASE_URL}/yellow_tripdata_{year}-{month:02d}.parquet"
#     full_tmp = raw_dir / f".full_{year}-{month:02d}.parquet.tmp"
#     sample_tmp = raw_dir / f".sample_{year}-{month:02d}.parquet.tmp"

#     try:
#         log.info("Downloading %s", url)
#         _download(url, full_tmp)

#         df = pd.read_parquet(full_tmp)
#         n_full = len(df)
#         if n_full > sample_size:
#             df = df.sample(n=sample_size, random_state=seed)
#         # Sort so the output order is deterministic.
#         df = df.sort_values("tpep_pickup_datetime").reset_index(drop=True)

#         # Write to a temp file, then rename, so a crash never leaves a half-written file.
#         df.to_parquet(sample_tmp, index=False)
#         sample_tmp.replace(out)
#         log.info("Saved %d of %d rows to %s", len(df), n_full, out)
#     finally:
#         full_tmp.unlink(missing_ok=True)
#         sample_tmp.unlink(missing_ok=True)

#     return out


# if __name__ == "__main__":
#     p = argparse.ArgumentParser()
#     p.add_argument("--year", type=int, required=True)
#     p.add_argument("--month", type=int, required=True)
#     p.add_argument("--sample-size", type=int, default=SAMPLE_SIZE)
#     p.add_argument("--force", action="store_true")
#     a = p.parse_args()
#     download_month(a.year, a.month, sample_size=a.sample_size, force=a.force)