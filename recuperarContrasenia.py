import tkinter as tk
from tkinter import messagebox
import sqlite3
from emailRecuperacion import EmailSender  # Importar la clase para enviar correos

class RecuperarContrasena:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Recuperar Contraseña")
        self.ventana.geometry("400x300")
        self.ventana.config(bg="white")

        # Título de la pantalla
        titulo = tk.Label(self.ventana, text="Recuperar Contraseña", font=("Arial", 24, "bold"), bg="white")
        titulo.pack(pady=10)

        # Campo de entrada para email
        self.entry_email = tk.Entry(self.ventana, font=("Arial", 14), justify="center", relief="solid", bd=1)
        self.entry_email.insert(0, "Ingrese su email")
        self.entry_email.pack(pady=20)

        # Botón de enviar
        boton_enviar = tk.Button(self.ventana, text="Enviar", font=("Arial", 12), bg="#00A2E8", fg="white", command=self.enviar_correo)
        boton_enviar.pack(pady=10)

        # Botón de regresar
        boton_regresar = tk.Button(self.ventana, text="Regresar", font=("Arial", 10), bg="white", fg="blue", relief="flat", command=self.volver)
        boton_regresar.pack(pady=5)

        self.email_sender = EmailSender()  # Crear instancia de EmailSender

        self.ventana.mainloop()

    def enviar_correo(self):
        email = self.entry_email.get()

        if self.verificar_email(email):
            contrasenia = self.obtener_contrasenia(email)
            if contrasenia:
                self.email_sender.enviar_email(email, contrasenia)  # Enviar el correo
                messagebox.showinfo("Éxito", "La contraseña ha sido enviada a su correo.")
            else:
                messagebox.showerror("Error", "No se pudo obtener la contraseña.")
        else:
            messagebox.showerror("Error", "El correo no está registrado.")

    def verificar_email(self, email):
        """Verifica si el email está en la base de datos."""
        try:
            conexion = sqlite3.connect('accesoFacturadb.db')
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM usuarios WHERE email = ?", (email,))
            existe = cursor.fetchone() is not None
            conexion.close()
            return existe
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Error en la base de datos: {e}")
            return False

    def obtener_contrasenia(self, email):
        """Obtiene la contraseña del usuario desde la base de datos."""
        try:
            conexion = sqlite3.connect('accesoFacturadb.db')
            cursor = conexion.cursor()
            cursor.execute("SELECT contrasenia FROM usuarios WHERE email = ?", (email,))
            contrasenia = cursor.fetchone()
            conexion.close()
            return contrasenia[0] if contrasenia else None
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Error en la base de datos: {e}")
            return None

    def volver(self):
        """Cierra la ventana de recuperar contraseña."""
        self.ventana.destroy()

# Ejecutar la pantalla de recuperación de contraseña
if __name__ == "__main__":
    RecuperarContrasena()
