import json
from pprint import pprint

from elasticsearch_connection import connect_to_es
from create_index import create_index


es = connect_to_es('http://localhost:9200')
create_index(es, "sample_index")

document_ids = []
dummy_data = json.load(open('dummy_data.json', encoding='utf-8'))
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
