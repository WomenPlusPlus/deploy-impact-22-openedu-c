import pyodbc
server = 'openeduc-server.database.windows.net'
database = 'openeduc-db'
username = 'openeduc-admin@openeduc-server'
password = 'deploy-impact-2022'
driver = '{ODBC Driver 18 for SQL Server}'

with pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
    print(conn)
    with conn.cursor() as cursor:
        cursor.execute("SELECT TOP 3 name, collation_name FROM sys.databases")
        row = cursor.fetchone()
        while row:
            print(str(row[0]) + " " + str(row[1]))
            row = cursor.fetchone()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mssql-django',
        'NAME': 'openeduc-db',
        'USER': 'openeduc-admin@openeduc-server',
        'PASSWORD': 'deploy-impact-2022',
        'HOST': 'openeduc-server.database.windows.net',
        'PORT': '1433',
        'OPTIONS': {
            'driver': 'ODBC Driver 18 for SQL Server',
        },
    },
}
