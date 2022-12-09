from model.rope_physics import RopePhysics


class Solution:
    rope_head_moves: list[str] = []

    SHORT_ROPE_KNOTS = 2
    LONG_ROPE_KNOTS = 10

    def __init__(self, input):
        self.rope_head_moves = input

    def solve(self) -> (int, int):
        # Task 1
        positions_count_tail_visited_once_or_more_simple_rope = RopePhysics().find_unique_points_visited_by_tail(self.rope_head_moves, knots_number=self.SHORT_ROPE_KNOTS)
        # Task 2
        positions_count_tail_visited_once_or_more_long_rope = RopePhysics().find_unique_points_visited_by_tail(self.rope_head_moves, knots_number=self.LONG_ROPE_KNOTS)
        return positions_count_tail_visited_once_or_more_simple_rope, positions_count_tail_visited_once_or_more_long_rope


def read_input() -> list[str]:
    input_file_name = 'input.txt'
    try:
        with open(input_file_name) as file:
            input_lines = file.readlines()
            if len(input_lines) == 0:
                raise Exception(f"File {input_file_name} is empty")
            input_lines_without_newline = [line.rstrip('\n') for line in input_lines]
            return input_lines_without_newline
    except EnvironmentError:
        raise Exception(f"File {input_file_name} is missing or invalid")


if __name__ == '__main__':
    input_lines = read_input()
    print(input_lines)
    solution = Solution(input_lines)
    print(f"Answer : {solution.solve()}")
    # 6503,
