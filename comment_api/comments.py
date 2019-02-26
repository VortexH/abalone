#!/usr/bin/python3
from flask import Flask, jsonify, request
import json
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
                  passwd='rkLotus956',
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
        {'video_id': [username, comment, timestamp]}

    """
    db = MySQLdb.connect(
            host = 'localhost',
            user = 'root',
            passwd = 'rkLotus956',
            db='hackday_abalone'
            )

    cur = db.cursor()


    response_dict = json.loads(request.data.decode('utf-8'))
    print(response_dict)
    value = list(response_dict.values())
    post_parameters = value[0]
    print("The payload sent in the post request is {}".format(post_parameters))
    username = post_parameters[0]
    print("The username is {}".format(username))
    query_string = 'SELECT id FROM users WHERE name="{}"'.format(username)
    print(query_string)
    
    cur.execute(query_string)
    user_id= cur.fetchall()[0]
    print(type(user_id))
    print(user_id[0])

    print(response_dict.keys())
    print(list(response_dict.keys()))
    video_id = list(response_dict.keys())[0]
    print(user_id)
    print(video_id)
    print(post_parameters[1])
    print(post_parameters[2])
    sql_string = 'INSERT INTO comments (user_id, video_id, comment, timestamp) VALUES ({}, "{}", "{}", "{}")'.format(
                    user_id,
                    video_id,
                    post_parameters[1],
                    post_parameters[2]
                    )

    #cur.execute("INSERT INTO comments (user_id, video_id, comment, timestamp) VALUES (1, 'alsdjfasdf', 'hey whatups askjfd', 'april152019')")


    cur.execute(sql_string)

    db.close()

    return jsonify('success')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='6000')
