import os
import pytest

try:
	from neo4j import GraphDatabase
except Exception:
	pytest.skip("neo4j driver not installed", allow_module_level=True)


creds = {
	"neo4j-desktop": {
		"uri": "bolt://localhost:7687",
		"user": "neo4j",
		"password": "contraseña"
	},
	"neo4j-docker": {
		"uri": "bolt://localhost:7688",
		"user": "neo4j",
		"password": "12345678"
	},
	"memgraph-docker": {
		"uri": "bolt://localhost:7689",
		"user": "",
		"password": ""
	}
}


@pytest.mark.parametrize("db_location", ["neo4j-desktop", "neo4j-docker", "memgraph-docker"])
def test_local_neo4j_connection(db_location):
	uri = os.getenv("NEO4J_URI", creds[db_location]["uri"])
	user = os.getenv("NEO4J_USER", creds[db_location]["user"])
	password = os.getenv("NEO4J_PASSWORD", creds[db_location]["password"])

	driver = GraphDatabase.driver(uri, auth=(user, password))
	try:
		with driver.session() as session:
			result = session.run("RETURN 1 AS value")
			record = result.single()
			assert record is not None
			assert record["value"] == 1
	except Exception as e:
		pytest.fail(f"Failed to connect or run query against Neo4j at {uri}: {e}")
	finally:
		driver.close()
