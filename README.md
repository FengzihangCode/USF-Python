# USF-Python
USF Access Framework for Python

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

### Reading a USF file
```python
import usf

data = usf.read("schedule.usf")
if usf.is_valid(data):
    print("Valid USF file")
    subjects = usf.get_subjects(data)
    print(subjects)
else:
    print("Invalid USF file")
```

### Creating a USF file
```python
schedule = usf.create()

definition = {
    "name": "Mathematics",
    "teacher": "Dr. Smith",
    "location": "Room 101",
    "time": [(1, 2)],  # Periods
    "week": "all"  # Every week
}
usf.add_subject(schedule, definition)
usf.save(schedule, "my_schedule.usf")
```

### Adding a Course to an Existing USF File
```python
data = usf.read("schedule.usf")
usf.add_subject(data, {
    "name": "Physics",
    "teacher": "Prof. Johnson",
    "location": "Room 203",
    "time": [(3, 4)],
    "week": "odd"
})
usf.save(data, "updated_schedule.usf")
```

### Generating a USF File from Scratch
```python
schedule = usf.create()
usf.add_subject(schedule, {
    "name": "Computer Science",
    "teacher": "Ms. Lee",
    "location": "Lab 2",
    "time": [(5, 6)],
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
    "subjects": [
        {
            "name": "Mathematics",
            "teacher": "Dr. Smith",
            "location": "Room 101",
            "time": [[1, 2]],
            "week": "all"
        }
    ]
}
```

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests on GitHub.

## License
This project is licensed under the MIT License.

