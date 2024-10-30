import sqlite3

class AccesoBackend:
    def __init__(self):
        self.conexion = sqlite3.connect('accesoFacturadb.db')
        self.cursor = self.conexion.cursor()

    def verificar_acceso(self, email, contrasena):
        """
        Verifica si existe un usuario con el email y contraseña dados.
        """
        try:
            # Consulta para verificar las credenciales con email y contraseña.
            self.cursor.execute(
                "SELECT * FROM usuarios WHERE email = ? AND contrasenia = ?",
                (email, contrasena)
            )
            datos = self.cursor.fetchone()
            return datos is not None  # Devuelve True si las credenciales son correctas
        except sqlite3.Error as e:
            print(f"Error al verificar acceso: {e}")
            return False

    def registrar_usuario(self, usuario, contrasena, email, telefono):
        """
        Registra un nuevo usuario en la base de datos.
        """
        try:
            self.cursor.execute(
                "INSERT INTO usuarios (usuario, contrasenia, email, tel) VALUES (?, ?, ?, ?)",
                (usuario, contrasena, email, telefono)
            )
            self.conexion.commit()
            print("Usuario registrado correctamente.")
        except sqlite3.Error as e:
            print(f"Error al registrar usuario: {e}")

    def cerrar_conexion(self):
        """
        Cierra la conexión con la base de datos.
        """
        self.conexion.close()
