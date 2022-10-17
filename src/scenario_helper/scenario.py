class Scenario:
    def __init__(self,
                 scenario_name="something",
                 givens=None,
                 whens=None,
                 thens=None):

        self.scenario_name = scenario_name
        if givens is None:
            givens = ["some action"]
        if whens is None:
            whens = ["something happening"]
        if thens is None:
            thens = ["something will be triggered"]

        self.givens = givens
        self.whens = whens
        self.thens = thens

    def set_scenario_name(self, scenario_name):
        self.scenario_name = scenario_name

    def set_when(self, when_text, index):
        self.whens[index] = when_text

    def set_then(self, then_text, index):
        self.thens[index] = then_text

    def set_given(self, given_text, index):
        self.givens[index] = given_text

    def get_scenario_name(self):
        return self.scenario_name

    def get_when(self, index):
        return self.whens[index]

    def get_then(self, index):
        return self.thens[index]

    def get_given(self, index):
        return self.givens[index]

    def get_whens(self):
        return self.whens

    def get_thens(self):
        return self.thens

    def get_givens(self):
        return self.givens

    def add_given(self):
        self.givens.append("some action")

    def add_when(self):
        self.whens.append("something happening")

    def add_then(self):
        self.thens.append("something will be triggered")

    def remove_given(self):
        self.givens.pop()

    def remove_when(self):
        self.whens.pop()

    def remove_then(self):
        self.thens.pop()

    def remove_given_index(self, index):
        self.givens.pop(index)

    def remove_when_index(self, index):
        self.whens.pop(index)

    def remove_then_index(self, index):
        self.thens.pop(index)

    def get_as_string(self):
        whole_text = f"\tScenario: {self.scenario_name}\n"
        test_elements = [self.givens, self.whens, self.thens]
        prefixes = ['Given', 'When', 'Then']
        for index in range(3):
            whole_text += self.convert_array_to_string(test_elements[index], prefixes[index])
        return whole_text

    def convert_array_to_string(self, array, prefix):
        converted_string = ""
        for index, element in enumerate(array):
            if index == 0:
                converted_string += f"\t\t{prefix} {element}\n"
            else:
                converted_string += f"\t\tAnd {element}\n"
        return converted_string
