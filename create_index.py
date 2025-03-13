from elasticsearch import Elasticsearch
from pprint import pprint

es = Elasticsearch('http://localhost:9200/')
client_info = es.info()
print('Connected to Elasticsearch')
pprint(client_info.body)

es.indices.delete(index="example_index", ignore_unavailable=True)
es.indices.create(index="example_index")
print(es.indices.get_alias().keys())

# We can adjust the number of shards and replicas,
# by updating the settings, while creating an index.
es.indices.delete(index="example_index", ignore_unavailable=True)
es.indices.create(index="example_index", settings={
    "index": {
        "number_of_shards": "3",
        "number_of_replicas": "2"
    }
})
print(es.indices.get_alias().keys())
