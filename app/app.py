import uuid
from qna import answer_question


def start_qna(session_id):
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
    start_qna(SESSION_ID)
