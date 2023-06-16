from dagster import op
from decouple import config

BUCKET = config('AWS_S3_BUCKET')
KEY = "SSDA903_2020_episodes.csv"


@op(required_resource_keys={'s3'})
def s3_test_op(context):
    return context.resources.s3.list_objects_v2(
        Bucket=BUCKET,
        Prefix=KEY
    )
