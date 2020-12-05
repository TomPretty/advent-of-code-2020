from parse import parse_boarding_pass
from utils import read_boarding_passes

boarding_passes = read_boarding_passes()

seat_ids = [parse_boarding_pass(bp) for bp in boarding_passes]
max_seat_id = max(seat_ids)

print(f"max: {max_seat_id}")
