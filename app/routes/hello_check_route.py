from flask import Blueprint, request, jsonify


hello_check_bp = Blueprint("hello_check_bp",__name__)

@hello_check_bp.route("/")
def hello_check():
    return jsonify({"data":{"verion":"v0.0.0"},
    "msg":"ok"})