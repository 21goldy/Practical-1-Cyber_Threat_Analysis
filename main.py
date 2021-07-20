import logo
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

print(logo.logo)
URL = str(input("\n🚨Enter the URL here for testing🚨: "))
# print(URL)

URL_SCORE = 0


def alexa_rank(x):
    ALEXA = "https://www.alexa.com/siteinfo/domain.com"

    chrome_driver_path = "C:\Program Files\Google\Chrome\Application\chromedriver.exe"

    driver = webdriver.Chrome(executable_path=chrome_driver_path)
    driver.get(ALEXA)

    driver.find_element_by_xpath('//*[@id="input-site"]').clear()
    time.sleep(5)
    domain_search = driver.find_element_by_xpath('//*[@id="input-site"]')
    domain_search.send_keys(x)
    domain_search.send_keys(Keys.ENTER)

    domain_rank = driver.find_element_by_class_name('rankmini-rank')
    alexa_ranking = domain_rank.text
    # if alexa_ranking != 0:
    print(f"1. Alexa ranking of the URL is {alexa_ranking}✅")
    # else:
    #     print("1. Alexa ranking does not exists!❌")


# alexa_rank()


def check_ipaddress(x):
    if URL.find('www') == -1 and ('https' in x or 'http' in x):
        print("2. Contains Ip address❌")

    else:
        print("2. Does not contains Ip address✅")


# check_ipaddress(URL)


def check_len(x):
    if len(x) >= 75:
        print('3. Length of the URL is greater than or equal to 75, Phishing URL❌')
    elif 54 <= len('URL'):
        print('3. Length of the URL is greater than or equal to 54, Suspicious URL❌')
    else:
        print('3. Length is less than 54, Legitimate URL✅')


# check_len(URL)


def check_symbol(x):
    if '@' in x:
        print("4. '@' symbol found!❌")
    else:
        print("4. '@' symbol not found!✅")


# check_symbol(URL)


def check_tinyurl(x):
    if 'tiny' in x or 'bitly' in x or 'free-url-shortener' in x:
        print("5. Uses tiny url❌")
    else:
        print("5. Does not uses tiny url✅")


# check_tinyurl(URL)


def check_hyphen(x):
    if '-' in x:
        print("6. '-' found!❌")
    else:
        print("6. '-' not found!✅")


# check_hyphen(URL)

def check_https(x):
    if 'https' in URL:
        print('7. Uses HTTPS protocol✅')
    else:
        print('7. Does not uses HTTPS protocol❌')


# check_https(URL)


def check_redirecting(x):
    if URL.count("//") > 1:
        print("8. Uses redirecting method❌")

    else:
        print("8. Does not uses redirecting method✅")


# check_redirecting(URL)

print("\nTest in progress...\n")
time.sleep(1)
print("Preparing the reports...")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)
print(".")

print("\n📜Test result:\n")
alexa_rank(URL)
check_ipaddress(URL)
check_len(URL)
check_symbol(URL)
check_tinyurl(URL)
check_hyphen(URL)
check_https(URL)
check_redirecting(URL)
