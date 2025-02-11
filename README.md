# USF-Python
Language: English｜<a href="./README_zh.md">简体中文</a>
USF Access Framework for Python

[![Upload Python Package](https://github.com/USF-org/USF-Python/actions/workflows/python-publish.yml/badge.svg)](https://github.com/USF-org/USF-Python/actions/workflows/python-publish.yml)

When the newest release only contains description updates, upload to PyPI will be failed.

## Introduction
USF-Python is a Python library that provides access to the USF format for efficiency and universality.

## Features
- **Lightweight & Compact**: Optimized for efficient storage and fast parsing.
- **Supports Course Schedules**: Store course names, instructors, locations, time slots, and week rules.
- **Flexible Week Rules**: Supports "all", "even", and "odd" week patterns.
- **Simple API**: Easy to read, write, and manipulate USF files.
- **Cross-Platform**: Works on all platforms supporting Python.

## Installation
You can simply install the package with **pip**
```sh
pip install usf
```
or install it locally
```sh
python setup.py install
```

## Usage
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

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests on GitHub.

## License
This project is licensed under the MIT License.

