import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions, wait
from selenium.webdriver.common.action_chains import ActionChains

from HomePage import HomePage
from ProductCategoryPage import ProductCategoryPage


def test_open_chrome():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.amazon.fr")
    barre_recherche = driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']")
    barre_recherche.send_keys("Playstation 5" + Keys.ENTER)
    driver.quit()

#excercice Carrefour CSS selector
def _open_chrome():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.carrefour.fr")
    cookie = driver.find_element(By.CSS_SELECTOR, ".banner-actions-container > button")
    cookie.click()
    time.sleep(2)
    barre_recherche = driver.find_element(By.CSS_SELECTOR, "div.pl-input-text > input")
    barre_recherche.send_keys("1664")
    rechercher = driver.find_element(By.CSS_SELECTOR,"div.pl-input-text-group__append")
    rechercher.click()
    first_result = driver.find_element(".ds-title.ds-title--medium.ds-title--s")
    first_result.click()
    acheter = driver.find_element(By.CSS_SELECTOR, "button.pl-button.pl-button--primary.add-to-cart__plus")
    acheter.click()
    driver.quit()

#exercice_xpath
#def test_open_chrome():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.carrefour.fr")
    cookie = driver.find_element(By.XPATH,"//div[@class='banner-actions-container'] /button")
    cookie.click()
    time.sleep(2)
    barre_recherche = driver.find_element(By.XPATH, "//div[@class='pl-input-text']")
    barre_recherche.send_keys("1664")
    recherche = driver.find_element(By.XPATH,"//div[@class='pl-input-text-group__append']")
    recherche.click()
    selection_element = driver.find_element("//h2[@aria-describedby='product-card-ppu-0e8a3824-3d3a-485e-ac08-d80501a4445c product-card-price-0e8a3824-3d3a-485e-ac08-d80501a4445c']")
    selection_element.click()
    acheter = driver.find_element(By.XPATH, "//button[@class='pl-button pl-button--primary add-to-cart__plus']")
    acheter.click()
    driver.quit()

#CORRECTION DE SIMON
def _css_correction():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.carrefour.fr/")
    time.sleep(2)
    close_cookies = driver.find_element(By.CSS_SELECTOR, ".banner-actions-container > button")
    close_cookies.click()
    search_bar = driver.find_element(By.CSS_SELECTOR, "input[required]")
    # possibilite utilisation [required]
    search_bar.send_keys("1664")
    search_button = driver.find_element(By.CSS_SELECTOR, "button[type=submit]")
    # possibilite utilisation [type=submit]
    search_button.click()
    first_result = driver.find_element(By.CSS_SELECTOR, ".product-grid-item:nth-child(1) .main-vertical--image")
    first_result.click()
    time.sleep(1)
    buy_button = driver.find_element(By.CSS_SELECTOR, ".pdp-button-container")
    # possibilite utilisation [aria-label='ACHETER'] : mais attention au changement de langue
    buy_button.click()
    time.sleep(2)
    retrait_en_magasin = driver.find_element(By.CSS_SELECTOR, ".push-services--pickers li:nth-child(1) label")
    delivery24 = driver.find_element(By.CSS_SELECTOR, ".push-services--pickers li:nth-child(2) label")
    delivery1 = driver.find_element(By.CSS_SELECTOR, ".push-services--pickers li:nth-child(3) label")
    assert retrait_en_magasin.text == 'Drive\nRetrait gratuit en magasin'
    assert "Drive" in retrait_en_magasin.text
    assert delivery24.text == 'Livraison\nVotre plein de course en 24h'
    assert delivery1.text == 'Livraison 1h\nVos courses d’appoint en 1h'
    driver.quit()


def _open_chrome():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.amazon.fr")
    cookie = driver.find_element(By.CSS_SELECTOR, "#sp-cc-accept")
    cookie.click()
    time.sleep(2)
    barre_recherche = driver.find_element(By.CSS_SELECTOR, "#twotabsearchtextbox")
    barre_recherche.send_keys("Livre" + Keys.ENTER)
    selection_article = driver.find_element(By.CSS_SELECTOR, "[data-asin='2832111076']")
    selection_article.click()
    ajout_panier = driver.find_element(By.CSS_SELECTOR, "[value='Ajouter au panier']")
    ajout_panier.click()
    driver.quit()

def _css_correction():
    driver = webdriver.Chrome()

    driver.maximize_window()
    driver.get("https://www.carrefour.fr/")

    wait = WebDriverWait(driver, 10)
    close_cookies_button = wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "#onetrust-accept-btn-handler")))
    close_cookies_button.click()

    search_bar = driver.find_element(By.CSS_SELECTOR, "input[required]")
    # possibilite utilisation [required]
    search_bar.send_keys("1664")
    search_button = driver.find_element(By.CSS_SELECTOR, "button[type=submit]")
    # possibilite utilisation [type=submit]
    search_button.click()
    first_result = driver.find_element(By.CSS_SELECTOR, ".product-grid-item:nth-child(1) .main-vertical--image")
    first_result.click()

    buy_button = wait.until(
        expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, ".pdp-button-container")))
    # possibilite utilisation [aria-label='ACHETER'] : mais attention au changement de langue
    buy_button.click()

    retrait_en_magasin = wait.until(
        expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, ".push-services--pickers li:nth-child(1) label")))
    delivery24 = driver.find_element(By.CSS_SELECTOR, ".push-services--pickers li:nth-child(2) label")
    delivery1 = driver.find_element(By.CSS_SELECTOR, ".push-services--pickers li:nth-child(3) label")
    assert retrait_en_magasin.text == 'Drive\nRetrait gratuit en magasin'
    assert "Drive" in retrait_en_magasin.text
    assert delivery24.text == 'Livraison\nVotre plein de course en 24h'
    assert delivery1.text == 'Livraison 1h\nVos courses d’appoint en 1h'
    driver.quit()


