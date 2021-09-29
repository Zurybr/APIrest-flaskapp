from flask import Flask,render_template,make_response,jsonify,request
from data import comments
app = Flask(__name__)
PORT = 4000
HOST = '0.0.0.0'

@app.route("/")
def index():
    return "ok"

@app.route("/temp")
def template():
    return render_template("./temp.html")
    

@app.route ("/comments")
def query_string():
    
    if request.args:
        postId = int(request.args.get('postId'))
        print(type(postId))
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
    res = {}
    iterador = 0
    for i in comments:
        res= comments
        iterador =+ 1
    res= make_response(jsonify(res),200)
    return res
    # res=make_response(jsonify({"error":"true"}),400)
    # return res










if __name__  == "__main__":
    print("Server running in port {}".format(HOST))
    app.run(host=HOST,port=PORT,debug=True)