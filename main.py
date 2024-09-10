import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys  

# Initialize the ChromeOptions
options = webdriver.ChromeOptions()
# Uncomment the line below to run headless (without opening a browser window)
# options.add_argument("--headless")  
driver = webdriver.Chrome(options=options)

# Fungsi untuk mengirim pesan
def kirim_pesan(driver, link_messenger, nama_facebook):
    # Format pesan dengan baris baru (\n) untuk membuat teks di setiap baris terpisah dalam satu bubble
    pesan = f"Hallo {nama_facebook}, ini adalah pesan dariku, perkenalkan namaku Rangga. Terimakasih."

    driver.get(link_messenger)
    time.sleep(5)
    
    try:
        # Tunggu hingga kotak pesan dapat ditemukan
        message_box = driver.find_element(By.XPATH, '//div[@aria-label="Pesan"]')
        message_box.send_keys(pesan)  # Kirim seluruh pesan sekaligus dengan baris baru
        message_box.send_keys(Keys.RETURN)
        time.sleep(3)
        print(f"Pesan terkirim ke {nama_facebook} ({link_messenger})")
    except Exception as e:
        print(f"Gagal mengirim pesan ke {nama_facebook} ({link_messenger}): {str(e)}")



link_login = 'https://www.facebook.com'

driver.get(link_login)

username = driver.find_element(By.CSS_SELECTOR, "input[name='email']")
password = driver.find_element(By.CSS_SELECTOR, "input[name='pass']")

username.clear()
username.send_keys("ranggaperkasa822@yahoo.com")
time.sleep(5)
password.clear()
password.send_keys("Jendela2!")
time.sleep(5)

driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
time.sleep(5)

# Membaca file CSV
with open('./test_facebook.csv', newline='') as csvfile:
    csvreader = csv.DictReader(csvfile)
    
    for row in csvreader:
        nama_facebook = row['nama_facebook']
        link_messenger = row['link_messenger']
        
        # Kirim pesan ke masing-masing link
        kirim_pesan(driver, link_messenger, nama_facebook)

driver.quit()