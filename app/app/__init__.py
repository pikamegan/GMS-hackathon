from flask import Flask

app = Flask(__name__)
db = SQLAlchemy(app)


from app import views
