from typing import Callable

WORRY_LEVEL_DIVISOR_AFTER_OPERATION = 3

class Monkey:
    id: int = 0
    count_of_items_inspected: int = 0
    items: list[int] = []
    operation_fun: Callable[[int], int] = None
    test_fun: Callable[[int], bool] = None
    if_test_true_throw_to_monkey_with_id: int = 0
    if_test_false_throw_to_monkey_with_id: int = 0

    def __init__(self, id: int, starting_items: list[int],
                 operation_fun: Callable[[int], int], test_fun: Callable[[int], bool],
                 if_test_true_throw_to_monkey_with_id: int, if_test_false_throw_to_monkey_with_id: int):
        self.id = id
        self.items = starting_items
        self.count_of_items_inspected = 0
        self.operation_fun = operation_fun
        self.test_fun = test_fun
        self.if_test_true_throw_to_monkey_with_id = if_test_true_throw_to_monkey_with_id
        self.if_test_false_throw_to_monkey_with_id = if_test_false_throw_to_monkey_with_id

    def inspect_items_and_throw_to_other_monkeys(self, monkeys: list['Monkey']):
        while self.items != []:
            item = self.items.pop(0)
            worry_level = self.operation_fun(item)
            worry_level_bored = int(worry_level / WORRY_LEVEL_DIVISOR_AFTER_OPERATION)
            if self.test_fun(worry_level_bored):
                self.throw_to_monkey(worry_level_bored, self.if_test_true_throw_to_monkey_with_id, monkeys)
            else:
                self.throw_to_monkey(worry_level_bored, self.if_test_false_throw_to_monkey_with_id, monkeys)
            self.count_of_items_inspected += 1

    def throw_to_monkey(self, item: int, target_monkey_id: int, monkeys: list['Monkey']):
        target_list = list(filter(lambda monkey: monkey.id == target_monkey_id, monkeys))
        if len(target_list) != 1:
            raise Exception(f"Monkey with id {target_monkey_id} does not exist!")
        else:
            target_list[0].add_item(item)

    def add_item(self, item: int):
        self.items.append(item)





