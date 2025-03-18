from pprint import pprint
from elasticsearch import Elasticsearch


def connect_to_es(uri):
    es = Elasticsearch(uri)
    client_info = es.info()
    print('Connected to Elasticsearch')
    pprint(client_info.body)
    return es
