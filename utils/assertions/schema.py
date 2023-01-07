import allure
from jsonschema import validate


@allure.step('Validating schema')
def validate_schema(instance: dict, schema: dict) -> None:
    validate(instance=instance, schema=schema)
