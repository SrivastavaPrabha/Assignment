from flask import Flask,request

app = Flask(__name__)

@app.route("/",methods=['GET'])
def volume():
    args=request.args
    pie = 3.14
    radius = args.get("radius", default="", type=float)
    height = args.get("height", default="", type=float)
    volume = (pie * (radius**2) * height)/3
    return {"The volume of cone is ": volume}

if __name__ == "__main__":
   app.run()