import json
import unittest
from usf.generator import USFGenerator
from usf.parser import USFParser
from usf.validator import USFValidator

class TestUSF(unittest.TestCase):
    def setUp(self):
        """初始化测试用例"""
        self.generator = USFGenerator(version=1)

        # 添加科目
        self.generator.add_subject("Mathematics", simplified_name="Math", teacher="Dr. Smith", room="Room 101")
        self.generator.add_subject("Physics", simplified_name="Phys", teacher="Dr. Johnson", room="Room 102")

        # 添加时间段（每天适用）
        self.generator.add_period("08:00:00", "09:30:00")  # 第一节课
        self.generator.add_period("10:00:00", "11:30:00")  # 第二节课

        # 添加课程表（星期一的第一节课为数学，第二节课为物理）
        self.generator.add_schedule(1, "all", "Mathematics", 1)  # 星期一，第一节，数学
        self.generator.add_schedule(1, "all", "Physics", 2)      # 星期一，第二节，物理

        # 生成 USF 数据
        self.usf_data = self.generator.generate_usf_data()

    def test_usf_generation(self):
        """测试 USF 生成"""
        self.assertIn("version", self.usf_data)
        self.assertIn("subjects", self.usf_data)
        self.assertIn("periods", self.usf_data)
        self.assertIn("timetable", self.usf_data)

        self.assertEqual(self.usf_data["version"], 1)
        self.assertEqual(len(self.usf_data["subjects"]), 2)
        self.assertEqual(len(self.usf_data["periods"]), 2)
        self.assertEqual(len(self.usf_data["timetable"]), 2)

    def test_usf_parser(self):
        """测试 USF 解析"""
        json_data = json.dumps(self.usf_data, indent=2)
        parser = USFParser(json_data)

        self.assertEqual(len(parser.get_subjects()), 2)
        self.assertEqual(len(parser.get_periods()), 2)
        self.assertEqual(len(parser.get_timetable()), 2)

        # 验证解析出的数据是否正确
        subjects = parser.get_subjects()
        self.assertEqual(subjects["Mathematics"]["teacher"], "Dr. Smith")
        self.assertEqual(subjects["Physics"]["room"], "Room 102")

    def test_usf_validation(self):
        """测试 USF 校验"""
        validator = USFValidator()

        # 校验正确的数据
        self.assertTrue(validator.validate(self.usf_data))

        # 校验错误的数据（缺少 timetable）
        invalid_data = {
            "version": 1,
            "subjects": self.usf_data["subjects"],
            "periods": self.usf_data["periods"]
        }
        self.assertFalse(validator.validate(invalid_data))

if __name__ == "__main__":
    unittest.main()