import seleniumwire.undetected_chromedriver as uc
from time import sleep

def run_directlink_bot(link, proxy=None, headless=True):
    options = uc.ChromeOptions()
    if headless:
        options.add_argument('--headless=new')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-notifications')
    options.add_argument("--remote-debugging-port=9222")
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')
    options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2}) # Block all Image
    
    driver = uc.Chrome(options=options, seleniumwire_options=dict(proxy=dict(http=proxy, https=proxy)))
    driver.maximize_window()
    driver.get(link)
    sleep(5)
    driver.quit()


if __name__=='__main__':
    from all_links import random_directlink
    run_directlink_bot(random_directlink, headless=False)

