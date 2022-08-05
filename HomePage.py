from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class HomePage:
    close_cookie_button_selector = (By.ID, "onetrust-accept-btn-handler")
    hamburger_selector = "#data-rayons"
    epicerie_salee_selector = (By.CSS_SELECTOR, ".nav-item__menu-link [alt='Epicerie salée']")


    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.action = ActionChains(self.driver)

    #closeCookie
    def close_cookie(self):
        close_cookie_button = self.wait.until(expected_conditions.element_to_be_clickable(self.close_cookie_button_selector)).click()
        self.wait.until(expected_conditions.invisibility_of_element_located(self.close_cookie_button_selector))

    #menuBurger
    def open_menu(self):
        open_menu_hamburger = self.driver.find_element(By.CSS_SELECTOR, self.hamburger_selector).click()


    #categorieEpicerieSalee
    def open_epicerie_salee(self):
        epicerie_salee = self.wait.until(expected_conditions.element_to_be_clickable(self.epicerie_salee_selector))
        self.action.move_to_element(epicerie_salee)
        self.action.perform()

    #sousCategorie
    def open_sub_category_menu(self):
        feculent = self.wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "#data-menu-level-1_R12 > li:nth-child(7)")))
        self.action.move_to_element(feculent)
        self.action.perform()

    #open_product_categorie
    def open_product_category_page(self):
        categorie_pates = self.driver.find_element(By.CSS_SELECTOR, "#data-menu-level-2_R12F05 > li:nth-child(3)")
        categorie_pates.click()
