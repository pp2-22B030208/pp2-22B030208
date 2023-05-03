import csv, psycopg2

config = psycopg2.connect(
    host = 'localhost',
    database = 'postgres',
    password = 'M@20031211di',
    user = 'postgres'
)
current = config.cursor()
arr = []
with open('1.csv') as f:
    reader = csv.reader(f, delimiter=',')

    for row in reader:
        row[0] = int(row[0])
        arr.append(row)

sql = '''
    INSERT INTO phonebook VALUES (%s, %s, %s) RETURNING *; 
'''

for row in arr:
    current.execute(sql, row)

final = current.fetchall()
print(final)

current.close()
config.commit()
config.close()