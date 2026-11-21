
from prefect import flow, task
import time


# TASK 1: EXTRACT
@task(name="extract_data")
def extract_data(source):
    print(f"Extracting customer and order data from source {source}...")
    time.sleep(3)

    return {
        "customers": ["Jibran", "Ali", "Ahmed"],
        "orders": [100, 200, 300]
    }


# TASK 2: VALIDATE
@task(name="validate_data")
def validate_data(data):
    print("Validating extracted data...")
    time.sleep(2)

    if not data["customers"] or not data["orders"]:
        raise ValueError("Invalid data")

    return data


# TASK 3: CLEAN CUSTOMERS
@task(name="clean_customers")
def clean_customers(data):
    print("Cleaning customer records...")
    time.sleep(4)

    return [name.upper() for name in data["customers"]]


# TASK 4: CLEAN ORDERS
@task(name="clean_orders")
def clean_orders(data):
    print("Cleaning order records...")
    time.sleep(5)

    return data["orders"]


# TASK 5: TRANSFORM CUSTOMERS
@task(name="transform_customers")
def transform_customers(customers):
    print("Transforming customer data...")
    time.sleep(3)

    return customers


# TASK 6: TRANSFORM ORDERS
@task(name="transform_orders")
def transform_orders(orders):
    print("Transforming order data...")
    time.sleep(4)

    return [amount * 1.10 for amount in orders]


# TASK 7: MERGE
@task(name="merge_data")
def merge_data(customers, orders):
    print("Merging customer and order data...")
    time.sleep(2)

    return {
        "customers": customers,
        "orders": orders
    }


# TASK 8: CALCULATE METRICS
@task(name="calculate_metrics")
def calculate_metrics(data):
    print("Calculating business metrics...")
    time.sleep(3)

    return {
        "total_sales": sum(data["orders"]),
        "total_customers": len(data["customers"])
    }


# TASK 9: GENERATE REPORT
@task(name="generate_report")
def generate_report(metrics):
    print("Generating final report...")
    time.sleep(2)

    return f"""
Total Sales: {metrics['total_sales']}
Total Customers: {metrics['total_customers']}
"""


# TASK 10: SAVE REPORT
@task(name="save_report")
def save_report(report):
    print("Saving report...")
    time.sleep(2)

    with open("sales_report.txt", "w") as file:
        file.write(report)

    return "Report saved successfully"


# MAIN FLOW
@flow(name="run_param_deploy")
def run_param_deploy(source):

    # Sequential extraction and validation
    raw_data = extract_data(source)

    validated_data = validate_data(raw_data)

    # Parallel branch 1 and branch 2
    customers = clean_customers.submit(validated_data)
    orders = clean_orders.submit(validated_data)

    # Each branch continues independently
    transformed_customers = transform_customers.submit(customers)
    transformed_orders = transform_orders.submit(orders)

    # Wait for both branches and merge
    merged = merge_data(
        transformed_customers.result(),
        transformed_orders.result()
    )

    # Sequential final processing
    metrics = calculate_metrics(merged)

    report = generate_report(metrics)

    result = save_report(report)

    print(result)

    return result


if __name__ == "__main__":
    run_param_deploy(source=12)
