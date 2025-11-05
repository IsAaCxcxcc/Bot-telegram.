import telebot
import requests
import time

# 🔑 Coloque aqui o token do seu bot (pego com o @BotFather)
TOKEN = "8570596255:AAFrY-IP5JxGc6AeljlJpatHaMFCtjbyYbw"

bot = telebot.TeleBot(TOKEN)

# Dicionário pra armazenar os pontos dos usuários
pontos = {}

@bot.message_handler(commands=['start'])
def start(msg):
    user_id = msg.from_user.id
    bot.reply_to(msg, "👋 Olá! Seja bem-vindo ao bot de anúncios!\n\n"
                      "Use /assistir pra ganhar pontos 💰\n"
                      "Use /saldo pra ver quantos pontos você tem.")
    if user_id not in pontos:
        pontos[user_id] = 0

@bot.message_handler(commands=['assistir'])
def assistir(msg):
    user_id = msg.from_user.id
    # 🔹 Aqui futuramente você colocará o link de anúncio do MyLead
    anuncio_link = "https://mylead.global/"
    bot.send_message(msg.chat.id, f"📺 Assista este anúncio: {anuncio_link}")
    bot.send_message(msg.chat.id, "⏳ Aguarde 10 segundos para receber seus pontos...")

    # Simula tempo de visualização
    time.sleep(10)

    # Adiciona pontos
    pontos[user_id] = pontos.get(user_id, 0) + 10
    bot.send_message(msg.chat.id, f"✅ Você ganhou 10 pontos!\nUse /saldo pra ver seu total.")

@bot.message_handler(commands=['saldo'])
def saldo(msg):
    user_id = msg.from_user.id
    total = pontos.get(user_id, 0)
    bot.send_message(msg.chat.id, f"💰 Seu saldo atual é: {total} pontos.\n"
                                  "100 pontos = R$ 1,00 💵")

@bot.message_handler(commands=['ajuda'])
def ajuda(msg):
    bot.reply_to(msg, "📘 Comandos disponíveis:\n"
                      "/start - Iniciar o bot\n"
                      "/assistir - Assistir anúncio e ganhar pontos\n"
                      "/saldo
