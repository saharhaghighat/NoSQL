from elasticsearch import Elasticsearch

# Create a client connection to the local Elasticsearch instance.
es = Elasticsearch("http://localhost:9200")
