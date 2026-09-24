class Choices(object):
    def __init__(self, *choices, **kwargs):
        self.CHOICES = tuple()
        self.CHOICES_DICT = {}
        self.REVERTED_CHOICES_DICT = {}
        self.CHOICES_CONST_DICT = {}
        self.REVERTED_CHOICES_CONST_DICT = {}

        name = kwargs.get("name", "CHOICES")
        if name != "CHOICES":
            self.add_choices(name, *choices)
        else:
            self._build_choices(*choices)

    def __contains__(self, item):
        return item in self.CHOICES_DICT

    def __iter__(self):
        return iter(self.CHOICES)

    def _build_choices(self, *choices):
        choice_values = list(self.CHOICES)
        for choice in choices:
            constant, value, display = choice
            if hasattr(self, constant):
                raise ValueError("You cannot declare two constants with the same name! %s" % repr(choice))
            if value in self.CHOICES_DICT:
                raise ValueError("You cannot declare two constants with the same value! %s" % repr(choice))

            setattr(self, constant, value)
            choice_values.append((value, display))
            self.CHOICES_DICT[value] = display
            self.REVERTED_CHOICES_DICT[display] = value
            self.CHOICES_CONST_DICT[constant] = value
            self.REVERTED_CHOICES_CONST_DICT[value] = constant

        self.CHOICES = tuple(choice_values)

    def add_choices(self, name="CHOICES", *choices):
        self._build_choices(*choices)
        if name != "CHOICES":
            self.add_subset(name, [choice[0] for choice in choices])

    def add_subset(self, name, constants):
        if hasattr(self, name):
            raise ValueError("Cannot use %s as a subset name. It is already an attribute." % name)

        subset = []
        subset_dict = {}
        reversed_subset_dict = {}
        subset_const_dict = {}
        reversed_subset_const_dict = {}

        for constant in constants:
            value = getattr(self, constant)
            display = self.CHOICES_DICT[value]
            subset.append((value, display))
            subset_dict[value] = display
            reversed_subset_dict[display] = value
            subset_const_dict[constant] = value
            reversed_subset_const_dict[value] = constant

        setattr(self, name, tuple(subset))
        setattr(self, "%s_DICT" % name, subset_dict)
        setattr(self, "REVERTED_%s_DICT" % name, reversed_subset_dict)
        setattr(self, "%s_CONST_DICT" % name, subset_const_dict)
        setattr(self, "REVERTED_%s_CONST_DICT" % name, reversed_subset_const_dict)
