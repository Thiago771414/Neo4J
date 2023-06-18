from neo4jrestclient.client import GraphDatabase
from neo4j import GraphDatabase

uri = "bolt://localhost:7687"
username = "neo4j"
password = "neo4j"

driver = GraphDatabase.driver(uri, auth=(username, password))
session = driver.session()

# Create some nodes with labels
with session.begin_transaction() as tx:
    tx.run("CREATE (:Usuario {name: 'Bob'})-[:follows]->(:Usuario {name: 'Alice'})")
    tx.run("CREATE (:Usuario {name: 'Lea'})-[:follows]->(:Usuario {name: 'Alice'})")
    tx.run("CREATE (:Usuario {name: 'Ana'})-[:follows]->(:Usuario {name: 'Bob'})")
    tx.run("CREATE (:Usuario {name: 'Alice'})-[:follows]->(:Usuario {name: 'Joel'})")
