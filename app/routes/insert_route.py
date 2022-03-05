from flask import jsonify, Blueprint, request
from app.schemas.users import Users
from app import db
from werkzeug.security import generate_password_hash

insert_bp =Blueprint("insert_bp",__name__,url_prefix="/api/v1")

@insert_bp.route("/insert/",methods=["POST","GET"])
def insert():
    if request.method == "POST":
        name = request.get_json().get("name",None)
        password = request.get_json().get("password",None)
        hashed_pw = generate_password_hash(password, method="sha256")
        new_user = Users(name=name, password=hashed_pw)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"data":f"name :{name}",
        "msg":"ok"})
    return jsonify({"data":"To insert a Posts make a POST HTTP Action",
    "msg":"Wrong Method"})