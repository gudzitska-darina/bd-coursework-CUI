import psycopg2
from config import host, user, password, db_name
import control
import sql_repo
import create_hist


def main():
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
        connection.autocommit = True

        while True:
            print("\nВведите название таблицы для которой хотите проверить средства быстродействия")
            command_input = input()
            command = command_input.split(' ')
            if command[0] == "devices":
                noind = control.check_speed_device(command[1], connection)
                sql_repo.create_index(connection)
                ind = control.check_speed_device(command[1], connection)
                sql_repo.drop_index(connection, 'index_device')
                val = [noind, ind]
                create_hist.generate_speed_index(val)
                continue
            elif command[0] == "indicators.temp":
                noind = control.check_speed_temp(command[1], command[2], connection)
                sql_repo.create_index_t(connection)
                ind = control.check_speed_temp(command[1], command[2], connection)
                sql_repo.drop_index(connection, 'index_temp')
                val = [noind, ind]
                create_hist.generate_speed_index(val)
                continue
            elif command[0] == "devices.search":
                count = control.check_speed_count(command[1], connection)
                ex = control.check_speed_ex(command[1], connection)
                val = [count, ex]
                create_hist.generate_speed_count(val)
                continue
            elif command[0] == "devices.hist":
                create_hist.generate_device_hist(connection)
                continue
            elif command[0] == "stop":
                break
            else:
                print("Таблица не найдена!")
                continue

        print("\nGoodBye)")
    except Exception as _ex:
        print("[INFO] Error with connection PostgreSQL", _ex)
    finally:
        if connection:
            connection.close()
            print("[INFO] Connection closed")


if __name__ == '__main__':
    main()

