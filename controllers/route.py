import datetime
import os
from flask import request
from flask_reuploads import AUDIO, UploadSet, configure_uploads
import assemblyai as aai
from app import settings

aai.settings.api_key = settings.API_KEY


def registryRouter(app, model, chatbot):
    wavaudio = UploadSet("files", AUDIO)

    app.config["UPLOADED_FILES_DEST"] = "./audio"
    configure_uploads(app, wavaudio)

    @app.route("/api/predict", methods=["POST"])
    def Audio2Text():
        try:
            transcriber = aai.Transcriber()
            filename = wavaudio.save(request.files["audio"])
            audio = "./audio/{}".format(filename)
            transcript = transcriber.transcribe(audio)
            return {"status": "success", "data": transcript.text}, 200
        except:
            return {"status": "success", "data": "Could not detect lyrics"}, 400
        finally:
            os.remove(audio)

    @app.route("/api/recommend", methods=["POST"])
    def recommend():
        try:
            userId = request.json["userId"]
            transcript = model.predict()
            transcript = transcript[(transcript["userId"] == int(userId))]
            result = transcript[(transcript["prediction"] > 3.5)].to_dict(
                orient="records"
            )
            return {
                "status": "success",
                "data": result,
                "no": transcript.to_dict(orient="records"),
            }, 200
        except Exception as e:
            print(e)
            return {"status": "success", "data": "Could not detect lyrics"}, 400

    @app.route("/api/chat", methods=["POST"])
    def chat():
        msg = request.json["msg"]
        chat = str(chatbot.chat(msg))
        return {"user": "BOT", "text": chat, "createdAt": datetime.datetime.now()}, 200
