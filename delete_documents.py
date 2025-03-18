from pprint import pprint
from elasticsearch import Elasticsearch


es = Elasticsearch('http://localhost:9200')
client_info = es.info()
print('Connected to Elasticsearch!')
pprint(client_info.body)

print(es.indices.get_alias())

es.indices.delete(index='sample_index', ignore_unavailable=True)
es.indices.create(index='sample_index')

import json

document_ids = []
dummy_data = json.load(open('dummy_data.json'))
for document in dummy_data:
    response = es.index(index='sample_index', body=document)
    document_ids.append(response['_id'])

response = es.delete(index='sample_index', id=document_ids[0])
pprint(response.body)

# When we try to delete a document, by an id not in index
# es throws 404 not found exception
try:
    response = es.delete(index='sample_index', id="random_id")
except Exception as e:
    print(e)
