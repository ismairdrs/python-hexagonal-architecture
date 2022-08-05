from unittest import TestCase
from booking_service.core.domain.entities import Booking
from booking_service.core.domain.enums import Status, Action


class TestStateMachine(TestCase):
    def test_should_always_start_with_created_status(self):
        booking = Booking()
        self.assertEqual(booking.status, Status.CREATED)

    def test_should_set_status_to_paid_when_paying_for_booking_with_created_status(self):
        booking = Booking()
        booking.change_state(Action.PAY)
        self.assertEqual(booking.status, Status.PAID)

    def test_should_set_status_to_canceled_when_canceling_booking_with_created_status(self):
        booking = Booking()
        booking.change_state(Action.CANCEL)
        self.assertEqual(booking.status, Status.CANCELED)

    def test_should_set_status_to_finished_when_finishing_booking_with_paid_status(self):
        booking = Booking()
        booking.change_state(Action.PAY)
        booking.change_state(Action.FINISH)
        self.assertEqual(booking.status, Status.FINISHED)

    def test_should_set_status_to_refunded_when_refounding_booking_with_paid_status(self):
        booking = Booking()
        booking.change_state(Action.PAY)
        booking.change_state(Action.REFOUND)
        self.assertEqual(booking.status, Status.REFUNDED)

    def test_should_set_status_to_created_when_reopening_canceled_booking(self):
        booking = Booking()
        booking.status = Status.CANCELED
        booking.change_state(Action.REOPEN)
        self.assertEqual(booking.status, Status.CREATED)
