from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://wooin:wooin@wooin0.q9s6dg9.mongodb.net/?retryWrites=true&w=majority')
db = client.luckySeven




@app.route('/')
def home():
    return render_template('index.html')






# 불이모지 카운트 API

@app.route("/fire", methods=["POST"])
def fireCount_post():
    fireCount_receive = request.form['fireCount_give']
    print(fireCount_receive)
    db.fireCount.update_one({'value':'count'},{'$set':{'countNum':fireCount_receive}})
    # DB안에 넣을때 딕셔너리 형태로 줄 것
    return jsonify({'msg':'count 업데이트 완료'})

@app.route("/fire", methods=["GET"])
def mars_get():
    currentCount = db.fireCount.find_one({'value':'count'})

    return jsonify({'msg':'fireCount 로드 완료', 'countNum' :currentCount['countNum']})


# 방명록
@app.route("/reply", methods=["POST"])
def reply_post():
    visit_receive = request.form['visit_give']
    vcom_receive = request.form['vcom_give']

    doc = {
        'visit':visit_receive,
        'vcom':vcom_receive
        }
    db.reply.insert_one(doc)

    return jsonify({'msg':'방명록 저장완료!'})

@app.route("/reply", methods=["GET"])
def reply_get():
    all_reply = list(db.reply.find({},{'_id':False}))
    return jsonify({'result':all_reply})






if __name__ == '__main__':
    app.run()









    