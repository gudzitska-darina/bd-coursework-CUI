def __getdevicesname(connection):
    namelist = []
    with connection.cursor() as cursor:
        cursor.execute(
            """SELECT (device_name) FROM devices"""
        )
        c = cursor.fetchall()
        for i in c:
            name = i[0]
            namelist.append(name)
    return namelist


def create_index(connection):
    with connection.cursor() as cursor:
        cursor.execute(
            """CREATE INDEX index_device ON devices USING btree (device_name)"""
        )


def create_index_t(connection):
    with connection.cursor() as cursor:
        cursor.execute(
            """CREATE INDEX index_temp ON indicators_temperature USING btree (indicators_states)"""
        )


def drop_index(connection, name):
    with connection.cursor() as cursor:
        cursor.execute(
            """DROP INDEX %s""" % name
        )


def data_sampling_device(connection, value):
    with connection.cursor() as cursor:
        cursor.execute(
            """SELECT (device_name) FROM devices
            WHERE device_name = '%s'
            ORDER BY device_name ASC""" % str(value)
        )
        c = cursor.fetchall()
    return c


def data_sampling_temp(connection, temp, state):
    with connection.cursor() as cursor:
        cursor.execute(
            """
            SELECT * FROM indicators_temperature
            WHERE temperature > '%s' AND indicators_states = '%s'
            ORDER BY indicators_states ASC""" % (int(temp), str(state))
        )
        c = cursor.fetchall()
    return c


def data_search_dev_count(connection, value):
    with connection.cursor() as cursor:
        cursor.execute(
            """SELECT COUNT(1) FROM devices
            WHERE device_name = '%s'
            """ % str(value)
        )
        c = cursor.fetchall()
    return c


def data_search_dev_ex(connection, value):
    with connection.cursor() as cursor:
        cursor.execute(
            """SELECT device_id FROM devices
            WHERE EXISTS(SELECT device_name FROM devices
            WHERE device_name = '%s')""" % str(value)
        )
        c = cursor.fetchall()
    return c
