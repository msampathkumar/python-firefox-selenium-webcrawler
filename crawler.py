import os
import time
import psutil
from multiprocessing import Pool

# External
# from webdriver_manager.firefox import GeckoDriverManager
# from selenium.webdriver import Firefox
#
# try:
#     driver = Firefox(executable_path=GeckoDriverManager().install())
#     print("Selenium WebManager is UP!")
#     driver.quit()
#     del driver
# except Exception as err:
#     raise Exception("Selenium WebSetup Issue!!")
#     print(str(err))
#
# selenium 4
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

from retry import retry
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import FirefoxOptions


THREAD_COUNTS = 2  # max(2, round(psutil.cpu_count() * 0.8)) * 3

test_url_link = "https://cloud.google.com/vpc/docs/configure-private-google-access"


def _get_file_name(url_link):
    """
    Return a file name based on url_link, only if file not found.
    """
    # os.rmdir('html_files/')
    dir_name = "html_files/"
    if not os.path.isdir(dir_name):
        os.mkdir(dir_name)
    fname = url_link.replace("/", "#")
    fname = os.path.join(dir_name, fname) + ".html"
    if not os.path.isfile(fname):
        return fname


@retry(tries=2, delay=40)
def _open_url(url_link=test_url_link):
    fname = _get_file_name(url_link)
    if not fname:
        print(f"#Skipping {url_link}#")
        return
    print(f"#Running {url_link}#")
    # Firefox DriverSetup
    opts = FirefoxOptions()
    opts.add_argument("--headless")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    web_driver = webdriver.Firefox(options=opts)
    web_driver.get(url_link)
    # Time dynamic html elements to load
    try:
        element = WebDriverWait(web_driver, 40).until(
            EC.presence_of_element_located((By.TAG_NAME, "devsite-code"))
        )
    except Exception as err:
        message = f"Wait Error: {url_link} \n"
        message += str(err) + "\n"
        print(message)
        time.sleep(4)
    html = web_driver.page_source
    if html:
        print(f"#NoDataFound {url_link}#")
        _save_url_file(fname, html)
    web_driver.quit()
    del web_driver


def _save_url_file(fname, html):
    # Save File
    with open(fname, "w") as fp:
        fp.write(html)
        print(f"#Saving to {fname}#")


def open_url(url_link):
    try:
        _open_url(url_link)
    except Exception as error:
        message = f"Error Parsing: {url_link} \n"
        message += str(error)
        message += "\n"
        print(message)


def crawler_urls_main(urls_file_name):
    start_time = time.time()
    print(f"start_time is {start_time}")
    print(f"THREAD_COUNTS is {THREAD_COUNTS}")
    with open(urls_file_name) as fp:
        pool_urls = fp.read().strip().splitlines()
        with Pool(THREAD_COUNTS) as _pool:
            _pool.map(open_url, pool_urls)
    print("Done!")
    print(f"Total is {time.time()- start_time}")


if __name__ == "__main__":
    default_input_urls_list_file = "urls_list"
    if os.path.isfile(default_input_urls_list_file):
        crawler_urls_main(default_input_urls_list_file)
        # os.system('pkill -9 -f "firefox"')
        # ps -aux | grep php | awk '{print $2}' | xargs kill -9
        print("==" * 200)
