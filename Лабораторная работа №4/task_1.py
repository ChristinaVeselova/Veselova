# TODO решите задачу
import json

INPUT_JSON = "input.json"


def task() -> float:
    with open(INPUT_JSON, "r") as f:
        json_data = json.load(f)

    values = sum([item["score"] * item["weight"] for item in json_data])

    return round(values, 3)


print(task())
