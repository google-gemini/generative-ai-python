Google Generative AI Python Client
==================================

[![PyPI version](https://badge.fury.io/py/google-generativeai.svg)](https://badge.fury.io/py/google-generativeai)
![PyPI - Downloads](https://img.shields.io/pypi/dd/google-generativeai)

Get started using the PaLM API in Python. Check out the [developer site](https://developers.generativeai.google/)
for comprehensive documentation.

## Installation and usage

Install from PyPI.
```bash
pip install google-generativeai
```

Get an [API key from MakerSuite](https://makersuite.google.com/app/apikey), then configure it here.
```python
import google.generativeai as palm

palm.configure(api_key=os.environ['PALM_API_KEY'])
```

Use the `palm.chat` function to have a discussion with a model.
```python
response = palm.chat(messages=["Hello."])
print(response.last) #  'Hello! What can I help you with?'
response.reply("Can you tell me a joke?")
```

## Documentation

Checkout the full [API docs](https://developers.generativeai.google/api), the [guide](https://developers.generativeai.google/guide) and [quick starts](https://developers.generativeai.google/tutorials).

## Colab magics

Once installed, use the Python client via the `%%palm` Colab magic. Read the full guide [here](https://developers.generativeai.google/tools/notebook_magic).

```python
%%palm
The best thing since sliced bread is
```
