def get_input():
    f = open("inputs/Day1.txt", "r")
    return [int(x) for x in f.readlines()]

def get_reading_states(reading: list):
    def get_state(current_index):
        previous_index = current_index - 1

        if previous_index < 0:
            return None
        if reading[current_index] > reading[previous_index]:
            return "Increased"
        if reading[current_index] < reading[previous_index]:
            return "Decreased"
        return "Equal"

    return [get_state(current_index=i) for i, _ in enumerate(reading)]

def part_one():
    states = get_reading_states(get_input())
    print(states.count("Increased"))

def part_two():
    def chunks(list, chunk_size):
        return [list[i:i+3] for i, _ in enumerate(list[:(len(list)-chunk_size) + 1])]
    states = get_reading_states([sum(x) for x in chunks(list=get_input(), chunk_size=3)])
    print(states.count("Increased"))

part_one()
part_two()
