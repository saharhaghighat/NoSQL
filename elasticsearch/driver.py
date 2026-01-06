from elasticsearch import Elasticsearch

# Create a client connection to the local Elasticsearch instance.
es = Elasticsearch("http://localhost:9200")


# Creating index
es.indices.create(
    index="my-logs",
    body={
        "settings": {"number_of_shards": 1, "number_of_replicas": 1},
        "mappings": {
            "properties": {
                "ts": {"type": "date"},
                "status": {"type": "integer"},
                "msg": {"type": "text"},
                "service": {"type": "keyword"},
            }
        },
    },
    ignore=400,
)

# Create Record

doc = {
    "service": "web",
    "status": 500,
    "msg": "err",
    "ts": "2025-10-12T10:01:00Z",
}

response = es.create(
    index="my-logs",
    id="42",
    document=doc,
)
print(response)


doc1 = {
    "service": "web",
    "status": 200,
    "msg": "ok",
    "ts": "2025-10-12T10:00:00Z",
}

doc2 = {
    "service": "api",
    "status": 201,
    "msg": "created",
    "ts": "2025-10-12T10:02:00Z",
}

res1 = es.index(
    index="my-logs",
    document=doc1,
)

res2 = es.index(
    index="my-logs",
    id="100",
    document=doc2,
)


print(res1)
print(res2)


# Get
response = es.get(
    index="my-logs",
    id="100",
)

print(response)

# Search
response = es.search(
    index="my-logs",
    body={
        "query": {"match": {"service": "web"}},
        "aggs": {"by_status": {"terms": {"field": "status"}}},
        "size": 5
    }
)

print(response)


# Update a field
response = es.update(
    index="my-logs",
    id="100",
    body={
        "doc": {
            "msg": "created-ok",
            "status": 202
        }
    }
)

print(response)

response = es.update(
    index="my-logs",
    id="200",
    body={
        "doc": {
            "service": "api",
            "status": 200,
            "msg": "upserted",
            "ts": "2025-10-12T10:10:00Z",
        },
        "doc_as_upsert": True,
    },
)
print(response)



# Delete

response = es.delete_by_query(
    index="my-logs",
    body={
        "query": {
            "term": {
                "service": "web"
            }
        }
    },
)