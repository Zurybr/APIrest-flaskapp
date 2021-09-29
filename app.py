from flask import Flask,render_template,make_response,jsonify,request
from data import comments
app = Flask(__name__)
PORT = 4000
HOST = '0.0.0.0'

@app.route("/")
def index():
    return render_template("./temp.html")

@app.errorhandler(404)
def page_not_found():
    res=make_response(jsonify({"error":"page not found"}),400)
    return res

@app.route ("/comments")
def query_string():
    
    if 'postId' in request.args:
        if request.args.get('postId') == "":
            res=make_response(jsonify({"error":"true"}),400)
            return res
        postId = int(request.args.get('postId'))
        res = {}
        iterador = 0
        for i in comments:
            for key,Value in i.items():
                if Value == postId:
                    res[iterador] = i
                    iterador =+ 1
                else:
                    continue
        res= make_response(jsonify(res),200)
        return res

    if 'id' in request.args:
        if request.args.get('id') == "":
            res=make_response(jsonify({"error":"true"}),400)
            return res
        id = int(request.args.get('id'))
        res = {}
        iterador = 0
        for i in comments:
            for key,Value in i.items():
                if Value == id:
                    res[iterador] = i
                    iterador =+ 1
                else:
                    continue
        res= make_response(jsonify(res),200)
        return res
        
    if 'email' in request.args:
        if request.args.get('email') == "":
            res=make_response(jsonify({"error":"true"}),400)
            return res
        email = request.args.get('email')
        res = {}
        iterador = 0
        for i in comments:
            for key,Value in i.items():
                if Value == email:
                    res[iterador] = i
                    iterador =+ 1
                else:
                    continue
        res= make_response(jsonify(res),200)
        return res

    res = {}
    iterador = 0
    for i in comments:
        res= comments
        iterador =+ 1
    res= make_response(jsonify(res),200)
    return res
@app.route ("/comments",methods=['POST'])
def post_query_string():
    res = {}
    iterador = 0
    for i in comments:
        res= comments
        iterador =+ 1
    res= make_response(jsonify(res),200)
    return res

if __name__  == "__main__":
    print("Server running in port {}".format(HOST))
    app.run(host=HOST,port=PORT,debug=True)