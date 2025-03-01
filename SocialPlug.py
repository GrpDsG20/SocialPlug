import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from colorama import Fore, init
import git
import sys
import shutil
import tempfile
import threading

init(autoreset=True)

REPO_URL = 'https://github.com/GrpDsG20/SocialPlug'

def actualizar_repositorio():
    repo_path = tempfile.mkdtemp()

    try:
        if not os.path.exists(repo_path):
            repo = git.Repo.clone_from(REPO_URL, repo_path)
        else:
            repo = git.Repo(repo_path)
            origin = repo.remotes.origin
            origin.fetch()
            if repo.is_dirty():
                origin.pull()
    except Exception as e:
        print(Fore.RED + f"Error al intentar actualizar el repositorio: {e}")

def ingresar_datos():
    username = input("Ingresa tu nombre de usuario: ")
    email = input("Ingresa tu correo electrónico: ")
    return username, email

def bienvenida():
    print(Fore.GREEN + """
                _       _       _              
               (_)     | |     | |            
 ___  ___   ___ _  __ _| |_ __ | |_   _  __ _ 
/ __|/ _ \ / __| |/ _` | | '_ \| | | | |/ _` |
\__ \ (_) | (__| | (_| | | |_) | | |_| | (_| |
|___/\___/ \___|_|\__,_|_| .__/|_|\__,_|\__, |
                         | |             __/ |
                         |_|            |___/ 
Herramienta creada por @SMITE""")

def seleccionar_plataforma():
    print(Fore.YELLOW + "Selecciona una plataforma:")
    print(Fore.CYAN + "1. Instagram")
    print(Fore.CYAN + "2. TikTok")
    print(Fore.CYAN + "3. Twitch")
    print(Fore.CYAN + "4. YouTube")
    print(Fore.CYAN + "5. Twitter")
    seleccion = input("Ingresa el número correspondiente: ")
    return seleccion

def procesando_animation():
    for i in range(5):
        print(Fore.YELLOW + "Procesando" + "." * (i % 3 + 1), end="\r")
        time.sleep(0.5)

def abrir_plataforma(plataforma, username, email):
    if plataforma == '1':
        url = "https://www.socialplug.io/es/servicios-gratuitos/seguidores-instagram-gratis"
        username_selector = 'socialHandle'
        email_selector = 'email'
    elif plataforma == '2':
        url = "https://www.socialplug.io/es/servicios-gratuitos/seguidores-tiktok-gratis"
        username_selector = 'socialHandle'
        email_selector = 'email'
    elif plataforma == '3':
        url = "https://www.socialplug.io/es/servicios-gratuitos/free-twitch-followers"
        username_selector = 'socialHandle'
        email_selector = 'email'
    elif plataforma == '4':
        url = "https://www.socialplug.io/es/servicios-gratuitos/suscriptores-youtube-gratis"
        username_selector = 'socialHandle'
        email_selector = 'email'
    elif plataforma == '5':
        url = "https://www.socialplug.io/es/servicios-gratuitos/seguidores-twitter-gratis"
        username_selector = 'socialHandle'
        email_selector = 'email'
    else:
        print(Fore.RED + "Selección no válida.")
        return

    chrome_options = Options()
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.get(url)

    procesando_animation()

    try:
        username_input = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.NAME, username_selector))
        )
        email_input = driver.find_element(By.NAME, email_selector)

        username_input.send_keys(username)
        email_input.send_keys(email)
        email_input.send_keys(Keys.RETURN)

        procesando_animation()

        time.sleep(5)

        try:
            error_message = WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located((By.CLASS_NAME, 'form-message'))
            )

            if "El servicio gratuito ya ha sido solicitado" in error_message.text:
                print(Fore.RED + "¡Error! El servicio ha sido utilizado recientemente. Recuerda que puedes intentar nuevamente después de 24 horas.")
                return
            else:
                print(Fore.GREEN + "Los seguidores están en camino. Revisa tu correo en la sección de promociones, notificaciones o spam. Confirma el correo y disfruta de los seguidores.")
                respuesta = input("¿Quieres volver a usar el servicio después de 24h? (s/n): ")
                if respuesta.lower() == 's':
                    print(Fore.YELLOW + "Servicio listo para ser utilizado nuevamente en 24 horas.")
                else:
                    print(Fore.YELLOW + "Gracias por utilizar el servicio.")
                return

        except Exception as e:
            print(Fore.RED + "¡Error! El servicio ha sido utilizado recientemente. Recuerda que puedes intentar nuevamente después de 24 horas.")
            return

    except Exception as e:
        print(Fore.RED + f"Se produjo un error en la verificación del formulario: {e}")

    print(Fore.YELLOW + "El navegador se ha dejado abierto para que puedas ver el proceso.")
    
    driver.quit()

def main():
    bienvenida()
    actualizar_repositorio()

    plataforma = seleccionar_plataforma()

    username, email = ingresar_datos()

    abrir_plataforma(plataforma, username, email)

    print(Fore.GREEN + "El proceso ha finalizado. Cerrando el script.")

if __name__ == "__main__":
    main()
