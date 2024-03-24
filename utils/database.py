import os
from neo4j import GraphDatabase, basic_auth


def read_query(query, params=None):
    driver = GraphDatabase.driver(
        os.getenv("NEO4J_URI"), auth=basic_auth("neo4j", "allocations-winches-routines")
    )

    with driver.session(database="neo4j") as session:
        results = session.execute_read(lambda tx: tx.run(query, params).data())

    driver.close()

    return results


def write_query(query, params=None):
    driver = GraphDatabase.driver(
        os.getenv("NEO4J_URI"), auth=basic_auth("neo4j", "allocations-winches-routines")
    )

    with driver.session(database="neo4j") as session:
        results = session.execute_write(lambda tx: tx.run(query, params))

    driver.close()

    return results