def _navigation_menu():
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get("https://www.carrefour.fr/")
    wait = WebDriverWait(driver,10)
    #fermer_cookies
    close_cookies_button = wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "#onetrust-accept-btn-handler")))
    close_cookies_button.click()
    #menu_burger
    hamburger_button = driver.find_element(By.CSS_SELECTOR, "#data-rayons")
    hamburger_button.click()

    epicerie_salee_menu = wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "#data-menu-level-0 > li:nth-child(12)")))
    action = ActionChains(driver)
    action.move_to_element(epicerie_salee_menu)
    action.perform()

    wait = WebDriverWait(driver, 15)
    epicerie_pates_riz_feculent = driver.find_element(By.CSS_SELECTOR, "#data-menu-level-1_R12 > li:nth-child(7)")
    action = ActionChains(driver)
    action.move_to_element(epicerie_pates_riz_feculent)
    action.perform()

    #wait = WebDriverWait(driver, 10)
    selection_pates = driver.find_element(By.CSS_SELECTOR, "ul#data-menu-level-2_R12F05 li:nth-child(3)")
    selection_pates.click()

    openProduct(driver,3)
    #acheter_produit
    acheter_produit = wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "#data-produit-acheter")))
    acheter_produit.click()

    #selectionner_drive
    selection_drive = wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, ".pl-visual-picker.service-picker.pl-visual-picker--size-m [id='1429']")))
    selection_drive.click()




def openProduct(driver,index):
    liste_produits = driver.find_elements(By.CSS_SELECTOR, ".product-grid-item:not(.storetail) h2")
    liste_produits[index].click()


#CORRECTION SIMON
def openProducts(driver, index):
    # Function to open product by element
    selector = f'.product-grid-item:not(.storetail):nth-child({index}) .product-card-image'
    product = driver.find_element(By.CSS_SELECTOR, selector)
    product.click()


def openProducts2(driver, index):
    # Function to open product by list
    if index >= 0 and index < 60:
        product_list = driver.find_elements(By.CSS_SELECTOR, ".product-grid-item:not(.storetail) .product-card-image")
        product_list[index].click()
    else:
        print("Index value is out of range. Should be between 0 and 59")


def carrefour():

    # Open browser and go to Web page
    driver = webdriver.Chrome()
    action = ActionChains(driver)
    driver.maximize_window()
    driver.get("https://www.carrefour.fr")

    # Definition of explicit wait
    wait = WebDriverWait(driver, 10)

    # Close cookies pop up
    close_cookies = wait.until(expected_conditions.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler")))
    close_cookies.click()

    # Clic on hamburger button
    hamburger_button = driver.find_element(By.CSS_SELECTOR, "#data-rayons")
    hamburger_button.click()

    # hover to epicerie salee
    epicerie_salee = wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, ".nav-item__menu-link [alt='Epicerie salée']")))
    action.move_to_element(epicerie_salee)
    action.perform()

    # hover to feculent
    feculent = wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "#data-menu-level-1_R12 > li:nth-child(7)")))
    action.move_to_element(feculent)
    action.perform()

    # clic on pate
    pates = driver.find_element(By.CSS_SELECTOR, "#data-menu-level-2_R12F05 > li:nth-child(3)")
    pates.click()

    # Call function to open product
    # openProducts(driver, 4)
    openProducts2(driver, 3)

    # Clic on buy button
    buy_button = wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "#data-produit-acheter")))
    buy_button.click()

    # Clic on Drive pick up
    pick_up = wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".push-services--pickers li:nth-child(1)")))
    pick_up.click()

    # print zip code inside text box
    zip_code = wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "[data-cs-mask=true]")))
    zip_code.send_keys("75001")
    time.sleep(1)
    zip_code.send_keys(Keys.ENTER)

    # select first store available
    first_store = wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, ".drive-service-list__list > li:nth-child(1) button")))
    first_store.click()

    # Control : product is not available
    add_info = wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, ".missing-products")))
    assert "indisponible" in add_info.text
    print("Test is PASSED !!!!")

    # window_in = add_info.get_attribute('class')
    # print(window_in)
    # assert window_in=='missing'

    driver.quit()

#TP_Page_Object

def _page_object():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.carrefour.fr")

    home = HomePage(driver)
    home.close_cookie()
    home.open_menu()
    home.open_epicerie_salee()
    home.open_sub_category_menu()

    product_category = ProductCategoryPage(driver)


    driver.quit()

