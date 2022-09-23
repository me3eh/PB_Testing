class Feature:
    def __init__(self):
        self.filename = "new_test"
        self.feature_description = "feature name"

    def get_filename(self):
        return self.filename + ".feature"

    def get_feature_description(self):
        return self.feature_description

    def set_feature_description(self, text):
        self.feature_description = text

    def set_filename(self, text):
        self.filename = text

    def get_as_string(self):
        whole_text = f'Filename: {self.get_filename()}\n\n\n' \
                     f'Feature: {self.get_feature_description()}'
        return whole_text

    def get_as_string_only_feature_description(self):
        whole_text = f'Feature: {self.get_feature_description()}'
        return whole_text

