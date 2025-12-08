from orderbook import Orderbook
from task import Task


class OrderbookApplication:
    def __init__(self) -> None:
        self.__running: bool = False
        self.__orderbook: Orderbook = Orderbook()

    def add_order(self, inputs: tuple[str, str, int]) -> None:
        self.__orderbook.add_order(*inputs)

        print("task added!")

    def print_finished_tasks(self) -> None:
        if not self.__orderbook.finished_orders:
            print("no finished tasks")

        self.__print_orders(self.__orderbook.finished_orders)

    def print_unfinished_tasks(self) -> None:
        if not self.__orderbook.unfinished_orders:
            print("no unfinished tasks")

        self.__print_orders(self.__orderbook.unfinished_orders)

    def mark_order_finished(self, inputs: tuple[int]) -> None:
        self.__orderbook.mark_order_finished(*inputs)

        print("marked as finished")

    def print_programmers(self) -> None:
        for programmer in self.__orderbook.programmers:
            print(programmer)

    def status_of_programmer(self, inputs: tuple[str]):
        (
            finished_tasks_count,
            unfinished_tasks_count,
            sum_of_finished_workloads,
            sum_of_unfinished_workloads,
        ) = self.__orderbook.status_of_programmer(*inputs)

        print(
            f"tasks: finished {finished_tasks_count} - unfinished {unfinished_tasks_count}, "
            f"hours: done {sum_of_finished_workloads} - scheduled {sum_of_unfinished_workloads}"
        )

    def run(self) -> None:
        self.__running = True

        self.__help()

        while self.__running:
            print()

            command = input("command: ")

            if command == "0":
                self.__exit()
            elif command == "1":
                try:
                    self.add_order(self.__add_order_inputs())
                except ValueError:
                    print("erroneous input")
            elif command == "2":
                self.print_finished_tasks()
            elif command == "3":
                self.print_unfinished_tasks()
            elif command == "4":
                try:
                    self.mark_order_finished(self.__mark_finished_inputs())
                except ValueError:
                    print("erroneous input")
            elif command == "5":
                self.print_programmers()
            elif command == "6":
                try:
                    self.status_of_programmer(self.__status_of_programmer_inputs())
                except ValueError:
                    print("erroneous input")
            else:
                self.__help()

    def __exit(self) -> None:
        self.__running = False

    def __help(self) -> None:
        print("commands:")
        print("0 exit")
        print("1 add order")
        print("2 list finished tasks")
        print("3 list unfinished tasks")
        print("4 mark task as finished")
        print("5 programmers")
        print("6 status of programmer")

    def __print_orders(self, orders: list[Task]) -> None:
        for task in orders:
            print(task)

    def __add_order_inputs(self) -> tuple[str, str, int]:
        description = input("description: ")
        programmer, workload = input("programmer and workload estimate: ").split(" ")

        return description, programmer, int(workload)

    def __mark_finished_inputs(self) -> tuple[int]:
        id = input("id: ")

        return (int(id),)

    def __status_of_programmer_inputs(self) -> tuple[str]:
        programmer = input("programmer: ")

        return (programmer,)


def main():
    orderbook_app = OrderbookApplication()

    orderbook_app.run()


if __name__ == "__main__":
    main()
