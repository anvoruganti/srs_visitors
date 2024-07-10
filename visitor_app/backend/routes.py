from flask import jsonify, request # type: ignore
from backend.models import VisitorModel

def init_routes(app):
    @app.route('/visitor_pass/<new_id>', methods=['GET'])
    def get_visitor_pass(new_id):
        visitor = VisitorModel.get_visitor(new_id)
        if visitor:
            visitor['_id'] = str(visitor['_id'])
            return jsonify({
                "TouristResponse": {
                    "Status": 0,
                    "Message": "Visitor pass found",
                    "ErrorMessage": ""
                },
                "VisitorPass": visitor
            }), 200
        else:
            return jsonify({
                "TouristResponse": {
                    "Status": 1,
                    "Message": "Visitor pass not found",
                    "ErrorMessage": "No visitor pass found for the given NewId"
                },
                "VisitorPass": None
            }), 404

    @app.route('/visitor_checkin', methods=['POST'])
    def update_visitor_checkin():
        data = request.json
        if not data or 'NewId' not in data:
            return jsonify({
                "TouristResponse": {
                    "Status": 1,
                    "Message": "Invalid data format",
                    "ErrorMessage": "NewId is required"
                }
            }), 400
        
        new_id = data['NewId']
        visitor = VisitorModel.get_visitor(new_id)
        
        if not visitor:
            return jsonify({
                "TouristResponse": {
                    "Status": 1,
                    "Message": "Visitor pass not found",
                    "ErrorMessage": "No visitor pass found for the given NewId"
                }
            }), 404
        
        if visitor.get('IsCheckedIn', False):
            return jsonify({
                "TouristResponse": {
                    "Status": 1,
                    "Message": "Already checked in",
                    "ErrorMessage": "This visitor has already been checked in"
                },
                "VisitorPass": visitor
            }), 409
        
        result = VisitorModel.check_in_visitor(new_id)
        
        if result.modified_count > 0:
            updated_visitor = VisitorModel.get_visitor(new_id)
            updated_visitor['_id'] = str(updated_visitor['_id'])
            return jsonify({
                "TouristResponse": {
                    "Status": 0,
                    "Message": "Visitor checked in successfully",
                    "ErrorMessage": ""
                },
                "VisitorPass": updated_visitor
            }), 200
        else:
            return jsonify({
                "TouristResponse": {
                    "Status": 1,
                    "Message": "Check-in failed",
                    "ErrorMessage": "Failed to update check-in status"
                }
            }), 500