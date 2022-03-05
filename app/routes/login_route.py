
from importlib.metadata import requires
from flask import Blueprint, jsonify, request
from app.schemas.users import Users
from app import db
from werkzeug.security import check_password_hash

login_db = Blueprint("login_bp",__name__,url_prefix="/api/v1")

@login_db.route("/login/",methods=["POST","GET"])
def login():
    if request.method=="POST":
        username = request.get_json().get("username",None)
        userpassword = request.get_json().get("userpassword",None)
        user = Users.query.filter_by(name=username).first()
        print(user.name,user.password)
        if user and check_password_hash(user.password,userpassword):
            return jsonify({"data":f"user {username} you are logged in",
            "msg":"ok"})
        else:
            return jsonify({"data":f"user {username} bad credentials",
            "msg":"ok"})
    return jsonify({"data":f"For login make a post",
            "msg":"ok"})
