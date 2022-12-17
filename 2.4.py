import json


def task():
    filename = "input.json"
    # TODO считать содержимое JSON файла
    file = open("input.json")
    data = json.load(file)

    gen_exr = (item["contains_improvement_appeals"] for item in data)
          # TODO записать выражение-генератор возвращающее значение по ключу contains_improvement_appeals
    return sum(gen_exr)


if __name__ == "__main__":
    print(task())
