from dataclasses import dataclass
from datetime import datetime

from booking_service.core.domain.enums import Status, Action


@dataclass(init=False, repr=True)
class Booking:
    id: int
    place_at: datetime
    start: datetime
    end: datetime
    _status: Status = Status.CREATED

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value: Status):
        if value not in Status:
            raise ValueError(f'Invalid status: {value}')
        self._status = value
