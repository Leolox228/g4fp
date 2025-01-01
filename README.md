# g4fp
This is a library for unlimited use of LLM through g4f, using a proxy
# Installation:
```
pip install g4fp
```
Usage example (async):
```py
import asyncio
from g4fp import AsyncClientProxy

async def main():
    client = await AsyncClientProxy()
    messages = [
        {"role": "user", "content": "Привет!"}
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

client = ClientProxy()
messages = [
    {"role": "user", "content": "Привет!"}
]
response = client.chat.completions.create(
    model="o1-mini",
    messages=messages,
)
print(response.choices[0].message.content)
```
