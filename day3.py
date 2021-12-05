from itertools import groupby

def get_input():
    f = open("inputs/Day3.txt", "r")
    return f.readlines()

def pivot(list : list[str]) -> list[list[str]]:
    result = []
    for column in range(len(list[0])):
        result.append([])
        for row in list:
            result[column].append(row[column])

    return result

def get_most_common_element(elements : list[str]) -> str:
    bits_with_count = group_bits(elements)
    return sorted(bits_with_count, reverse=True, key=lambda x: (x[1], x[0]))[0][0]

def get_least_common_element(elements : list[str]) -> str:
    bits_with_count = group_bits(elements)
    return sorted(bits_with_count, reverse=False, key=lambda x: (x[1], x[0]))[0][0]

def group_bits(elements):
    return [(key, len(list(group))) for key, group in groupby(sorted(elements))]
    
def get_gamma(input):
    common_elements = [get_most_common_element(column) for column in pivot(input)]
    return int("".join(common_elements), base=2)

def get_epsilon(input):
    common_elements = [get_least_common_element(column) for column in pivot(input)]
    return int("".join(common_elements), base=2)

def get_oxygen_rating(input : list[str]):
    def get_common_bits(input):
        return [get_most_common_element(column) for column in pivot(input)]

    common_elements = get_common_bits(input)
    current_bit = 0
    processed_values = input

    while len(processed_values) > 1:
        bit_criteria = common_elements[current_bit]
        processed_values = list(filter(lambda x: x[current_bit] == bit_criteria, processed_values))
        common_elements = get_common_bits(processed_values)
        current_bit += 1

    return int(processed_values[0], base=2)

def get_co2_rating(input : list[str]):
    def get_common_bits(input):
        return [get_least_common_element(column) for column in pivot(input)]

    common_elements = get_common_bits(input)
    current_bit = 0
    processed_values = input

    while len(processed_values) > 1:
        bit_criteria = common_elements[current_bit]
        processed_values = list(filter(lambda x: x[current_bit] == bit_criteria, processed_values))
        common_elements = get_common_bits(processed_values)
        current_bit += 1

    return int(processed_values[0], base=2)

input = get_input()

def part_one():
    print(get_gamma(input) * get_epsilon(input))

def part_two():
    oxygen = get_oxygen_rating(input)
    co2 = get_co2_rating(input)
    print(oxygen * co2)

part_one()
part_two()