from conexion import Conexion

class Usuario:

    def __init__(self, id_usuario=None, username=None, email=None, contrasena=None, id_rol=None):
        self.id_usuario = id_usuario
        self.username = username
        self.email = email
        self.contrasena = contrasena
        self.id_rol = id_rol

    def login(self):
     conexion = Conexion().conectar()

     cursor = conexion.cursor()

     sql = """
     SELECT
        u.id_usuario,
        u.username,
        r.nombre_rol
     FROM usuario u
     INNER JOIN rol r
        ON u.id_rol = r.id_rol
     WHERE u.username = %s
      AND u.contrasena = %s
     """

     cursor.execute(sql, (self.username, self.contrasena))

     usuario = cursor.fetchone()

     conexion.close()

     return usuario