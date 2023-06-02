from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://wooin:wooin@wooin0.q9s6dg9.mongodb.net/?retryWrites=true&w=majority')
db = client.luckySeven




@app.route('/')
def home():
    return render_template('index.html')



#### 팀원 API
# @app.route("/team", methods=["POST"])
# def team_post():
#     image_receive = request.form['image_give']
#     name_receive = request.form['name_give']
#     mbti_receive = request.form['mbti_give']
#     comment_receive = request.form['comment_give']
#     sty_receive = request.form['sty_give']
#     good_receive = request.form['good_give']
#     url_receive = request.form['url_give']
    
#     doc = {
#         'image':image_receive,
#         'name':name_receive,
#         'mbti':mbti_receive,
#         'comment':comment_receive,
#         'sty':sty_receive,
#         'good':good_receive,
#         'url':url_receive
#         }
#     db.teams.insert_one(doc)

#     return jsonify({'msg':'팀원 기록완료!'})

# @app.route("/team", methods=["GET"])
# def team_get():
#     all_teams = list(db.teams.find({},{'_id':False}))
#     return jsonify({'result':all_teams})














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


# 댓글창
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

# @app.route("/reply", methods=["DEL"])
# def reply_del():

#     db.users.delete_one({'name':'bobby'})



if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)









    