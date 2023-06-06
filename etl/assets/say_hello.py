from dagster import asset

@asset
def hello_asset():
    return [1, 2, 3]