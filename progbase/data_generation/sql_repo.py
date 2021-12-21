import random
import datetime


def sql_generate_device(num, connection):
    n = 0
    with connection.cursor() as cursor:
        while n <= num:
            cursor.execute(
                """INSERT INTO devices (device_name, measureg_object) values(
                    substr('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789',((random()*(36-1)+1)::integer),7),
                    substr('ABCDEFGHIJKLMNOPQRSTUVWXYZ',((random()*(26-1)+1)::integer),4)
                    )"""
            )
            n += 1


def sql_generate_indicator_temp(num, connection):
    n = 0
    min = __getfirstid(connection, "premise")
    max = __getcount(connection, "premises")
    with connection.cursor() as cursor:
        while n <= num:
            cursor.execute(
                """INSERT INTO indicators_temperature (temperature, premises, indicators_states) 
                    VALUES(
                    %s, %s,
                    substr('ABCDEFGHIJKLMNOPQRSTUVWXYZ',((random()*(26-1)+1)::integer),4)
                    )""" %
                (random.randint(-10, 30), random.randint(min, max + min - 1))
            )
            n += 1


def sql_generate_indicator_hum(num, connection):
    n = 0
    min = __getfirstid(connection, "premise")
    max = __getcount(connection, "premises")
    with connection.cursor() as cursor:
        while n <= num:
            cursor.execute(
                """INSERT INTO indicators_humidity (humidity, premises, indicators_states) 
                    VALUES(
                    %s, %s,
                    substr('ABCDEFGHIJKLMNOPQRSTUVWXYZ',((random()*(26-1)+1)::integer),4)
                    )""" %
                (random.randint(20, 70), random.randint(min, max + min - 1))
            )
            n += 1


def sql_generate_indicator_pres(num, connection):
    n = 0
    min = __getfirstid(connection, "premise")
    max = __getcount(connection, "premises")
    with connection.cursor() as cursor:
        while n <= num:
            cursor.execute(
                """INSERT INTO indicators_pressure (pressure, premises, indicators_states) 
                    VALUES(
                    %s, %s,
                    substr('ABCDEFGHIJKLMNOPQRSTUVWXYZ',((random()*(26-1)+1)::integer),4)
                    )""" %
                (random.randint(720, 790), random.randint(min, max + min - 1))
            )
            n += 1


def sql_generate_premise(num, connection):
    n = 0
    min = __getfirstid(connection, "device")
    max = __getcount(connection, "devices")
    with connection.cursor() as cursor:
        while n <= num:
            date = "2021-" + str(random.randint(1, 12)).zfill(2) + "-" + str(random.randint(1, 30)).zfill(2)
            cursor.execute(
                """INSERT INTO premises (premises_name, rooms_number, device, date) values(
                    substr('ABCDEFGHIJKLMNOPQRSTUVWXYZ',((random()*(26-1)+1)::integer),7),
                     %d, %d, CAST('%s' AS DATE))""" %
                (random.randint(1, 6), random.randint(min, max + min - 1), str(date))
            )
            n += 1


def __getfirstid(connection, name):
    table = name + 's'
    id = name + "_id"
    with connection.cursor() as cursor:
        cursor.execute(
            """SELECT %s FROM %s
            ORDER BY %s ASC
            LIMIT 1""" % (id, table, id)
        )
        c = cursor.fetchall()
        for i in c:
            min = i[0]
    return min


def __getcount(connection, name):
    with connection.cursor() as cursor:
        cursor.execute(
            """SELECT COUNT(*) FROM %s""" % name
        )
        c = cursor.fetchall()
        for i in c:
            max = i[0]
    return max


def add_device(connection, values):
    data = values.split(',')
    with connection.cursor() as cursor:
        cursor.execute(
            """INSERT INTO devices (device_name, measureg_object) VALUES('%s', '%s')""" % (data[0], data[1])
        )


def add_premises(connection, values):
    data = values.split(',')
    if not (isinstance(int(data[1]), int)):
        print("Not correct data!")
        return 0
    elif not (isinstance(data[2], int)) or get_dev_byid(connection, data[2]) is None:
        print("Not correct data!")
        return 0
    with connection.cursor() as cursor:
        cursor.execute(
            """INSERT INTO premises (premises_name, rooms_number, device, date) 
            VALUES('%s', %d, %d, '%s')""" % (data[0], int(data[1]), int(data[2]), datetime.date.today())
        )
    return 1


def add_ind_temp(connection, values):
    data = values.split(',')
    if not (isinstance(int(data[0]), int)):
        print("Not correct data!")
        return 0
    elif not (isinstance(int(data[1]), int)) or get_room_byid(connection, data[1]) is None:
        print("Not correct data!")
        return 0
    with connection.cursor() as cursor:
        cursor.execute(
            """INSERT INTO indicators_temperature (temperature, premises, indicators_states) 
            VALUES('%s', %d, '%s')""" % (int(data[0]), int(data[1]), data[2])
        )
    return 1


def add_ind_hum(connection, values):
    data = values.split(',')
    if not (isinstance(int(data[0]), int)):
        print("Not correct data!")
        return 0
    elif not (isinstance(int(data[1]), int)) or get_room_byid(connection, data[1]) is None:
        print("Not correct data!")
        return 0
    with connection.cursor() as cursor:
        cursor.execute(
            """INSERT INTO indicators_humidity (humidity, premises, indicators_states) 
            VALUES('%s', %d, '%s')""" % (int(data[0]), int(data[1]), data[2])
        )
    return 1


def add_ind_pres(connection, values):
    data = values.split(',')
    if not (isinstance(int(data[0]), int)):
        print("Not correct data!")
        return 0
    elif not (isinstance(int(data[1]), int)) or get_room_byid(connection, data[1]) is None:
        print("Not correct data!")
        return 0
    with connection.cursor() as cursor:
        cursor.execute(
            """INSERT INTO indicators_pressure (pressure, premises, indicators_states) 
            VALUES('%s', %d, '%s')""" % (int(data[0]), int(data[1]), data[2])
        )
    return 1


def get_dev_byid(connection, id_d):
    with connection.cursor() as cursor:
        cursor.execute(
            """SELECT device_id FROM devices
            WHERE EXISTS(SELECT device_id FROM devices
            WHERE device_id = %d)""" % int(id_d)
        )
        c = cursor.fetchall()
    return c


def get_room_byid(connection, id_d):
    with connection.cursor() as cursor:
        cursor.execute(
            """SELECT premise_id FROM premises
            WHERE premise_id = %d""" % int(id_d)
        )
        c = cursor.fetchall()
    return c