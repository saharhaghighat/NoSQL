from neo4j import GraphDatabase
class Neo4jDatabase:
    def __init__(self, uri, username, password):
        self.driver = GraphDatabase.driver(uri, auth=(username, password))

    def __exit__(self, exc_type, exc_val, traceback):
        self.driver.close()

    def __enter__(self):
        return self

    def execute_query(self, query, parameters=None):
        with self.driver.session() as session:
            result =session.run(query, parameters=parameters or {})
            return [record.data() for record in result]