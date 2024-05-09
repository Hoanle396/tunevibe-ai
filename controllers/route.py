import os
from flask import request
from flask_cors import cross_origin
from flask_reuploads import AUDIO, UploadSet, configure_uploads
import assemblyai as aai
from app import settings

aai.settings.api_key = settings.API_KEY


def registryRouter(app, model):
    wavaudio = UploadSet('files', AUDIO)

    app.config['UPLOADED_FILES_DEST'] = './audio'
    configure_uploads(app, wavaudio)

    @app.route("/api/predict", methods=["POST"])
    def Audio2Text():
        try:
            transcriber = aai.Transcriber()
            filename = wavaudio.save(request.files['audio'])
            audio = './audio/{}'.format(filename)
            transcript = transcriber.transcribe(audio)
            return {"status":"success","data":transcript.text},200
        except:
            return {"status":"success","data":"Could not detect lyrics"},400
        finally:
            os.remove(audio)
        