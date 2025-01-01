# g4fp
This is a library for unlimited use of LLM through g4f, using a proxy
# Installation:
```
pip install g4fp
```
# Now you can pass debug (bool) and proxy (FreeProxy object) values to ClientProxy and AsyncClientProxy
Usage example (async):
```py
import asyncio
from fp.fp import FreeProxy
from g4fp import AsyncClientProxy

async def main():
    client = await AsyncClientProxy(debug=False, proxy=FreeProxy(timeout=5, rand=True))
    messages = [
        {"role": "user", "content": "Hello!"}
    ]
    response = await client.chat.completions.create(
        model="o1-mini",
        messages=messages,
    )
    print(response.choices[0].message.content)

if __name__ == "__main__":
    asyncio.run(main())
```
Usage example (sync):
```py
from g4fp import ClientProxy

client = ClientProxy(debug=True)
messages = [
    {"role": "user", "content": "Hello!"}
]
response = client.chat.completions.create(
    model="o1-mini",
    messages=messages,
)
print(response.choices[0].message.content)
```
