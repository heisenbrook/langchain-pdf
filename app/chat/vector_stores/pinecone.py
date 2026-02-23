import os
import pinecone
from pinecone import Pinecone
from app.chat.embeddings.openai import embeddings

pinecone.Pinecone(
    api_key= os.getenv('PINECONE_API_KEY'),
    environment= os.getenv('PINECONE_ENV_NAME')
)

