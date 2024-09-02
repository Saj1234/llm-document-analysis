# LLM Document Analysis
**Integrating LangChain with ChatGPT and Search Engines (Google, Tavily, etc.)**

This project leverages LangChain agents to extend the capabilities of language models by integrating various LangChain tools, overcoming their knowledge limitations. 

- **Up-to-Date Information:** These tools enable access to real-time information from external services such as Google Search, Tavily, custom APIs, and more, ensuring that the language model can retrieve and incorporate the most current data.
- **Enhanced Accuracy and Relevance:** By using LangChain agents, the language model's output with accurate and relevant information, making it more reliable for real-world applications.

## QnA Application with LangChain Agents and Tools
![QnA Application - LangChain - Agents and Tools](assets/diagram-main.png "QnA Application")

Explore the [LangChain Default Tools](https://python.langchain.com/v0.1/docs/integrations/tools/) for more information.

## Running the Application Locally

### Environment Variables
We are using OpenAI, Google and Tavily as our agent tools do perform the document comparison and fetch updated using the power of LLMs. Each service needs their API keys to use their services. There are limitations and quotas for each platform. You can find more information on this on their websites. 

This app loads the API keys from each service from the environment variables. When running locally, you can create a .env file and add API keys and other relevant information you want load and read within the app as environment variables. 

Ensure you have obtained the necessary API keys for each tool provider:

- **OPENAI_API_KEY**: Obtain from [OpenAI API Keys](https://platform.openai.com/api-keys).
- **GOOGLE_API_KEY** and **GOOGLE_CSE_ID**: Follow the instructions [here](https://python.langchain.com/v0.1/docs/integrations/tools/google_search/).
- **TAVILY_API_KEY**: Available at [Tavily](https://app.tavily.com/home).
- **OPENAI_MODEL**: Select a model from the [OpenAI Model List](https://platform.openai.com/docs/models).
- **DEFAULT_DOCUMENT_URL**: The URL of the document you want to check against.
- **UPDATED_DOCUMENT_URL**: The URL of the document to compare against the default.


Create a `.env` file inside the `app` folder with the following content and set the values such API Keys other relevant information:

```plaintext
OPENAI_API_KEY=your_openai_api_key
GOOGLE_API_KEY=your_google_api_key
GOOGLE_CSE_ID=your_google_cse_id
TAVILY_API_KEY=your_tavily_api_key
OPENAI_MODEL="gpt-4o-mini"
DEFAULT_DOCUMENT_URL="default_document_url"
UPDATED_DOCUMENT_URL="updated_document_url_to_compare"
```


### Running the App as a Chat Application Locally
You can run this app locally as a chat application using the `app.py` file. The app has been tested with Python 3.12.1.

1. Start the application:
   ```bash
   python app.py
   ```
2. Once the app starts, you will be prompted to enter a question.

#### Example Usage
The app can operate as a QnA chat tool with document comparison capabilities:

```plaintext
Question: What are the main differences in the updated document compared to the main document?
```

You can also ask follow-up questions based on previous responses:

```plaintext
Question: Explain {one of the listed updates from the previous response} in detail.
```

#### Chat History
Each session generates a unique session ID, and the chat history is saved under this ID, allowing you to review past interactions.

### Running the application as an API in a Docker container
Docker file is defined with arguments to match the environment variables so that we can pass these values in docker build command on in the Docker compose file as args. 
Passing this via docker compose will will be handy as these argument can be replaces with devops pipeline variables. 

#### Running the Docker file locally
Docker file can be run locally with arguments in the command line. This setup is ideal fro automated but if running locally but we can give the build command as below with passing argument in command line:

```bash
 docker build --tag repo/image:tag --build-arg OPENAI_API_KEY=1234 --build-arg GOOGLE_API_KEY=1234 --build-arg GOOGLE_CSE_ID=1234 --build-arg TAVILY_API_KEY=1234 --build-arg OPENAI_MODEL=gpt-4o-mini --build-arg DEFAULT_DOCUMENT_URL=default_document_web_url --build-arg UPDATED_DOCUMENT_URL=updated_document_web_url .
```

Run the container in intercative mode
```bash
 docker run -it -p 5000:5000  imageid
```

