import tkinter as tk
from tkinter import messagebox
import sqlite3
import subprocess
from recuperarContrasenia import RecuperarContrasena  # Asegúrate de que este archivo esté en el mismo directorio

# Función para verificar las credenciales del usuario usando email y contraseña
def verificar_acceso():
    email = entry_email.get()
    contrasena = entry_contrasena.get()

    try:
        # Conectar a la base de datos
        conexion = sqlite3.connect('accesoFacturadb.db')
        cursor = conexion.cursor()

        # Consulta para validar las credenciales
        cursor.execute("SELECT * FROM usuarios WHERE email = ? AND contrasenia = ?", (email, contrasena))
        datos_usuario = cursor.fetchone()

        conexion.close()

        if datos_usuario:
            messagebox.showinfo("Acceso concedido", f"Bienvenido {email}")
            ventana.destroy()  # Cerrar la ventana de login
            abrir_registro()
        else:
            messagebox.showerror("Acceso denegado", "Email o contraseña incorrectos.")
    except sqlite3.Error as e:
        messagebox.showerror("Error", f"Error en la base de datos: {e}")

# Función para abrir la pantalla de registro
def abrir_registro():
    try:
        subprocess.run(['python', 'registro.py'])
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo abrir la pantalla de registro: {e}")

# Función para abrir la pantalla de recuperación de contraseña
def abrir_recuperar_contrasena():
    ventana.destroy()  # Cierra la ventana actual
    RecuperarContrasena()  # Llama a la clase de recuperación de contraseña

# Crear la ventana de login
ventana = tk.Tk()
ventana.title("Acceso - Facturación")
ventana.geometry("400x300")
ventana.config(bg="white")

# Título de la pantalla
titulo = tk.Label(ventana, text="Facturación", font=("Arial", 24, "bold"), bg="white")
titulo.pack(pady=10)

subtitulo = tk.Label(ventana, text="Acceso", font=("Arial", 16), bg="white")
subtitulo.pack()

# Campos de entrada para email y contraseña
entry_email = tk.Entry(ventana, font=("Arial", 14), justify="center", relief="solid", bd=1)
entry_email.insert(0, "email")
entry_email.pack(pady=10)

entry_contrasena = tk.Entry(ventana, font=("Arial", 14), justify="center", relief="solid", bd=1, show="*")
entry_contrasena.insert(0, "contraseña")
entry_contrasena.pack(pady=10)

# Botón de acceso
boton_acceso = tk.Button(ventana, text="Ingresar", font=("Arial", 12), bg="#00A2E8", fg="white", command=verificar_acceso)
boton_acceso.pack(pady=20)

# Botón de "Olvidó contraseña"
boton_olvido = tk.Button(ventana, text="¿Olvidó contraseña?", font=("Arial", 10), bg="white", fg="blue", relief="flat", command=abrir_recuperar_contrasena)
boton_olvido.pack()

# Ejecutar la ventana de login
ventana.mainloop()
