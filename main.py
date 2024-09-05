# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import psycopg2
from psycopg2 import Error
import json
import ftplib
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
  # Press Ctrl+F8 to toggle the breakpoint.
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="1234",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="netologyTarasyuk")
        cursor = connection.cursor()

        print("Информация о сервере PostgreSQL")
        print(connection.get_dsn_parameters(), "\n")

        cursor.execute("SELECT  * from Песни LIMIT 10;")
        record = cursor.fetchall()

        di = {}
        for uy in record:
            per = {}
            per["name"] = uy[1]
            per["time"] = str(uy[2])
            di[uy[0]] = per
        print(di)
        filename = 'new'
        with open('C:/Users/1/Desktop/new/newdata.json', 'w') as outfile:
            json.dump(di, outfile,ensure_ascii=False)


        # Fill Required Information
        HOSTNAME = "ftp.dlptest.com"
        USERNAME = "dlpuser@dlptest.com"
        PASSWORD = "eUj8GeW55SvYaswqUyDSm5v6N"

        ftp_server = ftplib.FTP(HOSTNAME, USERNAME, PASSWORD)
        ftp_server.encoding = "utf-8"
        filename = "File Name"

        # Read file in binary mode
        with open(filename, "rb") as file:
            # Command for Uploading the file "STOR filename"
            ftp_server.storbinary(f"STOR {filename}", file)

        ftp_server.dir()

        # Close the Connection

        # Convert person dictionary to JSON
        # json_string = json.dumps(record, indent=4)
        # print(json_string)
        print("Вы подключены к - ", "\n")

    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            ftp_server.quit()
            print("Соединение с PostgreSQL закрыто")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
