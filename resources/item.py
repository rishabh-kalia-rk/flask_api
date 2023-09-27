
from flask_restful import Resource,reqparse
from flask_jwt import jwt_required

from models.item import ItemModel 


class Item(Resource):
    
    parser= reqparse.RequestParser()
    parser.add_argument('price',
                    type=float,
                    required=True,
                    help="This filed cannot be left empty")
    parser.add_argument('store_id',
                    type=float,
                    required=True,
                    help="This filed cannot be left empty")
    
    def get(self,name):
        row=ItemModel.find_by_name(name)
        if row:
            return row.json()
        # we have creatd method in ItemsModel class which get us the json format of the object we created from ItemModel class.
        else:
            return {"message":"item not found"},404  

    def post(self,name):
        
        if ItemModel.find_by_name(name):
            return {"message":"Item already present"}, 409
        
        data_re=Item.parser.parse_args()
        item=ItemModel(name,data_re['price'],data_re['store_id'])
        try:
            item.save_to_db()
            #becasue item contain the object and using that we access the insert() method from class this object is made.
        except:
            return{"message":"an error occured inserting the item"},500
        return item.json(), 201
        # json is method we created to convert object arguments to json format 

    def put(self,name):
        data_re=Item.parser.parse_args()
        
        item=ItemModel.find_by_name(name) 
        if item is None:
            item=ItemModel(name,data_re['price'],data_re['store_id'])
        else:
           item.price=data_re['price']
           item.store_id=data_re['store_id']
        item.save_to_db()
        return item.json() , 200

    def delete(Self,name):
       item=ItemModel.find_by_name(name)
       if item:
           item.delete_from_db()
           return {"message":"item deleted"},200
       else:
           return {"message":"item not found"},400
       
            
class ItemList(Resource):
    @jwt_required()
    def get(self):
        return {'items':[x.json() for x in ItemModel.find_all()]}, 200
            
