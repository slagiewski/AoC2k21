def get_input():
    f = open("inputs/Day2.txt", "r")
    
    def split_command(command_str: str):
        parts = command_str.split()
        return (parts[0], int(parts[1]))

    return [split_command(x) for x in f.readlines()]

def part_one():
    def calculate_position(input):
        depth = distance = 0
        
        def get_depth_change(command):
            if command[0] == "down":
                return command[1]
            if command[0] == "up":
                return -command[1]
            return 0

        def get_distance_change(command):
            if command[0] == "forward":
                return command[1]
            return 0

        for x in input:
            depth += get_depth_change(x)
            distance += get_distance_change(x)

        return (depth, distance)
        
    position = calculate_position(get_input()) 
    print(position[0] * position[1])

def part_two():
    def calculate_position(input):
        depth = distance = aim = 0
        
        def get_aim_change(command):
            if command[0] == "down":
                return command[1]
            if command[0] == "up":
                return -command[1]
            return 0

        def get_distance_change(command):
            if command[0] == "forward":
                return command[1]
            return 0

        def get_depth_change(current_aim, command):
            if command[0] == "forward":
                return current_aim * command[1]
            return 0

        for x in input:
            aim += get_aim_change(x)
            depth += get_depth_change(aim, x)
            distance += get_distance_change(x)

        return (depth, distance)
        
    position = calculate_position(get_input()) 
    print(position[0] * position[1])

part_one()
part_two()