T: Make python test connection to neo4j instance work. I think it is caused by docker ports/networks.
	R: OK.
		S: It was an encoding error in Neo4j 3.15 docker image. Didn't work with ñ character in password
T: Make python test connection to memgraph instance work. I think it is caused by docker ports/networks.
	R: OK. It worked just fine
