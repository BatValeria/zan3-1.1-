import json


def task():
    filename = "input.json"
    file = open(filename)
    data = json.load(file)  # TODO считать содержимое JSON файла

    while True:
        counter = 0
        max_num = 0.00040403710013251447
        for key in data:
            counter += 1
            if key["score"] > max_num:
                max_num = key["score"]
                max_counter = counter - 1
        return data[max_counter]

if __name__ == "__main__":
    print(task())
