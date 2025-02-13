import json
import jsonschema
from jsonschema import validate

class USFValidator:
    def __init__(self, schema_file="schema.json"):
        """
        Initialize USF Validator.

        Args:
            schema_file (str, optional): Path to JSON Schema. Defaults to "schema.json".
        """
        try:
            with open(schema_file, "r", encoding="utf-8") as f:
                self.schema = json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"Schema file '{schema_file}' not found.")
        except json.JSONDecodeError:
            raise ValueError(f"Failed to decode JSON from the schema file '{schema_file}'.")

    def validate(self, data):
        """
        Validate USF data.

        Args:
            data (dict): USF formatted dictionary.

        Returns:
            bool: True if valid, raises an error if invalid.
        """
        try:
            validate(instance=data, schema=self.schema)
        except jsonschema.exceptions.ValidationError as e:
            raise ValueError(f"USF data validation failed: {e.message}")
        return True