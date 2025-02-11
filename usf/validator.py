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
        with open(schema_file, "r", encoding="utf-8") as f:
            self.schema = json.load(f)

    def validate(self, data):
        """
        Validate USF data.

        Args:
            data (dict): USF formatted dictionary.

        Returns:
            bool: True if valid, raises an error if invalid.
        """
        validate(instance=data, schema=self.schema)
        return True
    