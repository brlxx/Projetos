from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc

import flet as ft
import time as t



def iniciar():
    driver = uc.Chrome()
    driver.set_window_size(900,800)
    try:
            t.sleep(0.3)
            driver.get("https://firemail.com.br/")
            teclas = ActionChains(driver) #teclas
            driver.find_element(By.XPATH,'//*[@id="btn-gerar-aleatorio"]').click()
            t.sleep(0.4)

            email_entra = driver.find_element(By.XPATH,'//*[@id="form-email"]/div[2]/input')

            teclas.click(email_entra).key_down(Keys.CONTROL).send_keys('a').send_keys('c').key_up(Keys.CONTROL).perform()
            t.sleep(0.4)
            btn = driver.find_element(By.XPATH,'//*[@id="btn-criar-email"]')

            btn.click()

            t.sleep(0.4)
                

                # Abre uma nova aba e navega até o Discord
            driver.execute_script("window.open('');")
            abas = driver.window_handles  # Obtém uma lista de todas as abas/janelas abertas
            t.sleep(0.4)
            driver.switch_to.window(abas[1])  # Alterna para a nova aba
            t.sleep(0.2)
            driver.get("https://discord.com/register")

            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[name="email"]')))
                # Espera até que o campo de entrada no Discord esteja visível e acessível

            eemail = driver.find_element(By.CSS_SELECTOR,'[name="email"]')
            username = driver.find_element(By.CSS_SELECTOR,'[name="global_name"]')
            usuario = driver.find_element(By.CSS_SELECTOR,'[name="username"]')
            senha = driver.find_element(By.CSS_SELECTOR,'[name="password"]')

            try:
                t.sleep(1)
                teclas.click(eemail).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
                eemail.send_keys('@firemail.com.br')
            finally:
                print('Deu ruim')
            t.sleep(0.3)
            teclas.click(username).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
            teclas.click(usuario).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
            t.sleep(0.5)
            senha.send_keys('Contas343423')
            t.sleep(0.6)
            dia = driver.find_element(By.CSS_SELECTOR, '[aria-label="Dia"]').send_keys('23')
            t.sleep(0.3)
            mes = driver.find_element(By.CSS_SELECTOR, '[aria-label="Mês"]').send_keys('11',Keys.RETURN)
            t.sleep(0.3)
            ano = driver.find_element(By.CSS_SELECTOR, '[aria-label="Ano"]').send_keys('1987')
            t.sleep(0.3)

            btns = driver.find_element(By.XPATH,'//*[@id="app-mount"]/div[2]/div[1]/div[1]/div/div/div/form/div[2]/div/div[7]/button').click()

            driver.switch_to.window(abas[0])
                
            input()
    finally:
            driver.quit()
def main(page: ft.Page):
    page.title = "Teste"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    def a(e):
        iniciar()
    t = ft.Text(value="", color="#6800C2",font_family=10)
    page.add(   
        ft.Row([t,ft.TextButton('iniciar',on_click=a,width=100,height=35)], alignment=ft.MainAxisAlignment.CENTER)
    )
ft.app(target=main)