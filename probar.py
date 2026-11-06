import json, sys, time
from curl_cffi import requests

URL_HOME = 'https://www.sofascore.com'
URL_API = 'https://www.sofascore.com/api/v1/event/16671600/shotmap'

def probar_curl():
    print('--- curl_cffi ---')
    try:
        r = requests.get(URL_API, impersonate='chrome', timeout=30)
        print('status:', r.status_code)
        print(r.text[:300])
        return r.status_code == 200
    except Exception as e:
        print('error:', str(e)[:200])
        return False

def probar_navegador():
    print('--- SeleniumBase UC + xvfb ---')
    from seleniumbase import Driver
    driver = None
    try:
        driver = Driver(uc=True)
        driver.get(URL_HOME)
        time.sleep(6)
        driver.get(URL_API)
        time.sleep(3)
        texto = driver.find_element('tag name', 'body').text
        print(texto[:300])
        json.loads(texto)
        print('JSON válido: OK')
        return True
    except Exception as e:
        print('error:', str(e)[:200])
        return False
    finally:
        if driver:
            driver.quit()

if __name__ == '__main__':
    ok_curl = probar_curl()
    ok_nav = probar_navegador()
    print(f'\nRESULTADO -> curl_cffi: {ok_curl} | navegador: {ok_nav}')
    sys.exit(0 if (ok_curl or ok_nav) else 1)
