In this project I will test several graph technologies and use cases

Technologies:
- Neo4j
- Memgraph
- Gel
- Datomic

Tools
- Connectors
	- Neo4j python driver
	- GQLAlchemy
- Analysers
	- NetworkX
- Visualization
	- pyvis
	- jaal
	- orb (JS for browser)
	- Plotly?
	- D3?
	- Cytoscape? (JS)
	- memgraph lab
	- neo4j bloom

Use cases:
- Building strutural graph from text
- Building semantic graph from text
- GraphRAG
- 

# Prerequisites

Basic
- Pixi installed globally
- Justfile installed globally
- Docker Desktop installed and running: used for DB instances (neo4j, memgraph) and tools such as memgraph-lab

For running things:
- Run docker containers with `just up`. Precede with `just down` in case you want to make sure to start clean
- Run tests with `pixi run test`
- Run main witn `pixi run main`
