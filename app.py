from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
# from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import requests
import time
# import 
''' IMPORT FUNCTIONS '''
from models import HashtagInsights

slack = "https://slack.com/api/chat.postMessage?token=xoxp-191928386964-191976206613-362151076802-76c01eca4e9dd2062cbb0b0eaa67d409&channel=%23scraping&text="

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
# db = SQLAlchemy(app)

# class Todo(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     action = db.Column(db.String(200), nullable=False)
#     username = db.Column(db.String(200), nullable=False)
#     date_created = db.Column(db.DateTime, default=datetime.utcnow)

#     def __repr__(self):
#         return '<Task %r>' % self.id

@app.route('/get_hashtag_reach', methods = ['GET'])
@cross_origin()
def index():
    data = request.headers
    auth_token = 'Token rwer7REQi9KJz6w87KDXvhjr'
    if data['Authorization'] == auth_token:
        hashtag = request.args.get('hashtag')
        past_post_count = request.args.get('post_limit')
        if past_post_count:
            hashtag_details = HashtagInsights.get_reach_by_hashtag(hashtag, int(past_post_count))
        else:
            hashtag_details = HashtagInsights.get_reach_by_hashtag(hashtag)
        requests.post(slack + "HASHTAG REACH: Hashtag {} | Post_limit {}".format(hashtag,past_post_count))
        response = jsonify(hashtag_details)
    else:
        response = jsonify({"status": False, "Extra": "Unauthorized Request"})
    return response
    
if __name__ == "__main__":
    app.run(debug = True)