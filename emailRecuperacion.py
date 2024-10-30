import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from tkinter import messagebox

class EmailSender:
    def __init__(self):
        self.remitente = "asmdbedtgmail.com"  # Cambia esto a tu correo
        self.contraseña = "ASDAA0905"  # Cambia esto a tu contraseña

    def enviar_email(self, email, contrasenia):
        """Envía un correo con la contraseña al usuario."""
        try:
            msg = MIMEMultipart()
            msg['From'] = self.remitente
            msg['To'] = email
            msg['Subject'] = "Recuperación de Contraseña"

            cuerpo = f"Su contraseña es: {contrasenia}"
            msg.attach(MIMEText(cuerpo, 'plain'))

            with smtplib.SMTP('smtp.gmail.com', 587) as servidor:  # Cambia smtp.example.com a tu servidor SMTP
                servidor.starttls()
                servidor.login(self.remitente, self.contraseña)
                servidor.send_message(msg)

        except Exception as e:
            messagebox.showerror("Error", f"No se pudo enviar el correo: {e}")
