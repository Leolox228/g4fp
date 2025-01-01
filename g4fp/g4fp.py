#g4fp.py
import asyncio
from fp.fp import FreeProxy
from g4f.client import Client, AsyncClient

class _ProxyWrapper:
    def __init__(self, wrapped_obj):
        self._wrapped = wrapped_obj

    def __getattr__(self, name):
        attr = getattr(self._wrapped, name)
        if callable(attr):
            def method_wrapper(*args, **kwargs):
                while True:
                    try:
                        proxy = FreeProxy(timeout=5, rand=True).get()
                        kwargs["proxy"] = proxy
                        return attr(*args, **kwargs)
                    except Exception:
                        pass
            return method_wrapper
        elif hasattr(attr, '__dict__'):
            return _ProxyWrapper(attr)
        else:
            return attr

class _AsyncProxyWrapper:
    def __init__(self, wrapped_obj):
        self._wrapped = wrapped_obj
        self._loop = asyncio.get_event_loop()

    def __getattr__(self, name):
        attr = getattr(self._wrapped, name)
        if callable(attr):
            async def method_wrapper(*args, **kwargs):
                while True:
                    try:
                        proxy = await self._loop.run_in_executor(None, lambda: FreeProxy(timeout=5, rand=True).get())
                        kwargs["proxy"] = proxy
                        result = attr(*args, **kwargs)
                        if asyncio.iscoroutine(result):
                            return await result
                        return result
                    except Exception:
                        pass
            return method_wrapper
        elif hasattr(attr, '__dict__'):
            return _AsyncProxyWrapper(attr)
        else:
            return attr

def ClientProxy():
    original_client = Client()
    return _ProxyWrapper(original_client)

async def AsyncClientProxy():
    original_async_client = AsyncClient()
    return _AsyncProxyWrapper(original_async_client)
