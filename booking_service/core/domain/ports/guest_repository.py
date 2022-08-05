from abc import ABC, abstractmethod

from booking_service.core.domain.entities import Guest


class IGuestRepository(ABC):
    
    @abstractmethod
    def get_by_id(self, id: int) -> Guest:
        raise NotImplementedError()

    @abstractmethod
    def save(self, guest: Guest) -> None:
        raise NotImplementedError()
