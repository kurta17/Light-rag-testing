from neo4j import GraphDatabase
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

NEO4J_URI = os.getenv("NEO4J_URI")
NEO4J_USER = os.getenv("NEO4J_USER")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")

# Create Neo4j connection
driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

def test_connection():
    try:
        with driver.session() as session:
            result = session.run("RETURN '✅ Connected to Neo4j' AS msg")
            for record in result:
                print(record["msg"])  # Expected output: "✅ Connected to Neo4j"
    except Exception as e:
        print("❌ Connection failed:", e)

test_connection()
driver.close()
