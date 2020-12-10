from parse import parse_boarding_pass
from utils import read_boarding_passes

boarding_passes = read_boarding_passes()

seat_ids = [parse_boarding_pass(bp) for bp in boarding_passes]


def get_missing_ids(seat_ids):
    missing_ids = []
    for seat_id in range(128 * 8):
        if seat_id not in seat_ids:
            missing_ids.append(seat_id)
    return missing_ids


missing_ids = get_missing_ids(seat_ids)


def get_seat_id(missing_ids):
    for seat_id in missing_ids:
        if seat_id + 1 not in missing_ids and seat_id - 1 not in missing_ids:
            return seat_id


seat_id = get_seat_id(missing_ids)
print(f"seat id: {seat_id}")
