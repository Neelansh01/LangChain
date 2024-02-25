# LangChain
# LangChain Demo Application

A web application called LangChain Demo, which uses Streamlit, offers an interactive Q&A session regarding a fictional creature known as "huninchen". It uses OpenAI and Azure services to deliver a seamless, intelligent, and responsive experience.



## Prerequisites

For this project, ensure you have set up:

Azure Container Registry: To manage the Docker images.
App Services: Where the application will be hosted.
Blob Storage: For storing unstructured data.
Azure Cognitive Search: Powers the application's Q&A functionality.
OpenAI API Key: For generating natural language model responses.


## Configuration
.env.example

#### (#enter your values)
OPENAI_API_KEY=YOUR_OPENAI_API_KEY
AZURE_COGNITIVE_SEARCH_SERVICE_NAME=YOUR_AZURE_COGNITIVE_SEARCH_SERVICE_NAME
AZURE_COGNITIVE_SEARCH_INDEX_NAME=YOUR_AZURE_COGNITIVE_SEARCH_INDEX_NAME
AZURE_COGNITIVE_SEARCH_API_KEY=YOUR_AZURE_COGNITIVE_SEARCH_API_KEY
AZURE_CONN_STRING=YOUR_AZURE_CONN_STRING
CONTAINER_NAME=YOUR_CONTAINER_NAME


### blob.py
The creation of vector embeddings from documents and their loading into Azure Cognitive Search are handled by this script. It generates embeddings via the OpenAI API. After creation, the embeddings are saved in the Azure Search index, where they are easily accessible for quick and effective searches.

### azurecognitive_search.py
The creation of vector embeddings from documents and their loading into Azure Cognitive Search are handled by this script. It generates embeddings via the OpenAI API. After creation, the embeddings are saved in the Azure Search index, where they are easily accessible for quick and effective searches.

### application.py
The primary use case for Streamlit is this. Users can enter inquiries through a conversational interface that is set up. After that, an appropriate response is generated or retrieved using Azure Cognitive Search and OpenAI's model to process the input. During the session, previous exchanges can be examined.



To get started with the LangChain Demo Application, first, ensure that the necessary Azure services are set up and that the .env file is correctly populated with the required keys and identifiers. Follow the deployment steps for Azure to host and run your application.

# Final Web App:

<img width="674" alt="image" src="https://github.com/Neelansh01/LangChain/assets/39853942/401a234a-d5fc-40d3-b117-725fc0fb70fb">

We see the chat not only answers answers correctly but also understands intentions and human typos to provide correct answers.



# AWS Resources Rquired (for reference)

<img width="763" alt="image" src="https://github.com/Neelansh01/LangChain/assets/39853942/3ef874e7-8076-4508-844e-2e5657a41f47">

