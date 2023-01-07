from pydantic import BaseModel as PydanticBaseModel


class BaseModel(PydanticBaseModel):
    class Config:
        @staticmethod
        def schema_extra(schema: dict, model: PydanticBaseModel):
            """
            https://github.com/pydantic/pydantic/issues/1270#issuecomment-729555558
            """
            for prop, value in schema.get('properties', {}).items():
                field = [
                    model_field for model_field in model.__fields__.values()
                    if model_field.alias == prop
                ][0]

                if field.allow_none:
                    if 'type' in value:
                        value['anyOf'] = [{'type': value.pop('type')}]

                    elif '$ref' in value:
                        if issubclass(field.type_, BaseModel):
                            value['title'] = field.type_.__config__.title or field.type_.__name__
                        value['anyOf'] = [{'$ref': value.pop('$ref')}]
                    value['anyOf'].append({'type': 'null'})

    def __hash__(self):
        """
        https://github.com/pydantic/pydantic/issues/1303#issuecomment-599712964
        """
        return hash((type(self),) + tuple(self.__dict__.values()))
