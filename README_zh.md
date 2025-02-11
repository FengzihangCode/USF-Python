# USF-Python
语言：<a href="./README.md">English</a>｜简体中文

适用于 Python 的 USF 访问框架

[![Upload Python Package](https://github.com/USF-org/USF-Python/actions/workflows/python-publish.yml/badge.svg)](https://github.com/USF-org/USF-Python/actions/workflows/python-publish.yml)

当最新的 Release 仅包含文档更新时，提交到 PyPI 会失败

## 介绍
USF-Python 是为效率与通用性而生的 Python 访问框架

## 功能
- **轻量紧凑**: 专为高效存储和快速解析进行了优化
- **支持课程表**: 存储课程名称、教师、场地、时间段和周规则
- **弹性周支持**: 支持“每周”、“奇数周”和“偶数周”周规则
- **简单的 API**: 易于阅读、写入和操作
- **跨平台**: 适用于所有支持 Python 的平台

## 安装
你可以通过 **pip** 安装
```sh
pip install usf
```
或在本地通过如下代码安装
```sh
python setup.py install
```

## 使用示例
```python
import usf

# Reading a USF file
data = usf.read("schedule.usf")
if usf.is_valid(data):
    print("Valid USF file")
    subjects = usf.get_subjects(data)
    print(subjects)
else:
    print("Invalid USF file")

# Creating a USF file
# Initialize the USF Generator (version 1 by default)
usf_generator = usf.USFGenerator()

# Add subjects
usf_generator.add_subject("Mathematics", simplified_name="Math", teacher="Dr. Smith", room="Room 101")
usf_generator.add_subject("Physics", simplified_name="Phys", teacher="Prof. Johnson", room="Room 203")

# Add class periods
usf_generator.add_period("08:00:00", "09:30:00")
usf_generator.add_period("10:00:00", "11:30:00")

# Add schedule entries
usf_generator.add_schedule(day=1, week_type="all", subject="Mathematics", period_index=1)  # Monday
usf_generator.add_schedule(day=2, week_type="odd", subject="Physics", period_index=2)  # Tuesday (Odd Week)

# Generate the USF data and save it to a file
usf_generator.save_to_file("schedule.usf")

# Adding a Course to an Existing USF File
data = usf.read("schedule.usf")
usf.add_subject(data, {
    "name": "Physics",
    "teacher": "Prof. Johnson",
    "location": "Room 203",
    "time": [3, 4],
    "week": "odd"
})
usf.save(data, "updated_schedule.usf")

# Generating a USF File from Scratch
schedule = usf.create()
usf.add_subject(schedule, {
    "name": "Computer Science",
    "teacher": "Ms. Lee",
    "location": "Lab 2",
    "time": [5, 6],
    "week": "even"
})
usf.save(schedule, "new_schedule.usf")
```

## USF Format Specification
USF data is structured as a compact array:
- **name**: Course name (string)
- **teacher**: Instructor name (string)
- **location**: Classroom or venue (string)
- **time**: List of tuples representing periods, e.g., `[(1, 2)]` means periods 1 and 2
- **week**: `"all"`, `"even"`, or `"odd"`

Example JSON representation:
```json
{
  "version": 1,
  "subjects": {
    "Mathematics": {
      "simplified_name": "Math",
      "teacher": "Dr. Smith",
      "room": "Room 101"
    },
    "Physics": {
      "simplified_name": "Phys",
      "teacher": "Prof. Johnson",
      "room": "Room 203"
    }
  },
  "periods": [
    ["08:00:00", "09:30:00"],
    ["10:00:00", "11:30:00"]
  ],
  "timetable": [
    [1, "all", "Mathematics", 1],
    [2, "odd", "Physics", 2]
  ]
}
```

## 贡献
欢迎贡献！请随时在GitHub上打开议题或提交PR

## 许可证
该项目根据 MIT 许可证授权

