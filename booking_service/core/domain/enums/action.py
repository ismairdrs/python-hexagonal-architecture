from enum import Enum


class Action(Enum):
    PAY = 0
    FINISH = 1 # after paid and used
    CANCEL = 2 # can never be paid
    REFOUND = 3 # paid then refounded
    REOPEN = 4 # canceled then reopened
