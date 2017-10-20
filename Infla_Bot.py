# -*- coding: utf-8 -*-

import commands
import telebot    # Librería de la API del bot.
# from telebot import types    # Tipos para la API del bot.
# Librería para hacer que el programa que controla el bot no se acabe.
# Nuestro tokken del bot (el que @BotFather nos dió).
TOKEN = '361167179:AAEhx-9EFDgCHWTmc798-RN4oa4HL6I6G90'

bot = telebot.TeleBot(TOKEN)   # Creamos el objeto de nuestro bot.

#############################################
# Listener
# Con esto, estamos definiendo una función llamada 'listener',
# que recibe como parámetro un dato llamado 'messages'.


def listener(messages):
    for m in messages:   # Por cada dato 'm' en el dato 'messages'
        # Filtramos mensajes que sean tipo texto.
        if m.content_type == 'text':
            cid = m.chat.id   # Almacenaremos el ID de la conversación.
            # Y haremos que imprima algo parecido a esto -> [52033876]: /start
            print "[" + str(cid) + "]: " + m.text

# Así, le decimos al bot que utilice como función escuchadora nuestra
# función 'listener' declarada arriba.
bot.set_update_listener(listener)
#############################################
# Funciones
# Indicamos que lo siguiente va a controlar el comando '/roto2'.


# Indicamos que lo siguiente va a controlar el comando '/miramacho'
@bot.message_handler(commands=['hola'])
def command_hola(m):   # Definimos una función que resuleva lo que necesitemos.
    # Guardamos el ID de la conversación para poder responder.
    cid = m.chat.id
    # bot.send_message( cid, 'Hola! Som els manairons')   # Con la función
    # 'send_message()' del bot, enviamos al ID almacenado el texto que queremos
    bot.send_message(cid, 'Bon dia! Ja som república independent?')


@bot.message_handler(commands=['test_velocitat'])
def command_test_velocidad(m):
    cid = m.chat.id
    test = commands.getstatusoutput('speedtest-cli')
    if test[0] == 0:
        bot.send_message(cid, test[1])
    else:
        bot.send_message(cid, "[!] Error llançant Speedtest-cli.")


@bot.message_handler(commands=['traceroute'])
def command_traceroute(message):
    cid = message.chat.id
    comanda = message.text.replace("/", "")
    test = commands.getstatusoutput(comanda)
    if test[0] == 0:
        bot.send_message(cid, test[1])
    else:
        bot.send_message(cid, "[!] Error llançant Traceroute.")


@bot.message_handler(commands=['ping'])
def command_ping(message):
    cid = message.chat.id
    comanda = message.text.replace("/", "")
    comanda = comanda+" -c 5"
    test = commands.getstatusoutput(comanda)
    if test[0] == 0:
        bot.send_message(cid, test[1])
    else:
        bot.send_message(cid, "[!] Error llançant el Ping.")

#############################################
# Peticiones
bot.polling(none_stop=True)   # Con esto, le decimos al bot que siga
# funcionando incluso si encuentra algún fallo.
