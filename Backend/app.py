
from multiprocessing.sharedctypes import Value
from flask import Flask, render_template, request
import MySQLdb
db = MySQLdb.connect("localhost", "root", "", "project")
import json
import os
import base64
from flask_cors import CORS,cross_origin
app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
CORS(app, support_credentials=True)

#generating sql commands
def create_sql_comand(keys,value):
    str1="select leaf_division from leaf where "
    for index in range(0,len(keys)-1):
        str1=str1+f"{keys[index]}='{value[index]}' and "
    str1=str1+f"{keys[len(keys)-1]}='{value[len(keys)-1]}'"
    return str1

#getting images path from contained folder
def getFileNames(folderNames):
    IMAGES_PATH = './static/dataset/'
    answer = {}
    fileName = []
    for folder in folderNames:
        allfiles = os.listdir(IMAGES_PATH+folder)
        for file in allfiles:
            fileName.append((IMAGES_PATH.split(".")[1]).split(
                "/")[2] + "/" + folder + "/" + file)
        answer[folder] = fileName
        fileName = []
    return answer

def insert_sql_comand(keys,value):
    str1="insert into temp("
    str1=str1+"leaf_division , "
    for index in range(0,len(keys)-1):
        str1=str1+f"{keys[index]} , "
    str1=str1+f"{keys[len(keys)-1]}"
    str1=str1+")values("    
    str1=str1+f"'{output}' , "
    for index in range(0,len(keys)-1):
        str1=str1+f"'{value[index]}' , "
    str1=str1+f"'{value[len(keys)-1]}'"
    str1=str1+");"    
    # str1=str1+f"{keys[len(keys)-1]}='{value[len(keys)-1]}'"
    return str1
#recive client server call

@app.route("/predict", methods=["GET", "POST"])
@cross_origin(supports_credentials=True)
def calc():
    data = request.get_json()
    print(data);
    print(type(data));
    keys=[]
    value=[]
    
    for arr in data:
         keys.append(arr)
        #  print(key,key[0])
         value.append(data[arr])
    

    command = create_sql_comand(keys,value)
    curs = db.cursor()  #create a curser to database for  data extraction

    print(command)
    try:
        curs.execute(command)
        folder=curs.fetchall() #insert extracted data to folder variable
        intersection_folder=[]
        for foll in folder:
            print(foll[0])
            intersection_folder.append(foll[0])
        filenames=getFileNames(intersection_folder)
        print(filenames)
        return json.dumps(filenames) #dump data from server to client
    except:
        print( "Error: unable to fetch items")
        return json.dumps({})   #dump data from server to client

@app.route("/adddata", methods=["GET", "POST"])
@cross_origin(supports_credentials=True)
def send():
 
   data = request.get_json()
   print(data)
   print(type(data))
   keys1=[]
   value1=[]
    
   for arr in data:
        keys1.append(arr)
        #  print(key,key[0])
        value1.append(data[arr])
    
   command = insert_sql_comand(keys1,value1)
   curs = db.cursor()  #create a curser to database for  data extraction
   
   print(command)
   try:
       curs.execute(command)
       db.commit()
    #    print("how are you")
       return json.dumps("plz upload image now your response is added to database")
   except:     
           print( "Error: unable to fetch items")
           return json.dumps({})   #dump data from server to client
@app.route("/imagedata", methods=["GET", "POST"])
@cross_origin(supports_credentials=True)
def image():
 
   data = request.get_data()
   base64EncodedStr = base64.b64encode(data)
#    print(base64EncodedStr)
   with open("imageToSave.png", "wb") as fh:
        fh.write(base64.decodebytes(base64EncodedStr))
#    print(type(data))
#    print(type(base64EncodedStr))
   try:
        print("how are you")
        return json.dumps("image upload successfully")
   except:     
           print( "Error: unable to fetch items")
           return json.dumps({})   #dump data from server to client
@app.route("/imagename", methods=["GET", "POST"])
@cross_origin(supports_credentials=True)
def imagename():
   data = request.get_data()
   global output 
   output = data.decode()
   
   print(output)
   try:
       # print("how are you")
        return json.dumps()
   except:     
           print()
           return json.dumps({})   #dump data from server to client
app.run(debug=True)