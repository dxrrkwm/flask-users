from marshmallow import fields, validate

from app.extensions import ma
from app.models import User


class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User
        load_instance: bool = True

    id: fields.Integer = ma.auto_field(dump_only=True)
    name: fields.String = fields.String(required=True, validate=validate.Length(min=1, max=100))
    email: fields.Email = fields.Email(required=True, validate=validate.Length(max=120))
    created_at: fields.DateTime = fields.DateTime(dump_only=True)
