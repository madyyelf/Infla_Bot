# -*- coding: utf-8 -*-

import commands
import telebot    # Librería de la API del bot.
# from telebot import types    # Tipos para la API del bot.
# Librería para hacer que el programa que controla el bot no se acabe.
# Nuestro tokken del bot (el que @BotFather nos dió).
import socket
import os
TOKEN = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

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
    bot.send_message(cid, 'Bon dia! Som repúbliuca però tots els polítics han marxat!!!')


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


@bot.message_handler(commands=['estat_serveis'])
def command_estat_serveis(message):
    cid = message.chat.id
    # Caldria parametritzar des de arxiu els serveis.
    servidors = []
    servidors.append({"IP": "10.50.0.1", "NOM": "Karonte", "Ports": [22]})
    servidors.append({"IP": "10.51.0.100", "NOM": "KVM Intern", "Ports": [22]})
    servidors.append({"IP": "10.52.0.101", "NOM": "KVM DMZ", "Ports": [22]})
    servidors.append({"IP": "10.51.0.202", "NOM": "Robust", "Ports": [22, 80]})
    servidors.append({"IP": "10.52.200.1", "NOM": "Maersk", "Ports": [666]})
    servidors.append({"IP": "10.52.0.115", "NOM": "Moodle Cardona", "Ports": [22, 80, 443]})
    servidors.append({"IP": "10.51.0.4", "NOM": "DNS", "Ports": [22, 53]})
    servidors.append({"IP": "10.53.0.6", "NOM": "(KVM) Punts d'accés", "Ports": [22, 80, 443]})
    servidors.append({"IP": "10.52.0.116", "NOM": "MoodleSMIX", "Ports": [22, 80, 443]})
    servidors.append({"IP": "10.52.200.150", "NOM": "LXC Moodle", "Ports": [22, 80, 443]})
    servidors.append({"IP": "10.52.200.210", "NOM": "LXC Web", "Ports": [22, 80, 443]})

    # escanner = nmap.PortScanner()
    result = []

    for equip in servidors:
        # bot.send_message(cid,"Escanejant "+equip['IP']+" ...")
        # escanner.scan(equip['IP'], ''.join(equip['Ports']))
        # bot.send_message(cid, equip['IP']+' '+escanner[equip['IP']].state())
        if os.system("ping -c 1 "+equip['IP']) == 0:
            result.append("\n\nHost "+equip['IP']+" ("+equip['NOM']+") up.")
            for port in equip['Ports']:
                # print port
                # bot.send_message(cid, "Port "+port+": "+str(escanner[equip['IP']]['tcp']))
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(10)
                try:
                    s.connect((equip['IP'], port))
                    result.append("\nPort "+str(port)+" obert.")
                except socket.error:
                    result.append("\n[!] Port "+str(port)+" ERROR!")
                s.close()
        else:
            result.append("\n\n[!] Host "+equip['IP']+" ("+equip['NOM']+") DOWN!")
    bot.send_message(cid, ''.join(result))


@bot.message_handler(commands=['internet'])
def command_internet(message):
    cid = message.chat.id
    parametres = message.text.split()
    # Estaria be parametritzar les aules de manera que des de arxiu llegeixi.

    if len(parametres) == 2 and parametres[1] == "estat":
        bot.send_message(cid, "estat")
    elif len(parametres) == 3 and parametres[1] == "a33":
        if parametres[2] == "on":
            bot.send_message(cid, "donar internet A33")
            os.system("iptables -D FORWARD -i eth33 -o eth0 -j DROP")
        elif parametres[2] == "off":
            bot.send_message(cid, "treure internet A33")
            os.system("iptables -I FORWARD 1 -i eth33 -o eth0 -j DROP")
        else:
            bot.send_message(cid, "ajuda")
    elif len(parametres) == 3 and parametres[1] == "a34":
        if parametres[2] == "on":
            bot.send_message(cid, "donar internet A34")
        elif parametres[2] == "off":
            bot.send_message(cid, "treure internet A34")
        else:
            bot.send_message(cid, "ajuda")

    else:
        bot.send_message(cid, "ajuda")


#############################################
# Peticiones
bot.polling(none_stop=True)   # Con esto, le decimos al bot que siga
# funcionando incluso si encuentra algún fallo.
