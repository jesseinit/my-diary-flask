from marshmallow import Schema, exceptions


class BaseSchema(Schema):
    class Meta:
        ordered = True

    def load_json_into_schema(self, data):
        """Helper function to load raw json(deserialized data) request data
        into schema"""
        from helpers.validations import ValidationError
        try:
            data = self.loads(data)
        except exceptions.ValidationError as e:
            raise ValidationError(
                dict(message=e.messages), 422)

        if errors:
            raise ValidationError(
                dict(errors=errors, message='Validation error occurred'), 400)

        return data

    def load_object_into_schema(self, data, partial=False):
        """Helper function to load python objects into schema"""
        from helpers.validations import ValidationError

        try:
            data = self.load(data, partial=partial)
            return data
        except exceptions.ValidationError as e:
            raise ValidationError(
                dict(message=e.messages), 422)
