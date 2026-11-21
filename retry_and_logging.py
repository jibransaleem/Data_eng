from prefect import task , flow , get_run_logger
from prefect.exceptions import FailedRun
CAUSE_ERROR  = True
@task(name = "process_data" , retries = 3 ,  retry_delay_seconds = [1,2,5])
def process_data():
    global CAUSE_ERROR
    logger = get_run_logger()
    logger.info("Processing the data ...")
    if CAUSE_ERROR:
        CAUSE_ERROR =False
        logger.error("Failed to run the task")
        raise FailedRun("failed to run the task ")
    logger.info("Proceed the data")

@flow(name = "dag")
def dag() :
    process_data()  
if __name__ == "__main__":
    dag()