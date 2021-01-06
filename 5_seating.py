
# A seat might be specified like FBFBBFFRLR, where F means "front", B means "back", L means "left", and R means "right".

# The first 7 characters will either be F or B; these specify exactly one of the 128 rows on the plane (numbered 0 through 127). Each letter tells you which half of a region the given seat is in. Start with the whole list of rows; the first letter indicates whether the seat is in the front (0 through 63) or the back (64 through 127). The next letter indicates which half of that region the seat is in, and so on until you're left with exactly one row.

# For example, consider just the first seven characters of FBFBBFFRLR:

# Start by considering the whole range, rows 0 through 127.
# F means to take the lower half, keeping rows 0 through 63.
# B means to take the upper half, keeping rows 32 through 63.
# F means to take the lower half, keeping rows 32 through 47.
# B means to take the upper half, keeping rows 40 through 47.
# B keeps rows 44 through 47.
# F keeps rows 44 through 45.
# The final F keeps the lower of the two, row 44.
# The last three characters will be either L or R; these specify exactly one of the 8 columns of seats on the plane (numbered 0 through 7). The same process as above proceeds again, this time with only three steps. L means to keep the lower half, while R means to keep the upper half.

# For example, consider just the last 3 characters of FBFBBFFRLR:

# Start by considering the whole range, columns 0 through 7.
# R means to take the upper half, keeping columns 4 through 7.
# L means to take the lower half, keeping columns 4 through 5.
# The final R keeps the upper of the two, column 5.
# So, decoding FBFBBFFRLR reveals that it is the seat at row 44, column 5.

# Every seat also has a unique seat ID: multiply the row by 8, then add the column. In this example, the seat has ID 44 * 8 + 5 = 357.

# Ding! The "fasten seat belt" signs have turned on. Time to find your seat.

# It's a completely full flight, so your seat should be the only missing boarding pass in your list. 
# However, there's a catch: some of the seats at the very front and back of the plane don't exist on this 
# aircraft, so they'll be missing from your list as well.

# Your seat wasn't at the very front or back, though; the seats with IDs +1 and -1 from yours will be 
# in your list.

# What is the ID of your seat?
# 1:    2, 3, 4, 5, 6
# 2: 1, 2, 3, 4, 5, 6, 7
# 3: 1, 2, 3, 4, 5, 6, 7
# ...
# 57: 1, 2, X, 4, 5, 6, 7
# ...
# 126: 1, 2, 3, 4, 5, 6, 7
# 127:    2, 3, 4, 5, 6

def halfway_point(lower, upper):
    import math
    return math.ceil((upper - lower) / 2)


def find_location(location_string, lower, upper, lower_half, upper_half):
    for char in location_string:
        if char == lower_half:
            upper = upper - halfway_point(lower, upper)
        elif char == upper_half:
            lower = lower + halfway_point(lower, upper)
    return lower


def find_seat(seat):
    row = find_location(seat[:-3], lower=0, upper=127, lower_half='F', upper_half='B')
    column = find_location(seat[-3:], lower=0, upper=7, lower_half='L', upper_half='R')
    return row, column, find_seat_id(row, column)


def find_seat_id(row, column):
    return (row * 8) + column


seats = open('inputs/5_seats.txt').read().split('\n')
max_seat_id = 0
test_seats = ['FBFBBFFRLR', 'BFFFBBFRRR', 'FFFBBBFRRR', 'BBFFBBFRLL']
full_row = [0, 1, 2, 3, 4, 5, 6, 7]
seating_chart = {}
# FBFBBFFRLR: row 44, column 5, seat ID 357.
# BFFFBBFRRR: row 70, column 7, seat ID 567.
# FFFBBBFRRR: row 14, column 7, seat ID 119.
# BBFFBBFRLL: row 102, column 4, seat ID 820.

for seat in seats:
    row, column, seat_id = find_seat(seat)
    if seat_id > max_seat_id:
        max_seat_id = seat_id
    seating_chart.setdefault(row, []).append(column)


for row in seating_chart:
    seats = seating_chart[row]
    if len(seats) <= 7:
        missing_seats = list(set(full_row) - set(seats))
        if len(missing_seats) == 1:
            column = missing_seats[0]
            print(f'Missing: Row {row}, Column {column}, Seat ID: {find_seat_id(row, column)}')
print(f'Highest Seat ID: {max_seat_id}')
