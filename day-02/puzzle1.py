with open("input.txt") as f:
    lines = f.read().splitlines()


def parse_line(line: str):
    parts = line.split(" ")

    bounds = parts[0]
    lower, upper = bounds.split("-")
    letter = parts[1][0]
    password = parts[2]

    return {
        "bounds": {"upper": int(upper), "lower": int(lower)},
        "letter": letter,
        "password": password,
    }


password_infos = [parse_line(line) for line in lines]


def is_compliant(password_info):
    num_uses = len(
        [c for c in password_info["password"] if c == password_info["letter"]]
    )
    return (
        num_uses >= password_info["bounds"]["lower"]
        and num_uses <= password_info["bounds"]["upper"]
    )


num_compliant = len(
    [password_info for password_info in password_infos if is_compliant(password_info)]
)
print(num_compliant)
