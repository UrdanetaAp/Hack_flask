from flask import Flask, jsonify, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route("/")
def index():
    return " "


@app.route("/users", methods=['GET'])
def hack1():
    return jsonify({"payload":"success"})


@app.route("/user", methods=['POST'])
def hack2():
    return jsonify({"payload":"success"})


@app.route("/user", methods=['DELETE'])
def hack3():
    return jsonify({'payload':'success'})


@app.route("/user", methods=['PUT'])
def hack4():
    return jsonify({'payload':'success','error':False})


@app.route("/api/v1/users", methods=['GET'])
def hack5():
    return jsonify({"payload":[]})


@app.route("/api/v1/user", methods=['POST'])
def hack6():
    email = request.args.get('email')
    name =  request.args.get('name')
    return jsonify({"payload": {"email":email,"name":name,}})
    
@app.route("/api/v1/user/add", methods=['POST'])
def hack7():
    email = request.form.get('email')
    name = request.form.get('name')
    id = request.form.get('id')
    return jsonify({"payload": {"email":email,"name":name,"id":id,}})


@app.route("/api/v1/user/create", methods=['POST'])
def hack8():
    data = request.get_json()
    email = data.get('email')
    name = data.get('name')
    id = data.get('id')
    return jsonify({"payload": {"email":email,"name":name,"id":id,}})








if __name__ == "__main__":
    app.run(debug=True)
    
    
    