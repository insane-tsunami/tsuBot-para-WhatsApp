import os
from whatsapp import WhatsApp

whatsapp = WhatsApp(100, session="mysession")
print(whatsapp.send_message("Fabio 'tsuNami' Suenaga",":heart: Deu certo!"))
