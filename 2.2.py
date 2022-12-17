import json


def task(input_filename: str, output_filename: str) -> None:
    ...  # TODO считать содержимое json файл input.json
    with open(input_filename) as  file:
        data = json.load(file)

    ...  # TODO записать содержимое в json файл output.json с отступами
    json_out = json.dumps(data, indent=4)

    with open(output_filename, "w") as output:
        output.write(json_out)


if __name__ == "__main__":
    input_file = "input.json"
    output_file = "output.json"

    task(input_file, output_file)

    with open(output_file) as output_f:
        for line in output_f:
            print(line, end="")
