import uuid
from agents import load_agent_executor
from chat_history import load_chat_history, save_chat_history


agent_executor = load_agent_executor()


def answer_question(session_id, user_input):
    """Function process QNA session. This function will load chat history for passed session id if available."""

    chat_history = load_chat_history(session_id)
    # Invoke the agent and pass the current chat history
    response = agent_executor.invoke(
        {"input": user_input, "chat_history": chat_history}
    )
    response_output = response["output"]
    chat_history.append(response_output)
    save_chat_history(session_id, chat_history)

    return response_output


def q_and_a(session_id):
    """Function Qna Chat session"""
    while True:
        # Prompt user for input
        question = input("Question: ")

        # Break the loop if 'q' is pressed
        if question.lower() == "quit" or question.lower() == "exit":
            print("Exiting session")
            break

        answer = answer_question(session_id, question)
        print("Answer: ", answer)


if __name__ == "__main__":

    SESSION_ID = str(uuid.uuid1())
    print(SESSION_ID)
    q_and_a(SESSION_ID)
