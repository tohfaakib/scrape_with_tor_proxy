## pip install requests stem requests[socks]
from stem import Signal
from stem.control import Controller
import requests


def get_tor_session():
    session = requests.session()
    # Tor uses the 9050 port as the default socks port
    # session.proxies = {'http': 'http://54.146.102.118:8181',
    #                    'https': 'http://54.146.102.118:8181'}


    # session.proxies = {'http': 'http://127.0.0.1:8181',
    #                    'https': 'http://127.0.0.1:8181'}

    session.proxies = {'http':  'socks5://127.0.0.1:9050',
                       'https': 'socks5://127.0.0.1:9050'}
    return session


# signal TOR for a new connection
def renew_connection():
    with Controller.from_port(address='127.0.0.1', port=9051) as controller:
        controller.authenticate(password="TorPass34")
        controller.signal(Signal.NEWNYM)


renew_connection()
session = get_tor_session()
response = session.get("http://mylocation.org/")
print(response.text)
