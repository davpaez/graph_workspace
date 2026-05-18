from neo4j import GraphDatabase

# driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "contraseña"))
driver = GraphDatabase.driver("bolt://localhost:7688", auth=("neo4j", "12345678"))

with driver.session() as session:
    # result = session.run("MATCH (n) RETURN n")
    result = session.run("RETURN 1 AS value")
    for record in result:
        print(record)

driver.close()