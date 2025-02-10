class USFValidator:
    def __init__(self, data):
        self.data = data

    def validate(self):
        """校验USF数据格式"""
        if not isinstance(self.data, dict):
            return False
        if "subjects" not in self.data or "schedule" not in self.data:
            return False
        return True
