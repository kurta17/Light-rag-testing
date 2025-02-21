import os
from dotenv import load_dotenv
from lightrag import LightRAG, QueryParam
from lightrag.llm.openai import gpt_4o_mini_complete, gpt_4o_complete, openai_embed
from lightrag.utils import EmbeddingFunc
import pdfplumber
from neo4j import GraphDatabase
from lightrag.kg.neo4j_impl import Neo4JStorage

load_dotenv()

NEO4J_URI = os.getenv("NEO4J_URI")
NEO4J_USER = os.getenv("NEO4J_USER")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")

book = "ikigai.pdf"

WORKING_DIR = "./local_neo4jWorkDir"

if not os.path.exists(WORKING_DIR):
    os.mkdir(WORKING_DIR)


rag = LightRAG(
    working_dir=WORKING_DIR,
    embedding_func=openai_embed,
    llm_model_func=gpt_4o_mini_complete,
    chunk_token_size=1200,
    graph_storage="Neo4JStorage",
)

with pdfplumber.open(book) as pdf:
    text = ""
    for page in pdf.pages:
        text += page.extract_text()
# from txt file extract text and insert into rag (longlife-post.txt)
with open("longlife-post.txt") as f:
    post = f.read()
    rag.insert(post)


rag.insert(text)
# global search
print(rag.query("What is the meaning of ikigai?", param=QueryParam(mode="global")))

# local search
print(rag.query("what is the secret of living long?", param=QueryParam(mode="local")))

