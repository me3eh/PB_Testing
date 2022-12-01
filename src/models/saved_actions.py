class SavedActions:
    def __init__(self, bdd_attribute, action_name):
        self.bdd_attribute = bdd_attribute
        self.action_name = action_name

    def information_for_saved_actions(self):
        return f'{self.bdd_attribute}: {self.action_name}'
