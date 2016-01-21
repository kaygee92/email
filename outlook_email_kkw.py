from selenium import webdriver

print('Input your email')
userEmail = input()
print('Input password')
userPassword = input()

browser = webdriver.Firefox()
browser.get('https://outlook.com')

emailElem = browser.find_element_by_id('i0116')
emailElem.send_keys (userEmail)

passwordElem = browser.find_element_by_id('i0118')
passwordElem.send_keys (userPassword)
passwordElem.submit ()

composeElem = browser.find_element_by_id('_fce_e.ms-bgc-tlr-h')
composeElem.submit ()
