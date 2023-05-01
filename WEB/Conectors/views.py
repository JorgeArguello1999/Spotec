try:
    from Conectors.database import connection as database
except:
    from database import connection as database

class vistas(database):

    # Tablas de juego y categorias
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
        jugadores.tiempo, provincias.nombre 'provincia'

        from informacion
        inner join estilos
        on informacion.idestilo = estilos.idestilo
        inner join juegos
        on informacion.idevento = juegos.idevento
        inner join jugadores
        on juegos.idjugador = jugadores.idjugador
        inner join equipos
        on jugadores.idequipo = equipos.idequipo 
        inner join provincias
        on equipos.idprovincia = provincias.idprovincia
        """)
        cur = cur.fetchall()
        return cur

    def tabla_juego_categoria(self, idevento):
        cur = self.conn.cursor()
        cur.execute(f"""
        select informacion.idevento, informacion.categoria, estilos.nombre,
        juegos.serie, jugadores.nombres 'jnombres', jugadores.edad, equipos.nombre 'enombre', 
        jugadores.tiempo, provincias.nombre 'provincia'

        from informacion
        inner join estilos
        on informacion.idestilo = estilos.idestilo
        inner join juegos
        on informacion.idevento = juegos.idevento
        inner join jugadores
        on juegos.idjugador = jugadores.idjugador
        inner join equipos
        on jugadores.idequipo = equipos.idequipo 
        inner join provincias
        on equipos.idprovincia = provincias.idprovincia
        where informacion.idevento = {idevento}
        """)
        cur = cur.fetchall()
        return cur

    # Jugadores
    def listar_jugadores(self):
        cur = self.conn.cursor()
        cur.execute(f"""
        select jugadores.idjugador, jugadores.nombres, jugadores.edad, jugadores.fnacimiento,
        jugadores.tiempo, equipos.nombre, provincias.nombre 'pnombre', jugadores.cedula
        from jugadores
        inner join equipos
        on jugadores.idequipo = equipos.idequipo
        inner join provincias
        on equipos.idprovincia = provincias.idprovincia;
        """)
        cur = cur.fetchall()
        return cur

    def listar_jugadores_fill(self, provincia= None, cedula=None):
        cur = self.conn.cursor()
        cur.execute("""
        select jugadores.idjugador, jugadores.nombres, jugadores.edad, jugadores.fnacimiento,
        jugadores.tiempo, equipos.nombre, provincias.nombre 'pnombre', jugadores.cedula
        from jugadores
        inner join equipos
        on jugadores.idequipo = equipos.idequipo
        inner join provincias
        on equipos.idprovincia = provincias.idprovincia
        where provincias.idprovincia = %s or jugadores.cedula = %s
        """, (provincia, cedula))
        cur = cur.fetchall()
        return cur

    # Provincias
    def lista_provincias(self):
        cur = self.conn.cursor()
        cur.execute(f"""
        select *
        from provincias
        """)
        cur = cur.fetchall()
        return cur

    # Equipos
    def lista_equipos(self):
        cur = self.conn.cursor()
        cur.execute(f"""
        SELECT DISTINCT equipos.nombre FROM equipos
        inner join jugadores
        on jugadores.idequipo = equipos.idequipo
        inner join entrenadores
        on entrenadores.identrenador = equipos.identrenador
        order by equipos.nombre
        """)
        cur = cur.fetchall()
        return cur

if __name__ == '__main__':
    lin = vistas()
    lin.tabla_juego()
