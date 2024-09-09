from flask import Flask, request, abort
from chat_history import clear_chat_history, get_chat_history
from qna import answer_question

# create a Flask instance
app = Flask(__name__)

@app.route('/ping', methods=['GET', 'POST'])
def ping(): 
    """Function Ping - This function will be used to check API connectivity"""
    return 'Pong!'

@app.route('/ask', methods=['POST'])
def ask():
    """Function ask - Ask questions from LLM and session id will be used to load the chat from history if available."""
    if(request.method == 'POST'): 
        request_data = request.get_json(force=True)
        # check if JSON properties exist in the request body first
        if "session_id" in  request_data and "question" in  request_data:
            session_id = request_data["session_id"]
            question = request_data["question"]
            answer = answer_question(session_id, question)
            return answer

        return abort(500, "'session_id' or 'question' parameter missing.")

    return abort(500, "Invalid request.") 

@app.route('/gethistory', methods=['GET'])
def get_history():
    """Function gethistory - For debugging purposes, Gets the chat history for a given session_id."""
    if(request.method == 'GET'): 
        session_id = request.args.get('session_id')
        history = get_chat_history(session_id)
        return history
    
@app.route('/clearhistory', methods=['DELETE'])
def clear_history():
    """Function clearhistory - Clears the chat history saved in the database for a giver session_id."""
    if(request.method == 'DELETE'): 
        session_id = request.args.get('session_id')
        clear_chat_history(session_id)
        return "History cleared successfully."   

if __name__ == "__main__":
	# for debugging locally
	app.run(debug=True, host='0.0.0.0',port=5000, threaded=True)