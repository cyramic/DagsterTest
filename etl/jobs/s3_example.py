from dagster import job
from dagster_aws.s3 import s3_resource
from etl.ops.s3_test import s3_test_op


@job(resource_defs={'s3': s3_resource})
def example_job():
    s3_test_op()


example_job.execute_in_process(
    run_config={
        'resources': {
            's3': {
                'config': {
                    'region_name': 'eu-west-2',
                }
            }
        }
    }
)