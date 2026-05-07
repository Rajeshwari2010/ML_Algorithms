from flask import Flask,jsonify, request

app=Flask(__name__)

#initial data 
items = [{ "id":1, "name": "Rajeshwari","age": 21,"course": "Data Science"},
         {"id": 2 ,"name": "Rutu","age": 22,"course": "Web dev"}
         ]

@app.route("/")
def welcome():
    return "Welcome to the Sample data"


## Get: Retrieve all data
@app.route("/items", methods=['GET'])
def get_items():
    return jsonify(items)



# GET: retrive specific item by id
@app.route("/items/<int:item_id>",methods=['GET'])
def get_item(item_id):
    item=next((item for item in items if item['id']==item_id),None)
    if item is None:
        return jsonify({"error":"Item Not found"})
    return jsonify(item)

##Post Create a new task

@app.route("/items",methods=['POST'])
def create_item():
    if not request.json or not 'name' in request.json:
         return jsonify({"error":"Item Not found"})
    new_item={
        "id":items[-1]["id"]+1 if items else 1,
        "name":request.json['name'],
        "age":request.json['age'],
        "course":request.json['course']
    }
    items.append(new_item)
    return jsonify(new_item)

#put :update an existing data
@app.route("/items/<int:item_id>",methods=['PUT'])
def update_item(item_id):
      item=next((item for item in items if item['id']==item_id),None)
      if item is None:
           return jsonify({"error":"Item Not found"})
      item['name']=request.json.get('name',item['name'])
      item['age']=request.json.get('name',item['age'])
      item['course']=request.json.get('name',item['course'])
      return jsonify(item)

#Delete: delete data
@app.route("/items/<int:item_id>",methods=['DELETE'])
def delete_item(item_id):
      global items
      items=[item for item in items if item['id'] != item_id]
      return jsonify({"message": "Item deleted successfully"})

    

if __name__ == "__main__":
    app.run(debug=True)
