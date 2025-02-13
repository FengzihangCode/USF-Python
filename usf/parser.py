import json

class USFParser:
    def __init__(self, filename):
        """
        Initialize USF Parser.

        Args:
            filename (str): Path to USF JSON file.
        """
        try:
            with open(filename, "r", encoding="utf-8") as f:
                self.data = json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"File '{filename}' not found.")
        except json.JSONDecodeError:
            raise ValueError(f"Failed to decode JSON from the file '{filename}'.")

    def get_subjects(self):
        """Return the subjects dictionary."""
        return self.data.get("subjects", {})

    def get_periods(self):
        """Return the list of periods."""
        return self.data.get("periods", [])

    def get_timetable(self):
        """Return the timetable list."""
        return self.data.get("timetable", [])