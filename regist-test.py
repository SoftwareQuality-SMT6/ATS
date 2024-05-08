from selenium import webdriver
# menggunakan fungsi By
from selenium.webdriver.common.by import By
# menggunakan fungsi time
import time
 
options = webdriver.ChromeOptions()
options.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=options)

def click_signup_success_ok(driver):
  """akan mengklik 'Ok' pada notifikasi Javascript."""
  # memberi jeda hingga 10 detik untuk modal nya muncul
  time.sleep(10)

  try:
    # mencari element modal menggunakan ID
    modal = driver.find_element(By.ID, "signInModal")

    # mencari elemen 'Ok' Button dalam modal menggunakan XPATH
    # membuat 2 pencarian kata 'OK' atau 'Ok', untuk menghindari case-sensitive
    ok_button = modal.find_element(By.XPATH, ".//button[text()='Ok' or contains(text(), 'OK')]")
    ok_button.click()

  except Exception as e:
    print(f"Error clicking OK button: {e}")

driver.get("https://www.demoblaze.com/")
tombol = driver.find_element(By.ID,"signin2")
# jalankan variabel tombol dengan fungsi click()
tombol.click()

# fungsi sleep digunakan untuk membuat delay
time.sleep(5)

# menggunakan fungsi By untuk mengetahui elemen di web menggunakan ID
driver.find_element(By.ID,"sign-username").send_keys("dkwadakdmnao")
driver.find_element(By.ID,"sign-password").send_keys("ksdnfnsoienf")

# fungsi sleep digunakan untuk membuat delay
time.sleep(5)

# menggunakan fungsi By untuk mengetahui elemen di web menggunakan XPATH
sign_up_button = driver.find_element(By.XPATH, "//button[text()='Sign up']")

# fungsi yaitu mengklik button sign_up_button
sign_up_button.click()

# fungsi sleep digunakan untuk membuat delay
time.sleep(5)

# fungsi yaitu mengklik button 'Ok' pada notifikasi Javascript
click_signup_success_ok(driver) 