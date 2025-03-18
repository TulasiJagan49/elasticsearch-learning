from elasticsearch_connection import connect_to_es


def create_index(es_client, index_name, settings={}):
    es_client.indices.delete(index=index_name, ignore_unavailable=True)
    if settings:
        es_client.indices.create(index=index_name, settings=settings)
    else:
        es_client.indices.create(index=index_name)
    print(es_client.indices.get_alias().keys())

if __name__=="__main__":
    es = connect_to_es('http://localhost:9200')
    create_index(es, "sample_index")

    # We can adjust the number of shards and replicas,
    # by updating the settings, while creating an index.
    create_index(es, "sample_index", settings={
        "index": {
            "number_of_shards": "3",
            "number_of_replicas": "2"
        }
    })
