import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from tkinter import messagebox

class EmailSender:
    def __init__(self):
        self.remitente = "222h17117@alumno.ujat.mx"  # correo
        self.contraseña = "Asmd@090904"  # contraseña

    def enviar_email(self, email, contrasenia):
        """Envía un correo con la contraseña al usuario."""
        try:
            msg = MIMEMultipart()
            msg['From'] = self.remitente
            msg['To'] = email
            msg['Subject'] = "Recuperación de Contraseña"

            cuerpo = f"Su contraseña es: {contrasenia}"
            msg.attach(MIMEText(cuerpo, 'plain'))

            with smtplib.SMTP('smtp-mail.outlook.com', 587) as servidor: 
                servidor.starttls()
                servidor.login(self.remitente, self.contraseña)
                servidor.send_message(msg)

        except Exception as e:
            messagebox.showerror("Error", f"No se pudo enviar el correo: {e}")
