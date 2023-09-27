
from flask_restful import Resource, reqparse
from models.user import UserModel



class UserRegister(Resource):
    
    parser=reqparse.RequestParser()
    parser.add_argument('username',type=str,required=True)
    parser.add_argument('password',type=str,required=True)
    
    def post(self):
        data=UserRegister.parser.parse_args()
        if UserModel.find_by_username(data['username']):
            return {"message":"User already exist"} , 409
        user =UserModel(data['username'],data['password'])
        user.save_to_db()
        return {"message": "user created successfully"} , 201


class User (Resource):
    @classmethod
    def get(cls,user_id):
        user=UserModel.find_by_id(user_id)
        if not user:
            return {"message":"user not found"}, 404
        return user.json(), 200
    @classmethod
    def delete(cls,user_id):
        user=UserModel.find_by_id(user_id)
        if not user:
            return {"message":"user not found"},404
        user.delete_from_db()
        return {"message":"user deleted"}, 200
