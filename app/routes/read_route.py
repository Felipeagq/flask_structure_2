from app import db
from app.schemas.users import Users
from flask import Blueprint, jsonify, request

read_bp = Blueprint("read_bp",__name__,url_prefix="/api/v1")

@read_bp.route("/read")
def read():
    users = Users.query.all()
    data = []
    for user in users:
        data.append([user.name,user.password])
    return jsonify({"data":data,
    "msg":"ok"})