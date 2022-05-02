import requests
import json

URL=" http://127.0.0.1:8000/Todo/"

def get_record(id=None):
    data={}
    if id is not None:
        data={'id':id}
    jsondata=json.dumps(data)

    headers={'content-Type':'application/json'}
    r=requests.get(url=URL,headers=headers,data=jsondata)
    data=r.json()
    print(data)

#get_record(1)
#get_record()

def post_record():
    data = {
        'name': 'sairam',
        'notes': 'hyd',

    }
    jsondata=json.dumps(data)
    headers = {'content-Type': 'application/json'}
    r=requests.post(url=URL,headers=headers,data=jsondata)
    data=r.json()
    print(data)

#post_record()

def update_record():
    data = {
        'id':1,
        'name': 'mohan',
        'address': 'srnagar',
        
    }
    jsondata=json.dumps(data)
    headers = {'content-Type': 'application/json'}
    r=requests.put(url=URL,headers=headers,data=jsondata)
    data=r.json()
    print(data)


#update_record()

def delete_data():
    data={'id':4}

    jsondata=json.dumps(data)
    headers = {'content-Type': 'application/json'}
    r=requests.delete(url=URL,headers=headers,data=jsondata)
    data=r.json()
    print(data)

delete_data()
