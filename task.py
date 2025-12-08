class Task:
    ID_COUNTER = 0

    def __init__(
        self,
        description: str,
        programmer: str,
        workload: int,
    ) -> None:
        Task.ID_COUNTER += 1

        self.__id: int = Task.ID_COUNTER
        self.description: str = description
        self.workload: int = workload
        self.programmer: str = programmer
        self.__finished: bool = False

    def __str__(self) -> str:
        workload = f"{self.workload} hours"
        programmer = f"programmer {self.programmer}"
        status = "finished" if self.__finished else "not finished"

        return f"{self.__id}: {self.description} ({workload}), {programmer} {status.upper()}"

    @property
    def id(self) -> int:
        return self.__id

    @property
    def finished(self) -> bool:
        return self.__finished

    def mark_finished(self) -> None:
        self.__finished = True
