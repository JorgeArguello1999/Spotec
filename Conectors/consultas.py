try:
    from Conectors.database import connection as database
except:
    from database import connection as database

class formularios(database):

    def insertar_informacion(self, categoria:int, estilo:int):
        try:
            cur = self.conn.cursor()
            query = f"""
            INSERT INTO informacion (categoria, idestilo) 
            values ({categoria}, {estilo})
            """
            cur.execute()
            self.conn.commit()
        except:
            return False

if __name__ == '__main__':
    lin = formularios()
