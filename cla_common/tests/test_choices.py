from unittest import TestCase

from cla_common.choices import Choices


class ChoicesTest(TestCase):
    def test_choices_expose_legacy_api(self):
        choices = Choices(("UNKNOWN", "unknown", "Unknown"), ("YES", "yes", "Yes"))

        self.assertEqual(choices.YES, "yes")
        self.assertEqual(choices.CHOICES, (("unknown", "Unknown"), ("yes", "Yes")))
        self.assertEqual(choices.CHOICES_DICT["yes"], "Yes")
        self.assertEqual(choices.REVERTED_CHOICES_DICT["Yes"], "yes")
        self.assertEqual(choices.CHOICES_CONST_DICT["YES"], "yes")
        self.assertEqual(choices.REVERTED_CHOICES_CONST_DICT["yes"], "YES")
        self.assertIn("yes", choices)
        self.assertEqual(list(choices), list(choices.CHOICES))

    def test_choices_support_subsets(self):
        choices = Choices(("UNKNOWN", "unknown", "Unknown"), ("YES", "yes", "Yes"))

        choices.add_subset("KNOWN", ("YES",))

        self.assertEqual(choices.KNOWN, (("yes", "Yes"),))
        self.assertEqual(choices.KNOWN_CONST_DICT["YES"], "yes")
