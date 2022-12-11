from .monkey import Monkey


class MonkeyInteraction:
    monkeys: list[Monkey] = []

    def __init__(self, monkeys: list[Monkey]):
        self.monkeys = monkeys

    def perform_rounds(self, rounds_count: int):
        for i in range(0, rounds_count):
            self.perform_one_round()
            self.print_round_results(i)

    def get_monkey_business(self):
        inspections_of_each_monkey: list[int] = list(map(lambda monkey: monkey.count_of_items_inspected, self.monkeys))
        inspections_of_each_monkey.sort(reverse=True)
        assert len(inspections_of_each_monkey) >= 2
        return inspections_of_each_monkey[0] * inspections_of_each_monkey[1]

    def perform_one_round(self):
        for monkey in self.monkeys:
            monkey.inspect_items_and_throw_to_other_monkeys(self.monkeys)

    def print_round_results(self, round_id):
        print(f"After round {round_id + 1}, the monkeys are holding items with these worry levels:")
        for monkey in self.monkeys:
            print(f"Monkey {monkey.id}: {str(monkey.items)}")
        print()
