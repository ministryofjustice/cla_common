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

CASE_STATE_OPEN = 'open'
CASE_STATE_CLOSED = 'closed'
CASE_STATE_REJECTED = 'rejected'
CASE_STATE_ACCEPTED = 'accepted'
CASE_STATE_CHOICES = (
    (CASE_STATE_OPEN, 'OPEN'),
    (CASE_STATE_CLOSED, 'CLOSED'),
    (CASE_STATE_REJECTED, 'REJECTED'),
    (CASE_STATE_ACCEPTED, 'ACCEPTED')
)
