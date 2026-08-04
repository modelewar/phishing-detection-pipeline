import os
import sys
import json
from dotenv import load_dotenv
import certifi
import pandas as pd
import numpy as np
import pymongo
from src.exception import NetworkSecurityException
from src.logging.logger import logging

load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL", "mongodb://localhost:27017")

print(MONGO_DB_URL)

ca = certifi.where()


class DataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def csv_to_json(self, file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)

            records = list(json.loads(data.T.to_json()).values())

            return records
        
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def insert_data_db(self, records, db, collection):
        try:
            self.db = db
            self.collection = collection
            self.records = records

            self.mongoclient = pymongo.MongoClient(MONGO_DB_URL)

            self.db = self.mongoclient[self.db]
            self.collection = self.db[self.collection]

            # Clear collection before inserting to prevent duplicates
            self.collection.delete_many({})
            self.collection.insert_many(self.records)
            
            return len(self.records)
        
        except Exception as e:
            raise NetworkSecurityException(e, sys)


if __name__ == '__main__':
    CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
    FILE_PATH = os.path.join(CURRENT_DIR, "Network_Data", "phisingData.csv")

    DATABASE = "MODELEWAR" 
    Collection = "NetworkData"

    networkobj = DataExtract()
    rec = networkobj.csv_to_json(file_path=FILE_PATH)
    print(f"Extracted {len(rec)} records from CSV.")

    no_of_rec = networkobj.insert_data_db(records=rec, db=DATABASE, collection=Collection)
    print(f"Inserted {no_of_rec} records into MongoDB.")