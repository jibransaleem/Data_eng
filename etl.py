
from prefect import flow, task
import time

@task(name="load_data")
def load_data(url):
    print("Loading data from:", url)
    time.sleep(5)
    print("Loaded")
    return "data loaded"


@task(name="normalize_data")
def normalize_data(data):
    print("Normalizing the data...")
    time.sleep(10)
    print("Normalized")
    return "data-normalized"


@task(name="fill_missing_values")
def fill_missing_values(data):
    print("Filling missing values...")
    time.sleep(4)
    print("Done filling")
    return "filled missing values"


@flow(name="dummy-etl")
def dummy_etl(url: str):

    loaded_data = load_data(url)

    # Execute these two tasks concurrently
    norm = normalize_data.submit(loaded_data)
    cleaned = fill_missing_values.submit(loaded_data)

    # Collect results
    return loaded_data + norm.result() + cleaned.result()


if __name__ == "__main__":
    dummy_etl("https://github.com/jibransaleem.git")
