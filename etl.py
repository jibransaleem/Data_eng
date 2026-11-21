
from prefect import flow, task
import requests


@task(name="Predicts_age")
def Predicts_age(name: str):
    url = f"https://api.agify.io/?name={name}"

    response = requests.get(url)
    response.raise_for_status()

    data = response.json()
    return data["age"]


@task(name="ISEven")
def ISEven(age: int):
    return age % 2 == 0


@task(name="Even_Age")
def Even_Age(age: int):
    print(f"{age} is an EVEN age")


@task(name="Odd_Age")
def Odd_Age(age: int):
    print(f"{age} is an ODD age")


@flow(name="Age-Prediction-Flow")
def Age_Prediction(name: str):

    # Task 1: Predict age
    age = Predicts_age(name)

    if age is None:
        print("Age prediction unavailable")
        return

    # Task 2: Check condition
    is_even = ISEven(age)

    # Conditional branching
    if is_even:
        Even_Age(age)
    else:
        Odd_Age(age)


if __name__ == "__main__":
    Age_Prediction("jibran")
