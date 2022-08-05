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

    def change_state(self, action: Action):
        if action not in Action:
            raise ValueError(f'Invalid action: {action}')

        set_state = {
            (Status.CREATED, Action.PAY): Status.PAID,
            (Status.CREATED, Action.CANCEL): Status.CANCELED,
            (Status.PAID, Action.FINISH): Status.FINISHED,
            (Status.PAID, Action.REFOUND): Status.REFUNDED,
            (Status.CANCELED, Action.REOPEN): Status.CREATED,
        }

        self.status = set_state.get((self.status, action), self._status)
