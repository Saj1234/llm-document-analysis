import os
import os.path
from dotenv import find_dotenv, load_dotenv
import pymongo

db_name = "llm_app_db"
db_collection_name = "collection_chat_history"
document_property_name_session_id = "session_id"
document_property_name_chat_history = "chat_history"

load_dotenv(find_dotenv())
DATABASE_CONNECTION_URL = os.getenv("DATABASE_CONNECTION_URL")

mongodb_client = pymongo.MongoClient(DATABASE_CONNECTION_URL)
mongodb_database = mongodb_client[db_name]
db_collection = mongodb_database[db_collection_name]

def get_chat_history(session_id):
    """Function loading saved chat history from the database."""

    query = { document_property_name_session_id : session_id }
    session_history =  db_collection.find_one(query)
    if not session_history:
       return []
    
    return session_history[document_property_name_chat_history]

def save_chat_history(session_id, chat_history):
    """Function saving chat history in the database."""
    # update 'data' if 'name' exists otherwise insert new document
    db_collection.find_one_and_update(
                          { document_property_name_session_id : session_id },
                          { "$set":{ document_property_name_chat_history : chat_history }},
                        upsert=True)
    
def clear_chat_history(session_id):
    """Function clearing chat history for session_id from the database."""

    query = { document_property_name_session_id : session_id }
    db_collection.delete_one(query)