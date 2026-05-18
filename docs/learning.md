Memgraph lab
	can:
		be used to connect, explore and query both Neo4j and Memgraph DBs
		do most of the thins that Neo4j Bloom can do, like exploring the graph interactively
	For connecting to docker service:
		use docker service name (as hostname) and internal port
	For connecting to service running outside docker (in the host machine):
		use `host.docker.internal` (as hostname) and port (as seen from the host machine)
		This is useful for connecting memgraph-lab running inside docker to Neo4j desktop running outside docker as a normal application


Neo4j python driver can be used to connect and manipulate both Neo4j and Memgraph DBs

Desktop Neo4j browser 
	can:
		host multiple local DBS and use the tools: Import, Query, Explore (Bloom) and Dashboards
		connect to local docker instances of Neo4j, but does not allow to use Explore (Bloom)
	cannot:
		connect to memgraph engine

Desktop Neo4j Import tool can:
	Import graphs from CSV interactively
	Define a schema graphically to restrict and shape the importing

Thanks to the previous connection possibilities:
	I can manipulate a local Neo4J DB from Python, Neo4J desktop and docker Memcache lab
	I can manipulate any graph DB anywhere from Python using Neo4j driver for Python

Puedo usar notebooks y acceder a este kernel de pixi tanto desde VSCode (con jupyterlab extension) como de un conda env especificamente creado para jupyterlab
