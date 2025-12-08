class Task:
    def __init__(
        self,
        id: int,
        description: str,
        programmer: str,
        workload: int,
        finished: bool = False,
    ) -> None:
        self.__id: int = id
        self.__description: str = description
        self.__workload: int = workload
        self.__programmer: str = programmer
        self.__finished: bool = finished

    def __str__(self) -> str:
        workload = f"{self.__workload} hours"
        programmer = f"programmer {self.programmer}"

        return f"{self.id}: {self.description} ({workload}), {programmer} {self.status.upper()}"

    @property
    def id(self) -> int:
        return self.__id

    @property
    def description(self) -> str:
        return self.__description

    @property
    def workload(self) -> int:
        return self.__workload

    @property
    def programmer(self) -> str:
        return self.__programmer

    @property
    def finished(self) -> bool:
        return self.__finished

    @property
    def status(self) -> str:
        return "finished" if self.__finished else "not finished"

    def mark_finished(self) -> None:
        self.__finished = True
