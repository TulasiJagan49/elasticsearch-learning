from elasticsearch import Elasticsearch
from pprint import pprint

import json

es = Elasticsearch('http://localhost:9200/')
client_info = es.info()
print('Connected to Elasticsearch')
pprint(client_info.body)

es.indices.delete(index="sample_index", ignore_unavailable=True)
es.indices.create(index="sample_index")
print(es.indices.get_alias().keys())

document = {
    'title': 'title',
    'text': 'text',
    'created_on': '2024-09-22',
}
response = es.index(index="sample_index", body=document)
print(response)

# Insert multiple documents
dummy_data = json.load(open("./dummy_data.json"))

def insert_document(index, document):
    response = es.index(index=index, body=document)
    return response

def print_info(response):
    print(f"Document ID: {response['_id']}")

for document in dummy_data:
    response = insert_document(index="sample_index", document=document)
    print_info(response)


# Elasticsearch infers the mapping of index from the inserted
# automatically.
index_mapping = es.indices.get_mapping(index="sample_index")
pprint(index_mapping["sample_index"]["mappings"]["properties"])

# We can also manually create a mapping for a index,
# but needs to be done before inserting a document
# into the index.

mapping = {
    "properties": {
        "created_on": {
            "type": "date"
        },
        "text": {
            "type": "text",
            "fields": {
                "keyword": {
                    "type": "keyword",
                    "ignore_above": 256
                }
            }
        },
        "title": {
            "type": "text",
            "fields": {
                "keyword": {
                    "type": "keyword",
                    "ignore_above": 256
                }
            }
        }
    }
}

es.indices.delete(index="sample_index", ignore_unavailable=True)
es.indices.create(index="sample_index")

es.indices.put_mapping(index="sample_index", body=mapping)
# we can also assign the mapping while creating index, like this:
# es.indices.create(index="sample_index", mappings=mapping)

index_mapping = es.indices.get_mapping(index="sample_index")
pprint(index_mapping["sample_index"]["mappings"]["properties"])