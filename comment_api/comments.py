#!/usr/bin/python3
from flask import Flask, jsonify, request
import MySQLdb

app = Flask(__name__)


@app.route('/get_comments/<video_id>')
def get_comments(video_id):
    """ Returns a dictionary with the key being the video_id
        and the value being a list of lists containing a username,
        comment string, and the timestamp
    """
    print(video_id)

    db = MySQLdb.connect(
                  host='localhost',
                  user='root',
                  passwd='',
                  db='hackday_abalone')

    cur = db.cursor()
    query_string = 'SELECT * FROM comments WHERE video_id="{}"'.format(video_id)
    cur.execute(query_string)  
    response = {}
    global_list = []
    for row in cur.fetchall():
        comment_list = []
        comment_list.append(row[1])
        comment_list.append(row[3])
        comment_list.append(row[4])
        global_list.append(comment_list)

    response[video_id] = global_list

    db.close()

    return jsonify(response)

@app.route('/submit_comment', methods=['POST'])
def submit_comment():
    """ Takes in a JSON of this type
        {'video_id': [ [username, comment, timestamp], ... ]}

    """
    return(request)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='6000')
