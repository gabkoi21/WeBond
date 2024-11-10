from marshmallow import Schema , fields 
import marshmallow as ma

class PlainEventSchema(Schema):
    eventName = ma.fields.Str()
    location = ma.fields.Str()
    timestamp = ma.fields.DateTime()


class plainTicketSchema(Schema):
    id = fields.Str(dump_only=True)
    price = fields.Int(required=True)
    quantity = fields.Int(required=True)
    timestamp = ma.fields.DateTime()
   


class TicketSchema(plainTicketSchema):
    event_id = fields.Int(required=True, load_only=True)
    ticket  = fields.Nested(plainTicketSchema(), dump_only=True)


class EventUpdateSchema(ma.Schema):
    eventName = ma.fields.Str()
    location = ma.fields.Str()
    timestamp = ma.fields.DateTime()


class TicketUpdateSchema(Schema):
    id = fields.Str(dump_only=True)
    price = fields.Int(required=True)
    quantity = fields.Int(required=True)
    timestamp = ma.fields.DateTime()


