from marshmallow import Schema, fields
import marshmallow as ma

    
class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    email = fields.Str(required=True)
    fullname = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)
    timestamp = ma.fields.DateTime(required=True) 