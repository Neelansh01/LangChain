import os
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores.azuresearch import AzureSearch
from langchain.document_loaders import AzureBlobStorageContainerLoader
from langchain.text_splitter import CharacterTextSplitter
#from dotenv import load_dotenv

#load_dotenv()
os.environ["OPENAI_API_KEY"] = "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"
model: str = "text-embedding-ada-002"

vector_store_address: str = f"https://searchservices001.search.windows.net"


embeddings: OpenAIEmbeddings = OpenAIEmbeddings(deployment=model, chunk_size=1)
index_name: str = "langchain-vector-demo"
vector_store: AzureSearch = AzureSearch(
    azure_search_endpoint=vector_store_address,
    azure_search_key="NMKbTz808lpljIgo7mZo47ZmxkksxLxdbDRrte6GFaAzSeCi7tMY",
    index_name=index_name,
    embedding_function=embeddings.embed_query,
)

loader = AzureBlobStorageContainerLoader(
    conn_str="DefaultEndpointsProtocol=https;AccountName=projectstorageaccount001;AccountKey=2us6XHpetXMhwvdpeTT+eRUIg6/kjWY3PvLTBCKkB6RK+aWCODsYKBQvTNEUS8+CfZ2MTVqXaWEq+AStwDYgNQ==;EndpointSuffix=core.windows.net",
    container="storagecontainer",
)
documents = loader.load()

text_splitter = CharacterTextSplitter(chunk_size=150, chunk_overlap=20)
docs = text_splitter.split_documents(documents)
vector_store.add_documents(documents=docs)

print("Data loaded into vectorstore successfully")
