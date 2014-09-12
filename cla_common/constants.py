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


EXEMPT_USER_REASON = Choices(
    # constant, db_id, friendly string
    ('ECHI', 'ECHI', 'Client is a child'),
    ('EDET', 'EDET', 'Client is in detention'),
    ('EPRE', 'EPRE', '12 month exemption'),
)

ECF_STATEMENT = Choices(
    # constant, db_id, friendly string
    ('XFER_TO_RECORDED_MESSAGE','XFER_TO_RECORDED_MESSAGE', '"On closing this call you will hear a recorded message which will contain information to highlight limited circumstances in which legal aid may still be available to you. Thank you [client name] for calling Civil Legal Advice. Goodbye"'),
    ('READ_OUT_MESSAGE', 'READ_OUT_MESSAGE', '"Legal aid may be available in exceptional circumstances to people whose cases are out of scope where a refusal to fund would breach Human Rights or enforceable European law. You could seek advice from a legal advisor about whether an application might succeed in your case and how to make one. Thank you for calling Civil Legal Advice. Goodbye"'),
    ('PROBLEM_NOT_SUITABLE', 'PROBLEM_NOT_SUITABLE', 'Problem not suitable for ECF message'),
    ('CLIENT_TERMINATED', 'CLIENT_TERMINATED', 'Could not provide - client terminated call'),
)


FEEDBACK_ISSUE = Choices(
    # constant, db_id, friendly string
    ('ADVISOR_CONDUCT','ADVISOR_CONDUCT', 'Advisor conduct'),
    ('ACCESS_PROBLEMS','ACCESS_PROBLEMS', 'Access problems'),
    ('ALREADY_RECEIVING_ADVICE','ALREADY_RECEIVING_ADVICE', 'Already receiving/received advice'),
    ('WRONG_CATEGORY','WRONG_CATEGORY', 'Category of law is incorrect'),
    ('DELAY_ADVISING_LACK_OF_FOLLOWUP_INFORMATION','DELAY_ADVISING_LACK_OF_FOLLOWUP_INFORMATION', 'Delay in advising (lack of follow up information)'),
    ('DELAY_ADVISING_OTHER','DELAY_ADVISING_OTHER', 'Delay in advising (other)'),
    ('INCORRECT_ELIGIBILITY_CALCULATION', 'INCORRECT_ELIGIBILITY_CALCULATION', 'Incorrect eligibility calculation'),
    ('INCORRECT_DIAGNOSIS', 'INCORRECT_DIAGNOSIS', 'Incorrect diagnosis (out of scope)'),
    ('INCORRECT_INFO_DIAGNOSIS', 'INCORRECT_INFO_DIAGNOSIS', 'Incorrect information provided (diagnosis)'),
    ('INCORRECT_XFER_PROVIDER', 'INCORRECT_XFER_PROVIDER', 'Incorrect transferring of calls (provider)'),
    ('INCORRECT_XFER_BACKDOOR', 'INCORRECT_XFER_BACKDOOR', 'Incorrect transferring of calls (front/back)'),
    ('INCORRECT_OR_MISSING_PERSONAL_DETAILS', 'INCORRECT_OR_MISSING_PERSONAL_DETAILS', 'Incorrect/missing contact details or DOB'),
    ('OTHER_DATA_ENTRY_ERROR', 'OTHER_DATA_ENTRY_ERROR', 'Other data entry errors'),
    ('SYSTEM_ERROR', 'SYSTEM_ERROR', 'System Error'),
    ('OTHER', 'OTHER', 'Other'),
)

SOCKETIO_CLIENT_CONFIG = {
    'SOCKETIO_SERVER_URL': env.get('SOCKETIO_SERVER_URL', 'http://localhost:8005')
}
