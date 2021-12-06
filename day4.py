def pivot(list : list[int]) -> list[list[int]]:
    result = []
    for column in range(len(list[0])):
        result.append([])
        for row in list:
            result[column].append(row[column])

    return result

class Board:
    def __init__(self, rows: list[str]) -> None:
        self.positions = [self.__enrich_row_with_positions__(row.split()) for row in rows]

    def __enrich_row_with_positions__(self, row: list[str]) -> tuple[int, bool]:
        return [(int(number_str), False) for number_str in row]

    def get_bingo(self) -> list[int] | None:
        def __get__bingo__(positions: list[list[tuple[int, bool]]]):
            for row in positions:
                if all(list(map(lambda x: x[1], row))):
                    return self.__get_not_marked_numbers__()
            return None

        return __get__bingo__(self.positions) or __get__bingo__(pivot(self.positions))

    def __get_not_marked_numbers__(self):
        result = []
        for row in self.positions:
            for number, marked in row:
                if not marked:
                    result.append(number)
        return result

    def mark_position(self, number):
        for row_index, row in enumerate(self.positions):
            for column_index, position in enumerate(row):
                if (position_number := position[0]) == number:
                    self.positions[row_index][column_index] = (position_number, True)

def get_input() -> tuple[list[int], list[Board]]:
    f = open("inputs/Day4.txt", "r")
    lines = f.readlines()
    bingo_numbers = [int(x) for x in lines[0].replace("\n", "").split(",")]
    boards_str = "".join(lines[2:])
    boards = [Board(x.splitlines()) for x in boards_str.split("\n\n")]
    return (bingo_numbers, boards)
    
input = get_input()

def part_one():
    for number in input[0]:
        for board in input[1]:
            board.mark_position(number)
            bingo = board.get_bingo()
            if bingo:
                print(sum(bingo) * number)
                return

def part_two():
    boards = input[1]
    completed_boards = set()
    for number in input[0]:
        for board_index, board in enumerate(boards):
            board.mark_position(number)
            bingo = board.get_bingo()
            if bingo:
                completed_boards.add(board_index)
                if len(completed_boards) == len(boards):
                    print(sum(bingo) * number)
                    return

part_one()
part_two()