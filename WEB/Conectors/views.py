try:
    from Conectors.database import connection as database
except:
    from database import connection as database

class vistas(database):

    def lista_categorias(self):
        cur = self.conn.cursor()
        cur.execute("""
        select informacion.idevento, informacion.categoria, estilos.nombre
        from informacion
        inner join estilos
        on informacion.idestilo = estilos.idestilo
        """)
        cur.fetchall
        return cur


    def lista_categorias_fill(self, idevento):
        cur = self.conn.cursor()
        cur.execute(f"""
        select informacion.idevento, informacion.categoria, estilos.nombre
        from informacion
        inner join estilos
        on informacion.idestilo = estilos.idestilo
        where idevento={idevento}
        """)
        cur.fetchall
        return cur

    def tabla_juego(self):
        cur = self.conn.cursor()
        cur.execute("""
        select informacion.idevento, informacion.categoria, estilos.nombre,
        juegos.serie, jugadores.nombres 'jnombres', jugadores.edad, equipos.nombre 'enombre', 
        jugadores.tiempo

        from informacion
        inner join estilos
        on informacion.idestilo = estilos.idestilo
        inner join juegos
        on informacion.idevento = juegos.idevento
        inner join jugadores
        on juegos.idjugador = jugadores.idjugador
        inner join equipos
        on jugadores.idequipo = equipos.idequipo 
        """)
        cur = cur.fetchall()
        return cur

    def tabla_juego_categoria(self, categoria):
        cur = self.conn.cursor()
        cur.execute(f"""
        select informacion.idevento, informacion.categoria, estilos.nombre,
        juegos.serie, jugadores.nombres 'jnombres', jugadores.edad, equipos.nombre 'enombre', 
        jugadores.tiempo

        from informacion
        inner join estilos
        on informacion.idestilo = estilos.idestilo
        inner join juegos
        on informacion.idevento = juegos.idevento
        inner join jugadores
        on juegos.idjugador = jugadores.idjugador
        inner join equipos
        on jugadores.idequipo = equipos.idequipo 
        where categoria = {categoria}
        """)
        cur = cur.fetchall()
        return cur



if __name__ == '__main__':
    lin = vistas()
    lin.tabla_juego()
