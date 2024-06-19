from app import app
import app.settings as settings
from controllers.route import registryRouter
from model.recommend import Recommend
from model.chatbot import ChatBot

model = Recommend()
chatbot = ChatBot()

if __name__ == "__main__":
    registryRouter(app, model, chatbot)
    app.run(host=settings.BE_HOST, port=settings.BE_PORT, debug=settings.ENV != "PROD")
