import json

class USFGenerator:
    def __init__(self, version=1):
        """
        Initialize USF Generator.

        Args:
            version (int, optional): USF format version. Defaults to 1.
        """
        self.version = version
        self.subjects = {}
        self.periods = []
        self.timetable = []

    def add_subject(self, name, simplified_name=None, teacher=None, room=None):
        """
        Add a subject to USF.

        Args:
            name (str): Subject name.
            simplified_name (str, optional): Shortened subject name.
            teacher (str, optional): Teacher's name.
            room (str, optional): Classroom.
        """
        self.subjects[name] = {
            "simplified_name": simplified_name or name,
            "teacher": teacher or "",
            "room": room or "",
        }

    def add_period(self, start_time, end_time):
        """
        Add a class period to USF.

        Args:
            start_time (str): Start time (HH:MM:SS).
            end_time (str): End time (HH:MM:SS).

        Returns:
            int: Index of the added period (1-based).
        """
        self.periods.append([start_time, end_time])
        return len(self.periods)  # Return 1-based index

    def add_schedule(self, day, week_type, subject, period_index):
        """
        Add a schedule entry.

        Args:
            day (int): Day of the week (1=Monday, ..., 7=Sunday).
            week_type (str): "all", "even", or "odd".
            subject (str): Subject name (must exist in subjects).
            period_index (int): Index of the period (1-based).
        """
        if subject not in self.subjects:
            raise ValueError(f"Subject '{subject}' is not defined.")
        if period_index < 1 or period_index > len(self.periods):
            raise ValueError(f"Invalid period index {period_index}.")
        self.timetable.append([day, week_type, subject, period_index])

    def generate(self):
        """
        Generate USF data as a dictionary.

        Returns:
            dict: USF formatted data.
        """
        return {
            "version": self.version,
            "subjects": self.subjects,
            "periods": self.periods,
            "timetable": self.timetable,
        }

    def save_to_file(self, filename):
        """
        Save USF data to a JSON file.

        Args:
            filename (str): Output filename.
        """
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(self.generate(), f, indent=2, ensure_ascii=False)