from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask import jsonify
from db import db
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from schemas import EventUpdateSchema, PlainEventSchema
from  models import EventModel


blp = Blueprint("events", __name__, description="Operations on events")

@blp.route('/event')
class Events(MethodView):

    @blp.response(200, PlainEventSchema(many=True))
    def get(self):
        return EventModel.query.all()


    @blp.arguments(PlainEventSchema)
    @blp.response(201,PlainEventSchema)
    def post(self, event_data):
        
        postEvent = EventModel(**event_data)

        try:
            db.session.add(postEvent)
            db.session.commit()

        except SQLAlchemyError: 
            abort(500, message="An error occurred while inserting the Event.")

        return postEvent


    @blp.response(201,PlainEventSchema )
    def delete(self):
        
        try: 
            db.session.query(EventModl).delete()
            db.session.commit()
            return jsonify({"Message": f"Event with the ID of {event_id} has been deleted successfully"})
                  
        except SQLAlchemyError: 
            abort(500, message="An error occurred while deleting the Event.")


    
# THIS IS THE EVENT ID METHODVIEW 

@blp.route('/event/<string:event_id>')
class eventById(MethodView):

    @blp.response(201,PlainEventSchema)
    def get(self, event_id):
       getEventId = EventModel.query.get_or_404(event_id)
       
       return getEventId

    @blp.response(201, PlainEventSchema)
    def delete(self, event_id):
        deletEventId = EventModel.query.get_or_404(event_id)
        
        try:
            db.session.delete(deletEventId)
            db.session.commit()
    
        
        except SQLAlchemyError:
             abort(500, message="An error occurred while deleting this Event.")

        return deletEventId


    @blp.arguments(EventUpdateSchema)
    @blp.response(200, PlainEventSchema)
    def put(self, event_data , event_id):
        updateEvents = EventModel.query.get(event_id)
        
        
        if updateEvents:
            updateEvents.eventName = event_data['eventName']
            updateEvents.location  = event_data['location']
            updateEvents.timestamp = event_data['timestamp']
            
            
        else: updateEvents = ItemModel(id=event_id, **event_data)
        
        
        try:
            db.session.add(updateEvents)
            db.session.commit()
        
        
        except SQLAlchemyError:
            abort(500, message="An event as been updated successfully")
            
            
            return updateEvents


