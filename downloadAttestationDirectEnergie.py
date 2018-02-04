#===============================================================================
# Automatic download (latest) direct energie facture
#===============================================================================


from selenium import webdriver
import time
webpage = r"https://clients.direct-energie.com/connexion-clients-particuliers/?tx_deauthentification[redirect_url]=https%3A%2F%2Fclients.direct-energie.com%2Fmon-espace-client%2F"

justificatifUrl = r"https://clients.direct-energie.com/mes-factures/mon-justificatif-de-domicile/" 
userName = "yourname@email.com" 
password = "yourpass"

driver = webdriver.Chrome()
driver.get(webpage)

sbox = driver.find_element_by_id("tx_deauthentification_login")
sbox.send_keys(userName)
sbox = driver.find_element_by_id("tx_deauthentification_password")
sbox.send_keys(password)

submit = driver.find_element_by_id("tx_deauthentification_mdp_oublie")
submit.click()

time.sleep(5)
# driver.get(justificatifUrl)
# download = driver.find_element_by_id("btn_justificatif")
# download.click()

factureUrl = 'https://clients.direct-energie.com/mes-factures/ma-facture-mon-echeancier/'
driver.get(factureUrl)

submit = driver.find_element_by_class_name("picto__puce__document_pdf")
submit.click()





print "Done"