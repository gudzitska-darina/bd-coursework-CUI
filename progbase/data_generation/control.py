import sql_repo


def generate_devices(num, connection):
    sql_repo.sql_generate_device(num, connection)
    print("[INFO] Data for 'devices' generate successful")


def generate_indicators_temp(num, connection):
    sql_repo.sql_generate_indicator_temp(num, connection)
    print("[INFO] Data for 'indicators_temperature' generate successful")


def generate_indicators_hum(num, connection):
    sql_repo.sql_generate_indicator_hum(num, connection)
    print("[INFO] Data for 'indicators_humidity' generate successful")


def generate_indicators_pres(num, connection):
    sql_repo.sql_generate_indicator_pres(num, connection)
    print("[INFO] Data for 'indicators_pressure' generate successful")


def generate_premises(num, connection):
    sql_repo.sql_generate_premise(num, connection)
    print("[INFO] Data for 'premises' generate successful")


def add_device(data, connection):
    sql_repo.add_device(connection, data)
    print("[INFO] Add to 'devices' successful")


def add_premises(data, connection):
    if sql_repo.add_premises(connection, data) == 1:
        print("[INFO] Add to 'premises' successful")
    else:
        return


def add_temp(data, connection):
    if sql_repo.add_ind_temp(connection, data) == 1:
        print("[INFO] Add to 'indicators.temp' successful")
    else:
        return


def add_hum(data, connection):
    if sql_repo.add_ind_hum(connection, data) == 1:
        print("[INFO] Add to 'indicators.humidity' successful")
    else:
        return


def add_pres(data, connection):
    if sql_repo.add_ind_pres(connection, data) == 1:
        print("[INFO] Add to 'indicators.pressure' successful")
    else:
        return
