class Scenario:
    def __init__(self):
        self.scenario_name = "Scenario: something"
        self.given = "Given some action"
        self.when = "When something happening "
        self.then = "Then something will be triggered"

    def set_scenario_name(self, scenario_name):
        self.scenario_name = 'Scenario: ' + scenario_name

    def set_when(self, when):
        self.when = 'When ' + when

    def set_then(self, then):
        self.then = 'Then ' + then

    def set_given(self, given):
        self.given = 'Given ' + given

    def get_scenario_name(self):
        return self.scenario_name

    def get_when(self):
        return self.when

    def get_then(self):
        return self.then

    def get_given(self):
        return self.given
