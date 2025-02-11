import json

class USFParser:
    def __init__(self, filename):
        """
        Initialize USF Parser.

        Args:
            filename (str): Path to USF JSON file.
        """
        with open(filename, "r", encoding="utf-8") as f:
            self.data = json.load(f)

    def get_subjects(self):
        """Return the subjects dictionary."""
        return self.data.get("subjects", {})

    def get_periods(self):
        """Return the list of periods."""
        return self.data.get("periods", [])

    def get_timetable(self):
        """Return the timetable list."""
        return self.data.get("timetable", [])