from extended_choices import Choices


ELIGIBILITY_STATES = Choices(
    # constant, db_id, friendly string
    ('MAYBE', 'maybe', 'Maybe'),
    ('YES', 'yes', 'Yes'),
    ('NO', 'no', 'No'),
)


TITLES = Choices(
    # constant, db_id, friendly string
    ('MR', 'mr', 'Mr'),
    ('MRS', 'mrs', 'Mrs'),
    ('MISS', 'miss', 'Miss'),
    ('MS', 'ms', 'Ms'),
    ('DR', 'dr', 'Dr')
)

CASE_STATES = Choices(
    # constant, db_id, friendly string
    ('OPEN', 'open', 'Open'),
    ('CLOSED', 'closed', 'Closed'),
    ('REJECTED', 'rejected', 'Rejected'),
    ('ACCEPTED', 'accepted', 'Accepted'),
)

# CASE_STATE_OPEN = 'open'
# CASE_STATE_CLOSED = 'closed'
# CASE_STATE_REJECTED = 'rejected'
# CASE_STATE_ACCEPTED = 'accepted'
# CASE_STATE_CHOICES = (
#     (CASE_STATE_OPEN, 'OPEN'),
#     (CASE_STATE_CLOSED, 'CLOSED'),
#     (CASE_STATE_REJECTED, 'REJECTED'),
#     (CASE_STATE_ACCEPTED, 'ACCEPTED')
# )

CASELOGTYPE_ACTION_KEYS = Choices(
    # constant, db_id, friendly string
    ('DECLINE_SPECIALISTS', 'decline_specialists', 'Deline Specialists'),
    ('PROVIDER_REJECT_CASE', 'provider:reject_case', 'Provider rejects the case'),
    ('PROVIDER_ACCEPT_CASE', 'provider:accept_case', 'Provider accepts the case'),
    ('PROVIDER_CLOSE_CASE', 'provider:close_case', 'Provider closes the case'),
)
