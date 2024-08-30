# LLM Document Analysis
**Integrating LangChain with ChatGPT and Search Engines (Google, Tavily, etc.)**

This project leverages LangChain agents to extend the capabilities of language models by integrating various LangChain tools, overcoming their inherent knowledge limitations. 

- **Up-to-Date Information:** These tools enable access to real-time information from external services such as Google Search, Tavily, custom APIs, and more, ensuring that the language model can retrieve and incorporate the most current data.
- **Enhanced Accuracy and Relevance:** By using LangChain agents, the language model's output is enriched with accurate and relevant information, making it more reliable for real-world applications.

## QnA Application with LangChain Agents and Tools
![QnA Application - LangChain - Agents and Tools](assets/diagram-main.png "QnA Application")

Explore the [LangChain Default Tools](https://python.langchain.com/v0.1/docs/integrations/tools/) for more information.

## Running the Application Locally

### Environment Variables
Create a `.env` file inside the `app` folder with the following content:

```plaintext
OPENAI_API_KEY=your_openai_api_key
GOOGLE_API_KEY=your_google_api_key
GOOGLE_CSE_ID=your_google_cse_id
TAVILY_API_KEY=your_tavily_api_key
OPENAI_MODEL="gpt-4o-mini"
DEFAULT_DOCUMENT_URL="default_document_url"
UPDATED_DOCUMENT_URL="updated_document_url_to_compare"
```

Ensure you have obtained the necessary API keys for each tool provider:

- **OPENAI_API_KEY**: Obtain from [OpenAI API Keys](https://platform.openai.com/api-keys).
- **GOOGLE_API_KEY** and **GOOGLE_CSE_ID**: Follow the instructions [here](https://python.langchain.com/v0.1/docs/integrations/tools/google_search/).
- **TAVILY_API_KEY**: Available at [Tavily](https://app.tavily.com/home).
- **OPENAI_MODEL**: Select a model from the [OpenAI Model List](https://platform.openai.com/docs/models).
- **DEFAULT_DOCUMENT_URL**: The URL of the document you want to analyze.
- **UPDATED_DOCUMENT_URL**: The URL of the document to compare against the default.

### Running the App as a Chat Application Locally
You can run this app locally as a chat application using the `app.py` file. The app has been tested with Python 3.12.1.

1. Start the application:
   ```bash
   python app.py
   ```
2. Once the app starts, you will be prompted to enter a question.

### Example Usage
The app can operate as a QnA chat tool with document comparison capabilities:

```plaintext
Question: What are the main differences in updated document compared to main document?
```

You can also ask follow-up questions based on previous responses:

```plaintext
Question: Explain {one of the listed updates from the previous response} in detail.
```

### Chat History
Each session generates a unique session ID, and the chat history is saved under this ID, allowing you to review past interactions.

