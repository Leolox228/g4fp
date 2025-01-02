#g4fp.py
import asyncio
from g4f.client import Client, AsyncClient
from proxy_list import ProxyList

class _ProxyWrapper:
    def __init__(self, wrapped_obj, debug=False):
        self._wrapped = wrapped_obj
        self.debug = debug

    def __getattr__(self, name):
        attr = getattr(self._wrapped, name)
        if callable(attr):
            def method_wrapper(*args, **kwargs):
                while True:
                    try:
                        proxy_list = ProxyList()
                        proxy = proxy_list.get_random_proxy()
                        if self.debug:
                            print(f"[DEBUG] Using proxy: {proxy}")
                        kwargs["proxy"] = "https://" + proxy.get("https")
                        result = attr(*args, **kwargs)
                        if self.debug:
                            print("[SUCCESS]")
                        return result
                    except Exception as e:
                        if self.debug:
                            print(f"[ERROR] {e}")
                        pass
            return method_wrapper
        elif hasattr(attr, '__dict__'):
            return _ProxyWrapper(attr, self.debug)
        else:
            return attr

class _AsyncProxyWrapper:
    def __init__(self, wrapped_obj, debug=False):
        self._wrapped = wrapped_obj
        self.debug = debug
        self._loop = asyncio.get_event_loop()

    def __getattr__(self, name):
        attr = getattr(self._wrapped, name)
        if callable(attr):
            async def method_wrapper(*args, **kwargs):
                while True:
                    try:
                        proxy_list = ProxyList()
                        proxy = await self._loop.run_in_executor(None, lambda: proxy_list.get_random_proxy())
                        if self.debug:
                            print(f"[DEBUG] Using proxy: {proxy}")
                        kwargs["proxy"] = "https://" + proxy.get("https")
                        result = attr(*args, **kwargs)
                        if asyncio.iscoroutine(result):
                            result = await result
                        if self.debug:
                            print("[SUCCESS]")
                        return result
                    except Exception as e:
                        if self.debug:
                            print(f"[ERROR] {e}")
                        pass
            return method_wrapper
        elif hasattr(attr, '__dict__'):
            return _AsyncProxyWrapper(attr, self.debug)
        else:
            return attr

def ClientProxy(debug=False):
    original_client = Client()
    return _ProxyWrapper(original_client, debug)

async def AsyncClientProxy(debug=False):
    original_async_client = AsyncClient()
    return _AsyncProxyWrapper(original_async_client, debug)
