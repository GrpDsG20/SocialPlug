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
import tempfile

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
    except Exception:
        pass  # Silenced error handling

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
    elif plataforma == '2':
        url = "https://www.socialplug.io/es/servicios-gratuitos/seguidores-tiktok-gratis"
    elif plataforma == '3':
        url = "https://www.socialplug.io/es/servicios-gratuitos/free-twitch-followers"
    elif plataforma == '4':
        url = "https://www.socialplug.io/es/servicios-gratuitos/suscriptores-youtube-gratis"
    elif plataforma == '5':
        url = "https://www.socialplug.io/es/servicios-gratuitos/seguidores-twitter-gratis"
    else:
        print(Fore.RED + "Selección no válida.")
        return

    # Configure Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--headless")  # Run in headless mode (without GUI)
    chrome_options.add_argument("--disable-logging")  # Disable Chrome logs
    chrome_options.add_argument("--log-level=3")  # Set the log level to only errors (no warnings or info)
    
    # Set up Chrome logging preferences to suppress warnings
    prefs = {
        'profile.managed_default_content_settings.images': 2,  # Disable images
        'profile.managed_default_content_settings.javascript': 2  # Disable JavaScript
    }
    chrome_options.add_experimental_option('prefs', prefs)

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.get(url)

    procesando_animation()

    try:
        username_input = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.NAME, 'socialHandle'))
        )
        email_input = driver.find_element(By.NAME, 'email')

        username_input.send_keys(username)
        email_input.send_keys(email)
        email_input.send_keys(Keys.RETURN)

        procesando_animation()

        time.sleep(5)

        # Only processing, suppress error messages
        print(Fore.YELLOW + "Procesando...")

    except Exception:
        pass  # Silent exception handling

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
1