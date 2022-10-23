import logging
import time

import psycopg2.extras
from redis import Redis

from etl import ETLProcess
from settings import ELASTIC_HOST, ELASTIC_PORT, TIME_SLEEP, REDIS_HOST, REDIS_PORT
from settings import dsl
from state import State, RedisStorage


def load_data(url: str, port: int, table_name: str) -> None:
    """Основная функция переноса всех данных из PostgreSQL в Elasticsearch"""
    # for state_name in state_names:
    while True:
        data, state = etl.extract(table_name)
        if len(data) == 0:
            return
        etl.loader(data, url, port, state)


if __name__ == '__main__':
    logger = logging.getLogger()
    logging.basicConfig(level=logging.INFO)

    elastic_host = ELASTIC_HOST
    elastic_url = 'http://{}'.format(elastic_host)
    elastic_port = ELASTIC_PORT
    time_sleep = TIME_SLEEP
    redis_host = REDIS_HOST
    redis_port = REDIS_PORT
    file_storage = RedisStorage(Redis(
        host=redis_host, port=redis_port, db=0))
    table_names = ['film_work', 'person', 'genre']
    states = State(storage=file_storage)
    if states.get_state('modified') is None:
        states.set_state('modified', '1000-04-10')
    while True:
        with psycopg2.connect(
                **dsl, cursor_factory=psycopg2.extras.RealDictCursor
        ) as pg_conn:
            etl = ETLProcess(pg_conn, states)
            for name in table_names:
                load_data(elastic_url, elastic_port, name)
                logger.info('successful genre {} transfer'.format(name))
        logger.info('successful transfer of all tables')
        pg_conn.close()
        time.sleep(time_sleep)
