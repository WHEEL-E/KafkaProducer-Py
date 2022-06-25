from faker import Faker

fake = Faker()


def returnFakeData():
    return {
        "user_id": fake.name(),
        "pulse": fake.address(),
        "SPO2": fake.year()
    }


if __name__ == "__main__":
    print(returnFakeData())
