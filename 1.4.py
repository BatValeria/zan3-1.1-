INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


def task():
    with open(INPUT_FILE, "r", encoding = "utf-8") as f1:
        with open(OUTPUT_FILE, "w", encoding = "utf-8") as f2:
            for line in f1:
                a = line.upper()
                for line in a:
                    f2.write(line)
    ...  # TODO перезаписать содержимое одного файла в другой


if __name__ == "__main__":
    task()

    with open(OUTPUT_FILE) as file:
        for line in file:
            print(line, end="")
