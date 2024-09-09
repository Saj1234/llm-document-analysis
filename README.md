# LLM Document Analysis
**Integrating LangChain with ChatGPT and Search Engines (Google, Tavily, etc.)**

This project leverages LangChain agents to extend the capabilities of language models by integrating various LangChain tools, overcoming their knowledge limitations. 

- **Up-to-Date Information:** These tools enable access to real-time information from external services such as Google Search, Tavily, custom APIs, and more, ensuring that the language model can retrieve and incorporate the most current data.
- **Enhanced Accuracy and Relevance:** By using LangChain agents, the language model's output with accurate and relevant information, making it more reliable for real-world applications.

## QnA Application with LangChain Agents and Tools
![QnA Application - LangChain - Agents and Tools](assets/diagram-main.png "QnA Application")

Explore the [LangChain Default Tools](https://python.langchain.com/v0.1/docs/integrations/tools/) for more information.


### Environment Variables
We are using OpenAI, Google and Tavily as our agent tools perform the document comparison and fetch information using the power of LLMs. Each service needs their API keys to use their services. There are limitations and quotas for each platform. You can find more information on this on their websites. 

This app loads the API keys from each service from the environment variables. When running locally, you can create a .env file and add API keys and other relevant information you want load and read within the app as environment variables. 

Ensure you have obtained the necessary API keys for each tool provider:

- **OPENAI_API_KEY**: Obtain from [OpenAI API Keys](https://platform.openai.com/api-keys).
- **GOOGLE_API_KEY** and **GOOGLE_CSE_ID**: Follow the instructions [here](https://python.langchain.com/v0.1/docs/integrations/tools/google_search/).
- **TAVILY_API_KEY**: Available at [Tavily](https://app.tavily.com/home).
- **OPENAI_MODEL**: Select a model from the [OpenAI Model List](https://platform.openai.com/docs/models).
- **DEFAULT_DOCUMENT_URL**: The URL of the document you want to check against.
- **UPDATED_DOCUMENT_URL**: The URL of the document to compare against the default.
- **DATABASE_CONNECTION_URL**: The URL for MongoDB database connection.



## Running the application locally
The app can be run locally as a chat application or an API app. 
Application maintains chat history by saving session specific chat history in MongoDB database. When running locally you can consider following options to setup the MongoDB database first. 

### Chat history with MongoDB database
Each session generates a unique session ID, and the chat history is saved under this ID, allowing you to review past interactions.

For maintaining chat history, app uses MonogDB database. For testing locally, there are couple of options you can consider if you dont have a MongoDB setup in your local machine. The app is using MongoDB Community Server. Alternatively you can choose to use [MobgoDB Atlas](https://www.mongodb.com/atlas/database).

1. Download MongoDB Community Server
 You can download the community version of [MongoDB here](https://www.mongodb.com/try/download/community) and setup locally. 

2. Running MongoDB as a Docker Container.
Running MongDB in a container would be the easier option. 
Detailed instructions on running MongoDB in a docker container can be found [here](https://www.mongodb.com/resources/products/compatibilities/docker)
 

Alternatively you can pull the MondoDB Docker image and run it locally. Detailed instructions [here](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-community-with-docker/)
```bash
docker run --name mongodb -p 27017:27017 -d mongodb/mongodb-community-server:latest
```
Once the container stars the MongoDB connection will be on `mongodb://localhost:27017/`


1. Running the app as a Chat Application
You can run this app locally as a chat application using the `app.py` file. The app has been tested with Python 3.12.1. Make sure the MongoDB database is setup properly and with either the docker container option or the local installation options. Runnng on the docker container would be the easier option for testing locally. 
   
- Create a `.env` file inside the `app` folder with the following content and set the values such API Keys other relevant information:

```plaintext
OPENAI_API_KEY=your_openai_api_key
GOOGLE_API_KEY=your_google_api_key
GOOGLE_CSE_ID=your_google_cse_id
TAVILY_API_KEY=your_tavily_api_key
OPENAI_MODEL="gpt-4o-mini"
DEFAULT_DOCUMENT_URL="default_document_url"
UPDATED_DOCUMENT_URL="updated_document_url_to_compare"
DATABASE_CONNECTION_URL="mongodb://localhost:27017/"
```



- Start the application:
   ```bash
   python app.py
   ```
- Once the app starts, you will be prompted to enter a question.

### Example usage
The app can operate as a QnA chat tool with document comparison capabilities:

```plaintext
Question: What are the main differences in the updated document compared to the main document?
```

You can also ask follow-up questions based on previous responses:

```plaintext
Question: Explain {one of the listed updates from the previous response} in detail.
```

2. Running as an API app

App can be used as an API using the `api.py` file as the starting point. Below instructions are to run the API app in a docker container and the MongoDB database base to be run in a separate container. 
When running both app and the MongoDB database in separate containers, the APP should be able to connect to the MongoDB database instance running in a separate container. 
See the all options with running MongoDB database in a container and connecting to it [here](https://www.mongodb.com/resources/products/compatibilities/docker)

Using a docker compose file will be easier to get the containers linked and run the app. Below show how you can rung each container individually and get it working. 

1. Build the main app using the Dockerfile and create an image. 
   Including Dockerfile arguments can be useful for automated builds, as they allow you to pass variables from your CI/CD pipeline directly into the Dockerfile.
   When running the Docker container locally, you can also pass these Dockerfile arguments directly from the command line using the following syntax:

   ```bash
    docker build \
          --tag repo/image:tag \
          --build-arg OPENAI_API_KEY=1234 \
          --build-arg GOOGLE_API_KEY=1234 \
          --build-arg GOOGLE_CSE_ID=1234 \
          --build-arg TAVILY_API_KEY=1234 \
          --build-arg OPENAI_MODEL=gpt-4o-mini \
          --build-arg DEFAULT_DOCUMENT_URL=default_document_web_url \
          --build-arg UPDATED_DOCUMENT_URL=updated_document_web_url \
          --build-arg DATABASE_CONNECTION_URL="mongodb://llm-mongodb:27017" 
   ```
2. Running the app and the MongoDB database in their own containers. 
   Since the there are two container running which needs to be communitcating with each other, it makes sense to run the container in the same docker network. 
   Once you have you docker network created you can specify the network name with the `--network` with `docker run` command. 

   - **See existing docker networks** 
   ```bash
    docker network ls
   ```
   This will list existing docker networks. You can chose to run your containers using an existing docker network or create a new network specific for LLM app.

   - **Create a docker network**
   ```bash
    docker network create llm-network
   ```
   Once you have the network, both the MongoDB container and the app container can be run in the same network 

   - **Running the MongoDB container**
   ```bash
     docker run --name llm-mongodb -d --network llm-network mongodb/mongodb-community-server:latest
   ``` 
   in the above command, make sure to give the container a name via --name argument. When connecting to MongoDB database, the connection URL will need be referenced by this name. In the command above it is using the container name as `llm-mongodb` hence the connection URL will have to be `mongodb://{mongodb-container-name}:27017` which in this case it will be `mongodb://llm-mongodb:27017`
   
   - **Running the app container**
   Make sure to give the same network name that given in the MongoDB docker container run command. `--network llm-network`
   The API app willbe exposed via port 5000

   ```bash
    docker run --network llm-network -it -p 5000:5000 app_image_id
   ```

### Verifying the API with the `ping` endpoint

Once the containers are up and running, you can verify the API by checking the `ping` endpoint. Open your browser and enter the following URL:

```bash
http://localhost:5000/ping
```

If the API is running successfully, you should see the response `Pong!`.


#### Asking a question using the `/ask` API endpoint

You can send questions to the `/ask` endpoint and receive responses. For follow-up questions, ensure you include the same `session_id` to maintain context.

POST API route is defined `/ask` which expects following parameters
- `session_id` 
  session_id used to save the chat history, when sent the same session_id, app will load available chat history for the session_id
- `question`
  User question 

To send a POST request, use the following endpoint and include the `session_id` and `question` in the request body as JSON.

**Endpoint:**

```bash
http://localhost:5000/ask
```

**Request Body Example (as JSON):**

```json
{
    "session_id": "1234",
    "question": "Can you compare the updated document with the default document and list the differences?"
}
```