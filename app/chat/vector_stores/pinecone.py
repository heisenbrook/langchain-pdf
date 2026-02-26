import os
from langchain.vectorstores.pinecone import Pinecone
from app.chat.embeddings.openai import embeddings

Pinecone(
    api_key=os.getenv('PINECONE_API_KEY'),
    environment=os.getenv('PINECONE_ENV_NAME')
)

vector_store = Pinecone.from_existing_index(

)
