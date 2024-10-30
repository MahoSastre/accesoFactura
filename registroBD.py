import sqlite3

class RegistroBD:
    def __init__(self, db_name):
        self.db_name = db_name

    def conectar(self):
        """Conecta a la base de datos."""
        return sqlite3.connect(self.db_name)

    def usuario_existe(self, usuario):
        """Verifica si el usuario ya existe en la base de datos."""
        conexion = self.conectar()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE usuario = ?", (usuario,))
        existe = cursor.fetchone() is not None
        conexion.close()
        return existe

    def registrar_usuario(self, usuario, contrasena, email, telefono):
        """Registra al usuario en la base de datos."""
        if self.usuario_existe(usuario):
            return False  # Usuario ya existe
        
        try:
            conexion = self.conectar()
            cursor = conexion.cursor()
            cursor.execute(
                "INSERT INTO usuarios (usuario, contrasenia, email, tel) VALUES (?, ?, ?, ?)",
                (usuario, contrasena, email, telefono)
            )
            conexion.commit()
            conexion.close()
            return True  # Registro exitoso
        except sqlite3.Error:
            return False  # Error al registrar

# Ejemplo de uso
if __name__ == "__main__":
    db = RegistroBD("accesoFacturadb.db")
    # Aquí puedes probar la funcionalidad
    usuario = "nuevo_usuario"
    contrasena = "contraseña123"
    email = "usuario@example.com"
    telefono = "1234567890"
    
    if db.registrar_usuario(usuario, contrasena, email, telefono):
        print("Usuario registrado correctamente.")
    else:
        print("El usuario ya existe o hubo un error al registrar.")
