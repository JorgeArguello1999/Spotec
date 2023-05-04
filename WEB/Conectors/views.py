try:
    from Conectors.database import connection as database
except:
    from database import connection as database

import itertools

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

    def lista_genero(self):
        cur = self.conn.cursor()
        cur.execute("""
        select * from genero
        """)
        cur.fetchall
        return cur

    def lista_estilos(self):
        cur = self.conn.cursor()
        cur.execute("""
        select * from estilos
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

    # Experimentando
    def maquetador_tabla(self, data):
        group_data = itertools.groupby(data, key=lambda x: x['idevento'])

        result_dict = {}
        for key, group in group_data:
            result_dict[key] = list(group)

        print("Dict: ", result_dict)
        return result_dict

    def maquetador_filtro(self, data):
        group_data = itertools.groupby(data, key=lambda x: x['idjugador'])

        result_dict = {}
        for key, group in group_data:
            result_dict[key] = list(group)

        print("Dict: ", result_dict)
        return result_dict


    def tabla_juego(self):
        cur = self.conn.cursor()
        cur.execute("""
        select informacion.idevento, informacion.categoria, estilos.nombre,
        juegos.serie, jugadores.nombres 'jnombres', jugadores.edad, equipos.nombre 'enombre', 
        juegos.tiempo_juego 'tiempo', provincias.nombre 'provincia'

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
        return self.maquetador_tabla(cur)

    def tabla_juego_categoria(self, idevento):
        cur = self.conn.cursor()
        cur.execute(f"""
        select informacion.idevento, informacion.categoria, estilos.nombre,
        juegos.serie, jugadores.nombres 'jnombres', jugadores.edad, equipos.nombre 'enombre', 
        juegos.tiempo_juego 'tiempo', provincias.nombre 'provincia'

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
        return self.maquetador_tabla(cur)

    def tabla_juego_genero_estilo(self, idgenero=1, idestilo=2):
        cur = self.conn.cursor()
        cur.execute(f"""
        select informacion.idevento, informacion.categoria, estilos.nombre,
        juegos.serie, jugadores.nombres 'jnombres', jugadores.edad, equipos.nombre 'enombre', 
        juegos.tiempo_juego 'tiempo', provincias.nombre 'provincia'

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
        where informacion.idgenero = {idgenero} and estilos.idestilo = {idestilo}
        """)
        cur = cur.fetchall()
        return self.maquetador_tabla(cur)

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
        on equipos.idprovincia = provincias.idprovincia
        order by jugadores.nombres ASC;
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
    def lista_equipos(self, cedula, idjugador):
        cur = self.conn.cursor()
        cur.execute(f"""
        select jugadores.idjugador, informacion.categoria,
        jugadores.nombres, equipos.nombre, provincias.nombre 'provincia', jugadores.edad,
        jugadores.cedula, juegos.tiempo_juego 'tiempo', estilos.nombre 'estilo'
        from juegos
        inner join informacion
        on juegos.idevento = informacion.idevento
        inner join jugadores
        on juegos.idjugador = jugadores.idjugador
        inner join estilos
        on informacion.idestilo = estilos.idestilo
        inner join equipos
        on equipos.idequipo = jugadores.idequipo
        inner join provincias
        on equipos.idprovincia = provincias.idprovincia
        where jugadores.cedula = {cedula} or jugadores.idjugador = {idjugador};
        """)
        cur = cur.fetchall()
        return self.maquetador_filtro(cur)

if __name__ == '__main__':
    lin = vistas()
    lin.tabla_juego()
