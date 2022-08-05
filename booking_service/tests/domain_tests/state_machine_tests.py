from unittest import TestCase
from booking_service.core.domain.entities import Booking
from booking_service.core.domain.enums import Status, Action


class TestStateMachine(TestCase):
    def test_should_always_start_with_created_status(self):
        booking = Booking()
        self.assertEqual(booking.status, Status.CREATED)
    