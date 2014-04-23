STATE_MAYBE = 0

STATE_CHOICES = (
    (STATE_MAYBE, 'Maybe'),
    (1, 'Yes'),
    (2, 'No'),
)

TITLE_CHOICES = (
            ('mr', 'Mr'),
            ('mrs', 'Mrs'),
            ('miss', 'Miss'),
            ('ms', 'Ms'),
            ('dr', 'Dr')
        )

CASE_STATE_OPEN = 0
CASE_STATE_CLOSED = 1
CASE_STATE_REJECTED = 2
CASE_STATE_ACCEPTED = 3
CASE_STATE_CHOICES = (
    (CASE_STATE_OPEN, 'OPEN'),
    (CASE_STATE_CLOSED, 'CLOSED'),
    (CASE_STATE_REJECTED, 'REJECTED'),
    (CASE_STATE_ACCEPTED, 'ACCEPTED')
)
