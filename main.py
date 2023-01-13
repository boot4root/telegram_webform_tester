import telebot
import webbrowser
import random
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from telebot import types

from seleniumwire import webdriver
from time import sleep
from random import choice
 
#browser = webdriver.Firefox() # Get local session of firefox
#browser.get("http://www.yandex.ru") # Load page
#assert "yandex".decode("utf-8") in browser.title
#elem = browser.find_element_by_name("text") # Find the query box
#elem.send_keys("http://программисту.рф/".decode("utf-8") + Keys.RETURN)
#time.sleep(0.2) # Let the page load, will be added to the API



bot = telebot.TeleBot('5921843743:AAGLfnfrEKs9yopmQ1y9y40YO1hvs_voLGI')

site_url = 'https://грузоперевозки-в-чите.рф/'
form_list = ['form1', 'form2']
name_list = ['John', 'Mary', 'Jane']
phone_list = ['123-456-7890', '234-567-8901', '345-678-9012']


def open_site(site):
    webbrowser.open(site)
    return

def fill_form(form, name, phone):
# code to fill out form with the provided name and phone 
    return

def submit_application():
# code to submit the application
    return



@bot.message_handler(commands=['start'])

def send_welcome(message):
    
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton("1")
    btn1 = types.KeyboardButton("2")
    settingsButton = types.KeyboardButton("Настройки")
    markup.add(btn, btn1, settingsButton)
    bot.send_message(message.from_user.id, "Добро пожаловать с тестировщика форм", reply_markup=markup)

def select_form(message):
    selection = int(message.text)
    selected_form = form_list[selection-1]
    bot.send_message(message.chat.id, 'Form selected: ' + selected_form)
    counter = 0
    max_repeats = 3
    interval = 300 # seconds (5 minutes)

    while counter < max_repeats:
        random_name = random.choice(name_list)
        random_phone = random.choice(phone_list)
            
        driver = webdriver.Chrome(executable_path='chromedriver.exe')
        driver.get(site_url)
        element = driver.find_element_by_tag_name('input')
        element.click()
        element.send_keys(choice(phones))
        markup.add(btn1)
        btn = driver.find_element_by_css_selector('.btn btn-block btn-danger')
        btn.click()
        sleep(1) 

        bot.send_message(message.chat.id, 'Имя: ' + random_name + 'Телефон: ' + random_phone)
        fill_form(selected_form, random_name, random_phone)
        submit_application()
        bot.send_message(message.chat.id, 'Форма отправлена.')
        counter += 1
        time.sleep(interval)


@bot.message_handler(commands=["start"])
def send_welcome(message):
    global DELETEuserName1
    bot.clear_step_handler(message)
    userName = bot.send_message(message.chat.id, "Здравствуйте, введите имя")
    DELETEuserName1 = userName.message_id
    bot.register_next_step_handler(userName, userSurNameFUNC)


def userSurNameFUNC(message):
    global userName, DELETEuserSurName, DELETEuserSurName1
    userName = message.text
    markup = types.InlineKeyboardMarkup()
    resetDataKey = types.InlineKeyboardButton("Сбросить", callback_data="resetData")
    markup.add(resetDataKey)
    userSurName = bot.send_message(message.chat.id, "Теперь введите фамилию", reply_markup=markup)
    DELETEuserSurName = userSurName.chat.id
    DELETEuserSurName1 = userSurName.message_id
    bot.delete_message(message.chat.id, message.message_id)
    bot.delete_message(message.chat.id, DELETEuserName1)
    bot.register_next_step_handler(userSurName, endProgrammFUNC)


def endProgrammFUNC(message):
    global userSurName, DELETEendProgramm, DELETEendProgramm1
    userSurName = message.text
    endProgramm = bot.send_message(message.chat.id, "Вас зовут " + userName + " " + userSurName)
    DELETEendProgramm = endProgramm.chat.id
    DELETEendProgramm1 = endProgramm.message_id
    bot.delete_message(message.chat.id, message.message_id)
    bot.delete_message(DELETEuserSurName, DELETEuserSurName1)


@bot.callback_query_handler(func=lambda call: True)
def inline_handler(call):
    if call.data == "resetData":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        send_welcome(call.message)



@bot.message_handler(content_types=["text"])
def start(message):
    if  message.text == 'Старт тестировки форм':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        templat1 = types.KeyboardButton("1")
        templat2 = types.KeyboardButton('2')
        markup.add(templat1, templat1)
        bot.send_message(message.from_user.id, "Выберите пожалуста шаблон формы", reply_markup=markup)

    for i, Template in enumerate(form_list):
        bot.send_message(message.chat.id, str(i+1) + '. ' + Template)
        bot.register_next_step_handler(message, select_form)


    if  message.text == 'Настройки':
        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="Старт", callback_data="test")
        keyboard.add(callback_button)
        open_site(site_url)
        bot.send_message(message.chat.id, 'Выберите настройки для тестировки формы у : ' + site_url)
        bot.send_message(message.chat.id, 'Выберите настройки для тестировки формы у : ' + site_url)



if __name__ == '__main__':
    bot.infinity_polling()



bot.polling(none_stop=True)
