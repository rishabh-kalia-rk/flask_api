
import os
from flask import Flask
from flask_restful import Api
from flask_swagger_ui import get_swaggerui_blueprint
from flask_jwt import JWT
from sqlalchemy import create_engine
from flask_cors import CORS
from dotenv import load_dotenv
import os


load_dotenv()

SECRETE_KEY =os.environ.get("SECRETE_KEY")

from security import authenticate,identity
from resources.item import Item,ItemList
from resources.store import Store,StoreList



from resources.user import UserRegister, User


app=Flask(__name__)
engine = create_engine('sqlite:///data.db')
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
CORS(app)



SWAGGER_URL='/swagger'
API_URL='/static/openapi.json'
SWAGGER_BLUEPRINT=get_swaggerui_blueprint(
	SWAGGER_URL,
	API_URL,
	config={
		'app_name':"list api"
	}

)
app.register_blueprint(SWAGGER_BLUEPRINT,url_prefix=SWAGGER_URL)
api=Api(app)

@app.before_request
def create_tables():
	db.create_all()

app.secret_key=SECRETE_KEY
jwt=JWT(app,authenticate,identity)

@app.route('/')
def home():
	return "<h1>Welcome to FLask Restful API</h1><p>Created By: Rishabh"
	






api.add_resource(Store,'/store/<string:name>')
api.add_resource(ItemList,'/items')
api.add_resource(Item,'/item/<string:name>')
api.add_resource(StoreList,'/stores')
api.add_resource(UserRegister,'/register')
api.add_resource(User,'/user/<int:user_id>')

if __name__=="__main__":
	from db import db
	db.init_app(app)
	app.run(port=5000)