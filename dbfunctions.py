from settings import *
import pymongo
from pymongo import MongoClient


def dbconnect() :
	client = MongoClient("mongodb://data:data@localhost:27017/data")
	db = client[databasename]
	return db

def save_collection(collection,arr):
	db = dbconnect()
	coll = db[collection]
	data = coll.insert(arr)
	return data

def update_collection(collection,arr,ary):
      
	db = dbconnect()
        coll = db[collection]
        data = coll.update(arr,ary,upsert = True )
        return data
        
def del_doc(collection,arr):
        db = dbconnect()
        coll = db[collection]
        data = coll.remove(arr)
        return data
        

def find_and_filter(collection,arr):
	db = dbconnect()
	coll = db[collection]
	cursor = coll.find(arr)
	result = [item for item in cursor]
	return result

def find_all_in_collection(collection):
	db = dbconnect()
	coll = db[collection]
	cursor = coll.find()
	result = [item for item in cursor]
	return result

