with open("input.txt") as f:
    lines = f.read().splitlines()


def parse_line(line: str):
    parts = line.split(" ")

    positions = parts[0]
    first, second = positions.split("-")
    letter = parts[1][0]
    password = parts[2]

    return {
        "positions": {"first": int(first), "second": int(second)},
        "letter": letter,
        "password": password,
    }


password_infos = [parse_line(line) for line in lines]


def is_compliant(password_info):
    letter = password_info["letter"]
    first_letter = password_info["password"][password_info["positions"]["first"] - 1]
    second_letter = password_info["password"][password_info["positions"]["second"] - 1]

    return (first_letter == letter and not second_letter == letter) or (
        second_letter == letter and not first_letter == letter
    )

    # return (
    #     len([l for l in [first_letter, second_letter] if l == password_info["letter"]])
    #     == 1
    # )


num_compliant = len(
    [password_info for password_info in password_infos if is_compliant(password_info)]
)
print(num_compliant)
