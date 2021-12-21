import sql_repo
import time


def check_speed_device(value, connection):
    start_time = time.time()
    sql_repo.data_sampling_device(connection, value)
    return time.time() - start_time


def check_speed_temp(value1, value2, connection):
    start_time = time.time()
    sql_repo.data_sampling_temp(connection, value1, value2)
    return time.time() - start_time


def check_speed_count(value, connection):
    start_time = time.time()
    sql_repo.data_search_dev_count(connection, value)
    return time.time() - start_time


def check_speed_ex(value, connection):
    start_time = time.time()
    sql_repo.data_search_dev_ex(connection, value)
    return time.time() - start_time
