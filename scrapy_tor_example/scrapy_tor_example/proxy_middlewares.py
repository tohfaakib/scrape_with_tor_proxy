from stem import Signal
from stem.control import Controller


def _set_new_ip():
    with Controller.from_port(port=9051) as controller:
        controller.authenticate(password='TorPass34')
        controller.signal(Signal.NEWNYM)


class ProxyMiddleware(object):
    def process_request(self, request, spider):
        _set_new_ip()
        # request.meta['proxy'] = 'http://54.146.102.118:8181'
        request.meta['proxy'] = 'http://127.0.0.1:8181'
        # request.meta['http'] = 'socks5://127.0.0.1:9050'
        # request.meta['https'] = 'socks5://127.0.0.1:9050'
        # spider.log('Proxy : %s' % request.meta['http'])
        # spider.log('Proxy : %s' % request.meta['https'])
        spider.log('Proxy : %s' % request.meta['proxy'])
