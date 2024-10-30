import tkinter as tk
from tkinter import messagebox
from registroBD import RegistroBD  # Importar la clase RegistroBD

class RegistroUsuario:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Registro de usuarios")
        self.ventana.geometry("500x500")

        # Crear el contenido de la interfaz
        self.crear_interfaz()

        self.bd = RegistroBD("accesoFacturadb.db")  # Inicializar la base de datos
        self.ventana.mainloop()

    def crear_interfaz(self):
        # Título
        titulo = tk.Label(self.ventana, text="Registro de usuarios", font=("Arial", 24))
        titulo.pack(pady=10)

        # Campos de entrada
        self.entry_usuario = self.crear_campo("usuario")
        self.entry_contrasena = self.crear_campo("contraseña", mostrar="*")
        self.entry_repetir_contrasena = self.crear_campo("Repetir contraseña", mostrar="*")
        self.entry_email = self.crear_campo("e-mail")
        self.entry_telefono = self.crear_campo("No. móvil")

        # Botón de registrar
        btn_registrar = tk.Button(self.ventana, text="registrar", command=self.registrar_usuario, bg="#5DADE2", width=10)
        btn_registrar.pack(pady=20)

        # Botón de regreso en la esquina superior derecha
        btn_volver = tk.Button(self.ventana, text="↩", command=self.volver, bg="#AED6F1", font=("Arial", 14))
        btn_volver.place(x=450, y=10)  # Ubicación en la esquina superior derecha

    def crear_campo(self, placeholder, mostrar=None):
        """Crea un campo de entrada con un texto de placeholder."""
        entry = tk.Entry(self.ventana, font=("Arial", 14), show=mostrar)
        entry.insert(0, placeholder)
        entry.bind("<FocusIn>", lambda event, e=entry: self.limpiar_placeholder(e, placeholder))
        entry.bind("<FocusOut>", lambda event, e=entry: self.restaurar_placeholder(e, placeholder))
        entry.pack(pady=5)
        return entry

    def limpiar_placeholder(self, entry, placeholder):
        """Limpia el placeholder al enfocar el campo."""
        if entry.get() == placeholder:
            entry.delete(0, tk.END)

    def restaurar_placeholder(self, entry, placeholder):
        """Restaura el placeholder si el campo está vacío."""
        if not entry.get():
            entry.insert(0, placeholder)

    def registrar_usuario(self):
        """Registra al usuario en la base de datos."""
        usuario = self.entry_usuario.get()
        contrasena = self.entry_contrasena.get()
        repetir_contrasena = self.entry_repetir_contrasena.get()
        email = self.entry_email.get()
        telefono = self.entry_telefono.get()

        if contrasena != repetir_contrasena:
            messagebox.showerror("Error", "Las contraseñas no coinciden.")
            return

        if self.bd.registrar_usuario(usuario, contrasena, email, telefono):
            messagebox.showinfo("Éxito", "Usuario registrado correctamente.")
            self.volver()
        else:
            messagebox.showerror("Error", "El usuario ya existe o hubo un error al registrar.")

    def volver(self):
        """Cierra la ventana de registro."""
        self.ventana.destroy()

# Ejecutar la pantalla de registro
if __name__ == "__main__":
    RegistroUsuario()
