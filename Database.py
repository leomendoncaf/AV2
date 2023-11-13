from py2neo import Graph

class Database:
    def __init__(self, uri, username, password):
        self.graph = Graph(uri, auth=(username, password))

    def execute(self, query):
        with self.graph.begin() as tx:
            result = tx.run(query)
            return result.data()

    def close(self):
        self.graph.close()
