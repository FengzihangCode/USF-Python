import json

class USFGenerator:
    def __init__(self):
        self.data = {"subjects": [], "schedule": []}

    def add_subject(self, name, teacher, location):
        """添加课程"""
        subject = {"name": name, "teacher": teacher, "location": location}
        self.data["subjects"].append(subject)

    def add_schedule(self, subject_index, day, time, week_rule="all"):
        """添加课程表项"""
        schedule_item = {
            "subject_index": subject_index,
            "day": day,
            "time": time,
            "week_rule": week_rule
        }
        self.data["schedule"].append(schedule_item)

    def save(self, filename):
        """保存USF文件"""
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(self.data, f, ensure_ascii=False, indent=2)
