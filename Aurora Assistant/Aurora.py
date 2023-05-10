import speech_recognition as sr
import pyttsx3
import os
import subprocess
import pyautogui
import transliterate
import time
import webbrowser

#developer - 3verlaster thank you for using this assistant!
#https://github.com/3verlaster


username = os.environ.get('USERNAME')

pyautogui.FAILSAFE = False

#pyttsx3 settings
engine = pyttsx3.init()
engine.setProperty('rate', 130)
engine.setProperty('voice', 'en')

desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Аврора запущена!")
    while True:
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language='ru-RU')
            print("Вы сказали: " + text)
            if "привет аврора" in text.lower():
                file_name = os.path.join(desktop_path, "hello.txt")
                with open(file_name, 'w') as file:
                    file.write("Привет, мир!")
                    #print("Файл создан на рабочем столе.")
                engine.say("Hello mother fucker")
                engine.runAndWait()

            elif "аврора" in text.lower():
                engine.say("At your service, sir")
                engine.runAndWait()

            elif "открой спотифай" in text.lower() or "открой spotify" in text.lower():
                spotify_path = f"C:\\Users\\{username}\\AppData\\Roaming\\Spotify\\Spotify.exe"
                if os.path.isfile(spotify_path):
                    engine.say("Opening Spotify...")
                    engine.runAndWait()
                    subprocess.Popen([spotify_path])
                else:
                    engine.say("Cannot find Spotify")
                    engine.runAndWait()

            elif "закрой спотифай" in text.lower() or "закрой spotify" in text.lower():
                try:
                    engine.say("Closing spotify...")
                    engine.runAndWait()
                    os.system(f"taskkill /f /im Spotify.exe")
                except Exception as e:
                    print(e)
                    pass

            elif "открой telegram" in text.lower():
                telegram_path = f"C:\\Users\\{username}\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe"
                if os.path.isfile(telegram_path):
                    engine.say("Opening Telegram...")
                    engine.runAndWait()
                    subprocess.Popen([telegram_path])
                else:
                    engine.say("Cannot find Telegram")
                    engine.runAndWait()

            elif "закрой telegram" in text.lower():
                try:
                    engine.say("Closing telegram...")
                    engine.runAndWait()
                    os.system(f"taskkill /f /im Telegram.exe")
                except Exception as e:
                    print(e)
                    pass

            elif "поставь звук" in text.lower():
                try:
                    volume_percent = int(text.lower().split('поставь звук', 1)[1])
                    volume = 65535 * volume_percent / 100
                    print(f"Ставлю звук: {volume_percent} а тоесть {volume} для nircmd.exe")
                    os.system(f"nircmd.exe setsysvolume {volume}")
                except Exception as e:
                    print(e)
                    pass



            elif "очисти консоль" in text.lower() or "очистить консоль" in text.lower():
                os.system("cls")

            elif "напиши" in text.lower():
                try:
                    russian_word = text.lower().split('напиши', 1)[1]
                    english_word = transliterate.translit(russian_word, 'ru', reversed=True)
                    print(f"Текст для ввода: {english_word}")
                    pyautogui.write(english_word, interval=0.1)
                except Exception as e:
                    print(e)
                    pass

            elif "нажми enter" in text.lower():
                try:
                    pyautogui.press('enter')
                except Exception as e:
                    print(e)
                    pass

            elif "сотри всё" in text.lower():
                try:
                    pyautogui.hotkey('ctrl', 'a')
                    time.sleep(0.3)
                    pyautogui.press('backspace')
                except Exception as e:
                    print(e)
                    pass

            elif "открой youtube" in text.lower():
                try:
                    engine.say("Opening youtube...")
                    engine.runAndWait()
                    webbrowser.open_new("https://youtube.com")
                except Exception as e:
                    print(e)
                    pass

            elif "открой нейросеть" in text.lower():
                try:
                    engine.say("Opening Chat G P T...")
                    engine.runAndWait()
                    webbrowser.open_new("https://chat.openai.com/?model=text-davinci-002-render-sha")
                except Exception as e:
                    print(e)
                    pass

            elif "открой гитхаб" in text.lower():
                try:
                    engine.say("Opening github...")
                    engine.runAndWait()
                    webbrowser.open_new("https://github.com/3verlaster")
                except Exception as e:
                    print(e)
                    pass

            elif "поменяй окно" in text.lower() or "поменять окно" in text.lower():
                try:
                    engine.say("Changing window...")
                    engine.runAndWait()
                    delay = 0.4  # задержка в 0.4 секунды

                    pyautogui.keyDown('alt')
                    time.sleep(delay)
                    pyautogui.press('tab')
                    time.sleep(delay)

                    pyautogui.keyUp('alt')
                    pyautogui.keyDown('tab')
                    time.sleep(delay)

                    pyautogui.keyUp('tab')
                except Exception as e:
                    print(e)
                    pass

            elif "отправь скриншот" in text.lower():
                try:
                    pyautogui.press('printscreen')
                    time.sleep(0.2)
                    pyautogui.hotkey('ctrl', 'v')
                    time.sleep(0.5)
                    pyautogui.press("enter")
                except Exception as e:
                    print(e)
                    pass

            elif "кто твой создатель" in text.lower():
                engine.say("My developer is Everlaster")
                webbrowser.open_new("https://github.com/3verlaster")
                time.sleep(0.7)
                webbrowser.open_new("https://t.me/everlaster_official")
                engine.runAndWait()

            elif "как тебя зовут" in text.lower():
                engine.say("My name is aurora")
                engine.runAndWait()

            elif "закрой вкладку" in text.lower():
                try:
                    engine.say("Closing tab...")
                    engine.runAndWait()
                    pyautogui.hotkey('ctrl', 'w')
                except Exception as e:
                    print(e)
                    pass

            elif "закрой окно" in text.lower():
                try:
                    pyautogui.hotkey('alt', 'f4')
                except Exception as e:
                    print(e)
                    pass

            elif "поменяй язык" in text.lower() or "поменять язык" in text.lower():
                try:
                    engine.say("Changing language...")
                    engine.runAndWait()
                    pyautogui.hotkey('shift', 'alt')
                except Exception as e:
                    print(e)
                    pass






        except sr.UnknownValueError:
            print("Речь не распознана (Либо вы ничего не сказали.)")
        except sr.RequestError as e:
            print("Ошибка сервиса распознавания речи; {0}".format(e))
