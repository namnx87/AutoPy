#===============================================================================
# Automatic download (latest) SFR facture
#===============================================================================


import re
from robobrowser import RoboBrowser
from requests import Session
import time
import dropbox
import common
url = 'https://www.sfr.fr/cas/login?service=https%3A%2F%2Fwww.sfr.fr%2Faccueil%2Fj_spring_cas_security_check&theme=espaceclientred'
factureUrl = 'https://espace-client-red.sfr.fr/facture-fixe/consultation?red=1'


if __name__ == '__main__':
    print "My automatic script to get latest SFR facture"
    session = Session()
    session.verify = False  # Skip SSL verification
    browser = RoboBrowser(session=session)
    browser.open(url)
    
    #Log in if needed
    form = browser.get_form(action='/cas/login?domain=espaceclientred&service=https%3A%2F%2Fwww.sfr.fr%2Faccueil%2Fj_spring_cas_security_check#sfrclicid=EC_mire_Me-Connecter')
    if form != None:
        form['username'].value = 'yourname@sfr.fr'
        form['password'].value = 'yourpass'
        browser.submit_form(form)
    print "Log in seems ok"
    time.sleep(5)
    print "Finding facture to download"
    browser.open(factureUrl)
    time.sleep(5)
    factures = browser.find(class_=re.compile(r'\bsr-chevron\b'))
    if factures == None:
        print "Something wrong!!! Could not find any facture"
        exit(1)
    print factures.next
    link = factures.attrs['href']
    #browser.follow_link(link)
    downUrl = u'http://espace-client-red.sfr.fr/%s' %link
    browser.open(downUrl)

    pdf_file = 'sfr_facture.pdf'
    common.saveFile(browser, pdf_file)
    common.uploadToDropbox(pdf_file)
    print "Done"

