from enum import Enum


class Status(Enum):
    CREATED = 'created'
    PAID = 'paid'
    FINISHED = 'finished'
    CANCELED = 'canceled'
    REFUNDED = 'refounded'
