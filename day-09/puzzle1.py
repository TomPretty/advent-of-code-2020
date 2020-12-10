with open("./input.txt") as f:
    numbers = f.read().splitlines()

numbers = [int(n) for n in numbers]


def is_valid(i):
    number = numbers[i]
    previous_numbers = numbers[i - 25 : i]
    possible_values = [a + b for a in previous_numbers for b in previous_numbers]
    return number in possible_values


for i in range(25, len(numbers)):
    if not is_valid(i):
        print(f"first invalid number: {numbers[i]}")
        break


target_sum = 675280050


stop = False
contiguous_numbers = []
for j in range(1, len(numbers)):
    for i in range(j):
        if sum(numbers[i:j]) == target_sum:
            contiguous_numbers = numbers[i:j]
            stop = True
        if stop:
            break
    if stop:
        break

min_value = min(contiguous_numbers)
max_value = max(contiguous_numbers)

print(f"cipher weakness: {min_value + max_value}")
