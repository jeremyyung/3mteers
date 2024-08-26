from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import mysql.connector
from datetime import datetime
from pydantic import BaseModel

#Fastapi data object
class Numitem(BaseModel):
    lucky_num: int
    guest_ip: str

#Create mysql connector
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
mydb = mysql.connector.connect(
    host="db",
    user="3madmin",
    password="mypass111",
    port="3306",
    database="3mdb"
)
mycursor = mydb.cursor()

@app.get("/getall")
async def getall():
    mycursor.execute("SELECT * FROM allnumbers ORDER BY date DESC")
    return parseFetch(mycursor)

@app.post("/update")
async def create_item(item: Numitem):
    insert_query = "INSERT INTO allnumbers (%s) VALUES (%s)"
    req_luckynum = item.lucky_num.__str__()
    guest_ip = item.guest_ip.__str__()

    if guest_ip:
        query_params = ("lucky_num, guest_ip", req_luckynum + ",\"" + guest_ip + "\"")
    else:
        query_params = ("lucky_num", req_luckynum)
    insert_query = insert_query % query_params
    try:
        mycursor.execute(insert_query)
        status = "ok"
        mydb.commit()
    except:
        status = "Failed to execute: %s" % insert_query

    return {"result": status }

def parseFetch(dbcursor):
    alldata = []
    fetch_results = dbcursor.fetchall()
    col_names = dbcursor.column_names
    for values in fetch_results:
        temp_json = {}
        for index in range(len(col_names)):
            if type(values[index]) == datetime:
                temp_json[col_names[index]] = values[index].strftime("%m/%d/%Y %H:%M:%S")
            else:
                temp_json[col_names[index]] = values[index]
        alldata.append(temp_json)
    return alldata