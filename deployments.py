from prefect import task , flow , get_run_logger
from prefect.exceptions import FailedRun
@task(name = "process_data" , retries = 3 ,  retry_delay_seconds = [1,2,5])
def process_data():
    global CAUSE_ERROR
    logger = get_run_logger()
    logger.info("Processing the data ...")
    logger.info("Proceed the data")

@flow(name = "dag")
def dag() :
    process_data()  
if __name__ == "__main__":
    dag()