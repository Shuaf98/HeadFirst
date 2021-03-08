from DBCm import UseDatabase


dbconfig = {'host': '127.0.0.1',
            'user': 'root',
            'password': 'root',
            'database': 'datarequestDB'
            }
with UseDatabase(dbconfig) as cursor:
    _SQL = """show tables"""
    cursor.execute(_SQL)
    data = cursor.fetchall()
            
    
                 