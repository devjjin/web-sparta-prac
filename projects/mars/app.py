from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://sparata:test@cluster0.jqqeot4.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/mars", methods=["POST"])
def mars_post():
    name_receive = request.form['name_give']
    size_receive = request.form['size_give']
    address_receive = request.form['address_give']
    print(name_receive,size_receive,address_receive)
    
    doc = {
        'name': name_receive,
        'address': address_receive,
        'size': size_receive
    }
    db.mars.insert_one(doc)
    return jsonify({'msg':'주문완료!'})

@app.route("/mars", methods=["GET"])
def mars_get():
    # db에서 가져오기
    all_mars = list(db.mars.find({},{'_id':False}))
    return jsonify({'result':all_mars})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)