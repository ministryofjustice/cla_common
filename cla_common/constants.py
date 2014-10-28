from os import environ as env

from extended_choices import Choices


ELIGIBILITY_STATES = Choices(
    # constant, db_id, friendly string
    ('UNKNOWN', 'unknown', 'Unknown'),
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


REQUIRES_ACTION_BY = Choices(
    # constant, db_id, friendly string

    # the Operator needs to take some actions (e.g. call the client)
    ('OPERATOR', 'operator', 'Operator'),

    # the Operator Manager needs to take some actions
    ('OPERATOR_MANAGER', 'operator_manager', 'Operator Manager'),

    # the Specialist needs to accept or reject the case
    ('PROVIDER_REVIEW', '1_provider_review', 'Provider Review'),

    # the Specialist has accepted the case and the Case needs further work
    ('PROVIDER', '2_provider', 'Provider'),
)

MATTER_TYPE_LEVELS = Choices(
    # constant, db_id, friendly string
    ('ONE', 1, '1'),
    ('TWO', 2, '2'),
)

CASELOGTYPE_ACTION_KEYS = Choices(
    # constant, db_id, friendly string
    ('DECLINE_SPECIALISTS', 'decline_specialists', 'Decline Specialists'),
    ('DEFER_ASSIGNMENT', 'defer_assign', 'Defer Specialist Assignment'),
    ('PROVIDER_REJECT_CASE', 'provider:reject_case', 'Provider rejects the case'),
    ('PROVIDER_ACCEPT_CASE', 'provider:accept_case', 'Provider accepts the case'),
    ('PROVIDER_CLOSE_CASE', 'provider:close_case', 'Provider closes the case'),
)

THIRDPARTY_REASON = [  ('CHILD_PATIENT', 'Child or patient'),
                       ('POWER_ATTORNEY', 'Subject to power of attorney'),
                       ('NO_TELEPHONE_DISABILITY', 'Cannot communicate via the telephone, due to disability'),
                       ('NO_TELEPHONE_LANGUAGE', 'Cannot communicate via the telephone, due to a language requirement'),
                       ('OTHER', 'Other')
                       ]

THIRDPARTY_RELATIONSHIP = [ ('PARENT_GUARDIAN', 'Parent or guardian'),
                            ('FAMILY_FRIEND', 'Family member or friend'),
                            ('PROFESSIONAL', 'Professional'),
                            ('LEGAL_ADVISOR', 'Legal adviser'),
                            ('OTHER', 'Other')
                            ]

ADAPTATION_LANGUAGES = [('ASSAMESE', 'Assamese'),
                        ('AZERI', 'Azeri'),
                        ('AFRIKAANS', 'Afrikaans'),
                        ('ALGERIAN', 'Algerian'),
                        ('ASHANTI', 'Ashanti'),
                        ('AKAN', 'Akan'),
                        ('ALBANIAN', 'Albanian'),
                        ('AMHARIC', 'Amharic'),
                        ('ARMENIAN', 'Armenian'),
                        ('ARABIC', 'Arabic'),
                        ('ASSYRIAN', 'Assyrian'),
                        ('AZERBAIJANI', 'Azerbaijani'),
                        ('BADINI', 'Badini'),
                        ('BENGALI', 'Bengali'),
                        ('BURMESE', 'Burmese'),
                        ('BAJUNI', 'Bajuni'),
                        ('BELORUSSIAN', 'Belorussian'),
                        ('BOSNIAN', 'Bosnian'),
                        ('BERBER', 'Berber'),
                        ('BASQUE', 'Basque'),
                        ('BULGARIAN', 'Bulgarian'),
                        ('BRAVA', 'Brava'),
                        ('BRAZILIAN', 'Brazilian'),
                        ('CANTONESE', 'Cantonese'),
                        ('CEBUANO', 'Cebuano'),
                        ('CREOLE', 'Creole'),
                        ('CHINESE', 'Chinese'),
                        ('CHEROKEE', 'Cherokee'),
                        ('COLUMBIAN', 'Columbian'),
                        ('CAMBODIAN', 'Cambodian'),
                        ('CHAOCHOW', 'Chaochow'),
                        ('CROATIAN', 'Croatian'),
                        ('CATALAN', 'Catalan'),
                        ('CZECH', 'Czech'),
                        ('DANISH', 'Danish'),
                        ('DARI', 'Dari'),
                        ('DUTCH', 'Dutch'),
                        ('EGYPTIAN', 'Egyptian'),
                        ('ENGLISH', 'English'),
                        ('ESTONIAN', 'Estonian'),
                        ('ERITREAN', 'Eritrean'),
                        ('ESPERANTO', 'Esperanto'),
                        ('ETHIOPIAN', 'Ethiopian'),
                        ('FARSI', 'Farsi'),
                        ('FIJIAN', 'Fijian'),
                        ('FLEMISH', 'Flemish'),
                        ('FANTI', 'Fanti'),
                        ('FRENCH', 'French'),
                        ('FINNISH', 'Finnish'),
                        ('FULLA', 'Fulla'),
                        ('GA', 'Ga'),
                        ('GERMAN', 'German'),
                        ('GURMUKHI', 'Gurmukhi'),
                        ('GAELIC', 'Gaelic'),
                        ('GORANI', 'Gorani'),
                        ('GEORGIAN', 'Georgian'),
                        ('GREEK', 'Greek'),
                        ('GUJARATI', 'Gujarati'),
                        ('HAKKA', 'Hakka'),
                        ('HEBREW', 'Hebrew'),
                        ('HINDI', 'Hindi'),
                        ('HOMA', 'Homa'),
                        ('HAUSA', 'Hausa'),
                        ('HUNGARIAN', 'Hungarian'),
                        ('HUI', 'Hui'),
                        ('ICELANDIC', 'Icelandic'),
                        ('IGBO', 'Igbo'),
                        ('ILOCANO', 'Ilocano'),
                        ('INDONESIAN', 'Indonesian'),
                        ('IRAQI', 'Iraqi'),
                        ('IRANIAN', 'Iranian'),
                        ('ITALIAN', 'Italian'),
                        ('JAPANESE', 'Japanese'),
                        ('KASHMIRI', 'Kashmiri'),
                        ('KREO', 'Kreo'),
                        ('KIRUNDI', 'Kirundi'),
                        ('KURMANJI', 'Kurmanji'),
                        ('KANNADA', 'Kannada'),
                        ('KOREAN', 'Korean'),
                        ('KRIO', 'Krio'),
                        ('KOSOVAN', 'Kosovan'),
                        ('KURDISH', 'Kurdish'),
                        ('KINYARWANDA', 'Kinyarwanda'),
                        ('KINYAMIRENGE', 'Kinyamirenge'),
                        ('KAZAKH', 'Kazakh'),
                        ('LATVIAN', 'Latvian'),
                        ('LAOTIAN', 'Laotian'),
                        ('LAO', 'Lao'),
                        ('LUBWISI', 'Lubwisi'),
                        ('LEBANESE', 'Lebanese'),
                        ('LINGALA', 'Lingala'),
                        ('LUO', 'Luo'),
                        ('LUSOGA', 'Lusoga'),
                        ('LITHUANIAN', 'Lithuanian'),
                        ('LUGANDA', 'Luganda'),
                        ('MANDARIN', 'Mandarin'),
                        ('MACEDONIAN', 'Macedonian'),
                        ('MOLDOVAN', 'Moldovan'),
                        ('MIRPURI', 'Mirpuri'),
                        ('MANDINKA', 'Mandinka'),
                        ('MALAY', 'Malay'),
                        ('MONGOLIAN', 'Mongolian'),
                        ('MOROCCAN', 'Moroccan'),
                        ('MARATHI', 'Marathi'),
                        ('MALTESE', 'Maltese'),
                        ('MALAYALAM', 'Malayalam'),
                        ('NDEBELE', 'Ndebele'),
                        ('NEPALESE', 'Nepalese'),
                        ('NIGERIAN', 'Nigerian'),
                        ('NORWEGIAN', 'Norwegian'),
                        ('NYAKUSE', 'Nyakuse'),
                        ('OROMO', 'Oromo'),
                        ('OTHER', 'Other'),
                        ('PAHARI', 'Pahari'),
                        ('PERSIAN', 'Persian'),
                        ('PORTUGUESE', 'Portuguese'),
                        ('PHILIPINO', 'Philipino'),
                        ('POLISH', 'Polish'),
                        ('POTHWARI', 'Pothwari'),
                        ('PUSTHU', 'Pusthu'),
                        ('PUNJABI', 'Punjabi'),
                        ('ROMANIAN', 'Romanian'),
                        ('RUSSIAN', 'Russian'),
                        ('SOTHO', 'Sotho'),
                        ('SERBO-CROAT', 'Serbo-Croat'),
                        ('SWEDISH', 'Swedish'),
                        ('SERBIAN', 'Serbian'),
                        ('SHONA', 'Shona'),
                        ('SINHALESE', 'Sinhalese'),
                        ('SIRAIKI', 'Siraiki'),
                        ('SLOVAK', 'Slovak'),
                        ('SAMOAN', 'Samoan'),
                        ('SLOVENIAN', 'Slovenian'),
                        ('SOMALI', 'Somali'),
                        ('SORANI', 'Sorani'),
                        ('SPANISH', 'Spanish'),
                        ('SRI LANKAN', 'Sri Lankan'),
                        ('SCOTTISH GAELIC', 'Scottish Gaelic'),
                        ('SUDANESE', 'Sudanese'),
                        ('SWAHILI', 'Swahili'),
                        ('SWAHILLI', 'Swahilli'),
                        ('SYLHETI', 'Sylheti'),
                        ('TAMIL', 'Tamil'),
                        ('TIBETAN', 'Tibetan'),
                        ('TELEGU', 'Telegu'),
                        ('ELAKIL', 'Elakil'),
                        ('TAGALOG', 'Tagalog'),
                        ('THAI', 'Thai'),
                        ('TIGRINIAN', 'Tigrinian'),
                        ('TIGRE', 'Tigre'),
                        ('TAJIK', 'Tajik'),
                        ('TAIWANESE', 'Taiwanese'),
                        ('TURKMANISH', 'Turkmanish'),
                        ('TSWANA', 'Tswana'),
                        ('TURKISH', 'Turkish'),
                        ('TWI', 'Twi'),
                        ('UGANDAN', 'Ugandan'),
                        ('UKRANIAN', 'Ukranian'),
                        ('URDU', 'Urdu'),
                        ('USSIAN', 'Ussian'),
                        ('UZBEK', 'Uzbek'),
                        ('VIETNAMESE', 'Vietnamese'),
                        ('WELSH', 'Welsh'),
                        ('WOLOF', 'Wolof'),
                        ('XHOSA', 'Xhosa'),
                        ('YUGOSLAVIAN', 'Yugoslavian'),
                        ('YIDDISH', 'Yiddish'),
                        ('YORUBA', 'Yoruba'),
                        ('ZULU', 'Zulu')
                    ]

DIAGNOSIS_SCOPE = Choices(
    # constant, db_id, friendly string
    ('INSCOPE', 'INSCOPE', 'In Scope'),
    ('OUTOFSCOPE', 'OUTOFSCOPE', 'Out of Scope'),
    ('UNKNOWN', 'UNKNOWN', 'Unknown (Diagnosis not complete)'),
)

CONTACT_SAFETY = Choices(
    # constant, db_id, friendly string
    ('SAFE', 'SAFE', 'Safe to contact'),
    ('DONT_CALL', 'DONT_CALL', 'Not safe to call'),
    ('NO_MESSAGE', 'NO_MESSAGE', 'Not safe to leave a message'),
)

EMAIL_SAFETY = Choices(
    # constant, db_id, friendly string
    ('SAFE', 'SAFE', 'Safe to email'),
    ('DONT_EMAIL', 'DONT_EMAIL', 'Not safe to email'),
)

EXEMPT_USER_REASON = Choices(
    # constant, db_id, friendly string
    ('ECHI', 'ECHI', 'Client is a child'),
    ('EDET', 'EDET', 'Client is in detention'),
    ('EPRE', 'EPRE', '12 month exemption'),
)

ECF_OPTIONS = [
    {
        'key': 'XFER_TO_RECORDED_MESSAGE',
        'label': 'Transferring inbound call to recorded message? Read out the following statement:',
        'text': '"On closing this call you will hear a recorded message which will contain information to highlight limited circumstances in which legal aid may still be available to you. Thank you [client name] for calling Civil Legal Advice. Goodbye"'
    },
    {
        'key': 'READ_OUT_MESSAGE',
        'label': 'Outbound call? Read out the following statement:',
        'text': '"Legal aid may be available in exceptional circumstances to people whose cases are out of scope where a refusal to fund would breach Human Rights or enforceable European law. You could seek advice from a legal advisor about whether an application might succeed in your case and how to make one. Thank you for calling Civil Legal Advice. Goodbye"'
    },
    {
        'key': 'PROBLEM_NOT_SUITABLE',
        'label': 'Problem not suitable for ECF message',
        'text': ''
    },
    {
        'key': 'CLIENT_TERMINATED',
        'label': 'Could not provide - client terminated call',
        'text': ''
    }
]

ECF_STATEMENT = Choices(
    # constant, db_id, friendly string
    *[(x['key'], x['key'], x['text']) for x in ECF_OPTIONS]
)


FEEDBACK_ISSUE = Choices(
    # constant, db_id, friendly string
    ('ADVISOR_CONDUCT','ADCO', 'Advisor conduct'),
    ('ACCESS_PROBLEMS','ACPR', 'Access problems'),
    ('ALREADY_RECEIVING_ADVICE','ARRA', 'Already receiving/received advice'),
    ('WRONG_CATEGORY','COLI', 'Category of law is incorrect'),
    ('DELAY_ADVISING_LACK_OF_FOLLOWUP_INFORMATION','DLAY', 'Delay in advising (lack of follow up information)'),
    ('DELAY_ADVISING_OTHER','DLAO', 'Delay in advising (other)'),
    ('INCORRECT_ELIGIBILITY_CALCULATION', 'INEL', 'Incorrect eligibility calculation'),
    ('INCORRECT_DIAGNOSIS', 'INDI', 'Incorrect diagnosis (out of scope)'),
    ('INCORRECT_INFO_DIAGNOSIS', 'INIP', 'Incorrect information provided (diagnosis)'),
    ('INCORRECT_XFER_PROVIDER', 'INTC', 'Incorrect transferring of calls (provider)'),
    ('INCORRECT_XFER_BACKDOOR', 'INFB', 'Incorrect transferring of calls (front/back)'),
    ('INCORRECT_OR_MISSING_PERSONAL_DETAILS', 'IMCD', 'Incorrect/missing contact details or DOB'),
    ('OTHER_DATA_ENTRY_ERROR', 'ODDE', 'Other data entry errors'),
    ('SYSTEM_ERROR', 'SESE', 'System Error'),
    ('OTHER', 'OTHR', 'Other'),
)


SOCKETIO_CLIENT_CONFIG = {
    'SOCKETIO_SERVER_URL': env.get('SOCKETIO_SERVER_URL', 'http://localhost:8005')
}


CASE_SOURCE = Choices(
    # constant, db_id, friendly string
    ('PHONE', 'PHONE', 'Phone'),
    ('VOICEMAIL', 'VOICEMAIL', 'Voicemail'),
    ('SMS', 'SMS', 'Sms'),
    ('WEB', 'WEB', 'Web')
)


GENDERS = Choices(
    # constant, db_id, friendly string
    ('MALE', 'Male', 'Male'),
    ('FEMALE', 'Female', 'Female'),
    ('PNS', 'Prefer not to say', 'Prefer not to say'),
)


ETHNICITIES = Choices(
    # constant, db_id, friendly string
    ('ASIAN_BANGLADESHI', 'Asian or Asian British Bangladeshi', 'Asian or Asian British Bangladeshi'),
    ('ASIAN_INDIAN', 'Asian or Asian British Indian', 'Asian or Asian British Indian'),
    ('ASIAN_OTHER', 'Asian or Asian British Other', 'Asian or Asian British Other'),
    ('ASIAN_PAKISTANI', 'Asian or Asian British Pakistani', 'Asian or Asian British Pakistani'),
    ('BLACK_AFRICAN', 'Black or Black British African', 'Black or Black British African'),
    ('BLACK_CARIBBEAN', 'Black or Black British Caribbean', 'Black or Black British Caribbean'),
    ('BLACK_OTHER', 'Black or Black British Other', 'Black or Black British Other'),
    ('CHINESE', 'Chinese', 'Chinese'),
    ('MIXED_OTHER', 'Mixed Other', 'Mixed Other'),
    ('MIXED_ASIAN', 'Mixed White and Asian', 'Mixed White and Asian'),
    ('MIXED_BLACK_AFRICAN', 'Mixed White and Black African', 'Mixed White and Black African'),
    ('MIXED_BLACK_CARIBBEAN', 'Mixed White and Black Caribbean', 'Mixed White and Black Caribbean'),
    ('OTHER', 'Other', 'Other'),
    ('PNS', 'Prefer not to say', 'Prefer not to say'),
    ('WHITE_BRITISH', 'White British', 'White British'),
    ('WHITE_IRISH', 'White Irish', 'White Irish'),
    ('GYPSY', 'Gypsy/Traveller', 'Gypsy/Traveller'),
    ('NOT_ASKED', 'Client Not Asked', 'Client Not Asked'),
)


RELIGIONS = Choices(
    # constant, db_id, friendly string
    ('CHRISTIAN', 'Christian', 'Christian'),
    ('BUDDHIST', 'Buddhist', 'Buddhist'),
    ('HINDU', 'Hindu', 'Hindu'),
    ('JEWISH', 'Jewish', 'Jewish'),
    ('MUSLIM', 'Muslim', 'Muslim'),
    ('SIKH', 'Sikh', 'Sikh'),
    ('OTHER', 'other ', 'other '),
    ('NO_RELIGION', 'No religion', 'No religion'),
    ('PNS', 'Prefer not to say', 'Prefer not to say'),
)


SEXUAL_ORIENTATIONS = Choices(
    # constant, db_id, friendly string
    ('BISEXUAL', 'Bisexual', 'Bisexual'),
    ('GAY_MAN', 'Gay man', 'Gay man'),
    ('GAY_WOMAN', 'Gay woman', 'Gay woman'),
    ('OTHER', 'Other', 'Other'),
    ('HETEROSEXUAL', 'Heterosexual', 'Heterosexual'),
    ('PNS', 'Prefer Not To Say', 'Prefer Not To Say'),
)


DISABILITIES = Choices(
    # constant, db_id, friendly string
    ('NCD', 'NCD - Not Considered Disabled', 'NCD - Not Considered Disabled'),
    ('MHC', 'MHC - Mental Health Condition', 'MHC - Mental Health Condition'),
    ('LDD', 'LDD - Learning Disability/Difficulty', 'LDD - Learning Disability/Difficulty'),
    ('ILL', 'ILL - Long-Standing Illness Or Health Condition', 'ILL - Long-Standing Illness Or Health Condition'),
    ('OTH', 'OTH - Other', 'OTH - Other'),
    ('UKN', 'UKN - Unknown', 'UKN - Unknown'),
    ('MOB', 'MOB - Mobility impairmentDEA - Deaf', 'MOB - Mobility impairmentDEA - Deaf'),
    ('HEA', 'HEA - Hearing impaired ', 'HEA - Hearing impaired '),
    ('VIS', 'VIS - Visually impaired', 'VIS - Visually impaired'),
    ('BLI', 'BLI - Blind', 'BLI - Blind'),
    ('PNS', 'PNS - Prefer not to say', 'PNS - Prefer not to say'),
)
