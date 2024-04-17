from abc import ABC, abstractmethod

from observer import Observer


class Subject(ABC):

    @abstractmethod
    def registerObserver(self, o: Observer) -> None:
        raise NotImplementedError

    @abstractmethod
    def removeObserver(self, o: Observer) -> None:
        raise NotImplementedError

    @abstractmethod
    def notifyObserver(self) -> None:
        raise NotImplementedError

