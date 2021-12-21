import psycopg2
import keyboard
import time
from config import host, user, password, db_name
import control


def main():
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
        connection.autocommit = True
        print("This part of the program is used to generate data for the database.")
        print("1 - generation by sql methods; \n2 - user input; \n 0 - exit.")
        while keyboard.read_key() != "0":
            if keyboard.read_key() == "1":
                while True:
                    print("\nВведите название таблицы и количество данных")
                    command_input = input()
                    command = command_input.split(' ')
                    if command[0] == "devices":
                        control.generate_devices(int(command[1]), connection)
                        continue
                    elif command[0] == "premises":
                        control.generate_premises(int(command[1]), connection)
                        continue
                    elif command[0] == "indicators.temp":
                        control.generate_indicators_temp(int(command[1]), connection)
                        continue
                    elif command[0] == "indicators.humidity":
                        control.generate_indicators_hum(int(command[1]), connection)
                        continue
                    elif command[0] == "indicators.pressure":
                        control.generate_indicators_pres(int(command[1]), connection)
                        continue
                    elif command[0] == "stop":
                        break
                    else:
                        print("Таблица не найдена!")
                        continue
            elif keyboard.read_key() == "2":
                while True:
                    print("\nВведите название таблицы и данные через запитую и без пробелов!")
                    command_input = input()
                    command = command_input.split(' ')
                    if command[0] == "devices":
                        data = command[1].split(',')
                        if len(data) != 2:
                            print("[INFO] Not correct amount of data")
                            continue
                        else:
                            control.add_device(command[1], connection)
                            continue
                    elif command[0] == "premises":
                        data = command[1].split(',')
                        if len(data) != 3:
                            print("[INFO] Not correct amount of data")
                            continue
                        else:
                            control.add_premises(command[1], connection)
                            continue
                    elif command[0] == "indicators.temp":
                        data = command[1].split(',')
                        if len(data) != 3:
                            print("[INFO] Not correct amount of data")
                            continue
                        else:
                            control.add_temp(command[1], connection)
                            continue
                    elif command[0] == "indicators.humidity":
                        data = command[1].split(',')
                        if len(data) != 3:
                            print("[INFO] Not correct amount of data")
                            continue
                        else:
                            control.add_hum(command[1], connection)
                            continue
                    elif command[0] == "indicators.pressure":
                        data = command[1].split(',')
                        if len(data) != 3:
                            print("[INFO] Not correct amount of data")
                            continue
                        else:
                            control.add_pres(command[1], connection)
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

