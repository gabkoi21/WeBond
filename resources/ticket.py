from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask import jsonify
from db import db
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from schemas import plainTicketSchema, TicketSchema, TicketUpdateSchema
from  models import TicketModel


blp = Blueprint("ticket", __name__, description="Operations on events")

@blp.route("/ticket")
class Ticket(MethodView):

    @blp.response(200, TicketSchema(many=True))
    def get(self):
        return TicketModel.query.all()


    @blp.arguments(TicketSchema)
    @blp.response(200, TicketSchema)
    def post(self, ticket_data):
        
        ticket = TicketModel(**ticket_data)

        try: 
            db.session.add(ticket)
            db.session.commit()

        except SQLAlchemyError: 
            abort(500, message="An error occurred while inserting the ticket.")
            
            return ticket


@blp.route('/ticket/<string:ticket_id>')
class ticketByID(MethodView):

    @blp.response(201, TicketSchema)
    def get(self, ticket_id):
        
        getTicketId = TicketModel.query.get_or_404(ticket_id)
        
        return getTicketId 

    @blp.response(201, TicketSchema)
    def delete(self, ticket_id):

        deleteTicket = TicketModel.query.get_or_404(ticket_id)

        try:
            db.session.delete(deleteTicket)
            db.session.commit()

        except SQLAlchemyError: 
            abort(500, message="An error occurred while delete the ticket.")
            
            return deleteTicket


    @blp.arguments(TicketUpdateSchema)
    @blp.response(201, TicketSchema)

    def put(self, ticket_data , ticket_id):
        updateTicket = TicketModel.query.get_or_404(ticket_id)
        
        if updateTicket:
            updateTicket.price = ticket_data["price"] 
            updateTicket.quantity = ticket_data["quantity"] 
            updateTicket.timestamp = ticket_data["timestamp"] 
             
             
        else: updateTicket = ItemModel(id=ticket_id, **ticket_data)  #
             
        try: 
            db.session.add(updateTicket)
            db.session.commit()
            
            
        except SQLAlchemyError: 
            abort(500, message="An error occurred while updating the ticket.")
            
            
            return updateTicket




