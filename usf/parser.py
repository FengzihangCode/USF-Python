import json

class USFParser:
    def __init__(self, usf_file):
        self.usf_file = usf_file
        self.data = None

    def load(self):
        """加载USF文件"""
        with open(self.usf_file, "r", encoding="utf-8") as f:
            self.data = json.load(f)

    def get_subjects(self):
        """获取课程列表"""
        if self.data is None:
            self.load()
        return self.data.get("subjects", [])

    def is_valid(self):
        """检查USF文件是否合法"""
        from .validator import USFValidator
        validator = USFValidator(self.data)
        return validator.validate()
