import csv
import itertools
import elasticsearch as es_lib
from time import sleep
from elasticsearch import Elasticsearch


def conf(index_name: str = "csv_info"):
    es = Elasticsearch("http://localhost:9200")
    try:
        es.indices.get(index=index_name)
    except es_lib.exceptions.NotFoundError:
        es.indices.create(index=index_name)
    return es


def from_scv_to_es(es_obj, file: str):
    with open(file, encoding="UTF-8") as csvfile:
        keys = csvfile.readline().split(',')
        for i in csv.reader(csvfile):
            dict_obj = dict(itertools.zip_longest(keys, i[0].split(','), fillvalue=None))
            es_obj.index(index="csv_info", body=dict_obj, id=dict_obj['customers_id'])


def search(es_obj, size: int = 30):
    sleep(1)
    for i in es_obj.search(index='csv_info', size=size)["hits"]["hits"]:
        print(i['_source'])


if __name__ == "__main__":
    es_conf = conf()
    from_scv_to_es(es_conf, "test.csv")
    search(es_conf)
    # es_conf.indices.delete(index="csv_info")
