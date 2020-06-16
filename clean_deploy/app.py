# deploy_front/app.py
#

import os.path
from flask import Flask
import os
import json
import run_backend

import time

app = Flask(__name__)

def get_predictions():

    videos = []
    
    novos_videos_json = "novos_videos.json"
    if not os.path.exists(novos_videos_json):
        run_backend.update_db()
    
    last_update = os.path.getmtime(novos_videos_json) * 1e9

    #if time.time_ns() - last_update > (720*3600*1e9): # aprox. 1 mes
    #    run_backend.update_db()

    with open("novos_videos.json", 'r') as data_file:
        for line in data_file:
            line_json = json.loads(line)
            videos.append(line_json)

    predictions = []
    for video in videos:
        #print(video)
        #print(video['video_id'])
        predictions.append((video['video_id'], video['title'], float(video['score'])))

    predictions = sorted(predictions, key=lambda x: x[2], reverse=True)[:30]


    predictions_formatted = []
    for e in predictions:
        #print(e)
        predictions_formatted.append(
            """
            <tr>
                <th>
                    <a href=\"{link}\">{title}</a>
                </th>
                <th> = {score}</th>
            </tr>
            """.format(title=e[1], link=e[0], score=e[2]))
  
    return '\n'.join(predictions_formatted), last_update

@app.route('/')
def main_page():
    preds, last_update = get_predictions()
    return """
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
        <title>Movie Recommendation</title>
    </head>
    <body>
    <h1>Movie Recommendation From YouTube With Machine learning</h1>
    <h6>Last Updated in Seconds: {}</h6>
    <table>
        <tr>
            <th>Video Descrition</th>
            <th>Average Precision Score</th>
        </tr>
             {}
    </table>
    </body>""".format((time.time_ns() - last_update) / 1e9, preds)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')