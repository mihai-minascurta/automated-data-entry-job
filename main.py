from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

ADDRESS = "https://www.apartments.com/"
LOCATION = "San Francisco, CA"
SHEET_ADRESS = "https://docs.google.com/forms/d/e/1FAIpQLSefdvxJhbqWsMbJbKhXZS7TGlbPqNp_tSJRbyHFYevL4j0vhw/viewform"

address_list = []
price_list = []
links_list = []

class AutoEntryJob:
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.prefs = {
            "profile.default_content_setting_values.geolocation": 2,  # 1 = allow, 2 = block
            "profile.default_content_setting_values.notifications": 2
        }
        self.options.add_experimental_option("prefs", self.prefs)
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.maximize_window()
        self.driver.get(ADDRESS)
        time.sleep(5)

    
    def searching(self):
        try:
            self.search = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#quickSearchLookup')))
            self.search.send_keys(LOCATION)
            time.sleep(5)

            self.go_search = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.storyicon.searchStoryIcon')))
            self.go_search.click()
            time.sleep(5)
            print("Cautarea locatiei a avut succes")
        except Exception as e:
            print(f"Eroare la cautarea locatiei , {e}")
    

    def apply_filtrer(self):
        try:
            #Filtru cu pret
            self.price_click = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[id='rentRangeLink'] i[class='storyicon down2StoryIcon']")))
            self.price_click.click()
            time.sleep(5)

            self.price_min = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#min-input')))
            self.price_min.send_keys("2200")
            time.sleep(5)

            self.price_max = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#max-input')))
            self.price_max.send_keys("2700")
            self.price_max.send_keys(Keys.ENTER)
            time.sleep(5)

            #Filtru cu dormitor/baie
            self.bed_click = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[id='bedRangeLink'] span:nth-child(1)")))
            self.bed_click.click()
            time.sleep(5)

            self.one_bed = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "header[id='searchBar'] div[class='button-group bed-filter-container '] button:nth-child(3)")))
            self.one_bed.click()
            time.sleep(5)

            self.one_bath = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "header[id='searchBar'] div[class='button-group bath-filter-container'] button:nth-child(2)")))
            self.one_bath.click()
            time.sleep(5)

            self.done = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[class='content-container'] button[class='done-btn btn btn-sm btn-text']")))
            self.done.click()
            time.sleep(5)
            #Filtru cu tipul de locatie
            self.type_click = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[id='typeSelect'] span[class='label search-filter-label']")))
            self.type_click.click()
            time.sleep(5)

            self.apartment = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[class='wrapper'] i[class='storyicon propApartmentStoryIcon']")))
            self.apartment.click()
            time.sleep(5)

            self.done_apartment = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[data-bind='click: searchTypeClicked']")))
            self.done_apartment.click()
            time.sleep(5)
            print("Toate filtrele au fost aplicate cu succes")
        except Exception as e:
            print(f"Eroare la filtre , {e}")

    def scroll_and_extract(self): #Functia care foloseste functia extract care extrage valorile, si in aceasta functie in timp ce se scroleaza se extrage
        try:
            last_height = self.driver.execute_script("return document.body.scrollHeight")

            while True:
                # Extragem datele vizibile
                self.extract_visible_properties()

                # Scroll jos
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(3)

                new_height = self.driver.execute_script("return document.body.scrollHeight")
                if new_height == last_height:
                    break  # Dacă nu mai există scroll nou, ieșim
                last_height = new_height

            print("Scroll-ul s-a terminat și datele au fost extrase")
            print(f"Adrese extrase:", address_list , len(address_list))
            print("Preturi extrase:", price_list , len(price_list))
            print("Link-uri extrase:", links_list , len(links_list))
            
        except Exception as e:
            print(f"Eroare la scroll și extragere: {e}")

    def extract_visible_properties(self):
        try:
            property_elements = self.driver.find_elements(By.CSS_SELECTOR, '#placardContainer ul li')
            #Se vor folosi mai multe try except uri deoarece unele locatii au selectori diferiti
            for prop in property_elements:
                #Vrem sa memoram doar 20 dintre acestea
                if len(address_list) >= 20:
                    break
                # Adresa
                address = "No address listed"
                try:
                    address = prop.find_element(By.CSS_SELECTOR, '.property-address').text
                except:
                    try:
                        address = prop.find_element(By.CSS_SELECTOR, '.js-placardTitle').text
                    except:
                        pass

                # Prețul
                price = "No price listed"
                try:
                    price = prop.find_element(By.CSS_SELECTOR, '.property-pricing').text
                except:
                    try:
                        price = prop.find_element(By.CSS_SELECTOR, '.price-range').text
                    except:
                        try:
                            price = prop.find_element(By.CSS_SELECTOR, '.property-rents').text
                        except:
                            pass

                # Link-ul
                link = "No link found"
                try:
                    link = prop.find_element(By.CSS_SELECTOR, 'a.property-link').get_attribute('href')
                except:
                    pass

                # Salvăm doar linkurile noi și valide
                if link != "No link found" and link not in links_list:
                    address_list.append(address)
                    price_list.append(price)
                    links_list.append(link)

        except Exception as e:
            print(f"Eroare la extragerea proprietăților vizibile: {e}")
    
    def google_sheet_data(self):
        try:
            self.driver.close()
            self.google_options = webdriver.ChromeOptions()
            self.google_options.add_experimental_option("prefs", self.prefs)
            self.google_driver = webdriver.Chrome(options=self.google_options)
            
            self.google_driver.get(SHEET_ADRESS)
            self.google_driver.maximize_window()
            time.sleep(5)
            print("Pagina cu google sheet a fost accesata cu succes")
        except Exception as e:
            print(f"Nu s a putut accesa pagina google sheet, {e}")

    def entry_data_sheet(self):


        try:
            for adress,price,list in zip(address_list,price_list,links_list):
                time.sleep(1)
                self.paste_adress = WebDriverWait(self.google_driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div[2]/textarea')))
                self.paste_adress.send_keys(adress)
                self.paste_adress = WebDriverWait(self.google_driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[2]/textarea')))
                self.paste_adress.send_keys(price)

                self.paste_link = WebDriverWait(self.google_driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[2]/textarea')))
                self.paste_link.send_keys(list)

                self.send = WebDriverWait(self.google_driver,10).until(EC.visibility_of_element_located((By.XPATH, '//span[text()="Trimite"]')))
                self.send.click()

                self.another_answer = WebDriverWait(self.google_driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')))
                self.another_answer.click()
            print("Datele au fost puse cu succes")
        except Exception as e:
            print(f"Eroare la introducerea datelor , {e}")

job = AutoEntryJob()
job.searching()
job.apply_filtrer()
job.scroll_and_extract()
job.google_sheet_data()
job.entry_data_sheet()

