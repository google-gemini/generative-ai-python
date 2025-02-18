# Google AI Python SDK for the Gemini API

[![PyPI version](https://badge.fury.io/py/google-generativeai.svg)](https://badge.fury.io/py/google-generativeai)
![Python support](https://img.shields.io/pypi/pyversions/google-generativeai)
![PyPI - Downloads](https://img.shields.io/pypi/dd/google-generativeai)

> [!IMPORTANT]
> From Gemini 2.0 onwards this SDK will no longer be
developing new features. Any new code should be written using the new SDK, `google-genai` ([github](https://github.com/googleapis/python-genai),
[pypi](https://pypi.org/project/google-genai/)). See the migration guide below to upgrade to the new SDK.

# Upgrade the Google GenAI SDK for Python

With Gemini 2 we are offering a [new SDK](https://github.com/googleapis/python-genai)
(<code>[google-genai](https://pypi.org/project/google-genai/)</code>,
<code>v1.0</code>). The updated SDK is fully compatible with all Gemini API
models and features, including recent additions like the
[live API](https://aistudio.google.com/live) (audio + video streaming),
improved tool usage (
[code execution](https://ai.google.dev/gemini-api/docs/code-execution?lang=python),
[function calling](https://ai.google.dev/gemini-api/docs/function-calling/tutorial?lang=python) and integrated
[Google search grounding](https://ai.google.dev/gemini-api/docs/grounding?lang=python)),
and media generation ([Imagen](https://ai.google.dev/gemini-api/docs/imagen)).
This SDK allows you to connect to the Gemini API through either
[Google AI Studio](https://aistudio.google.com/prompts/new_chat?model=gemini-2.0-flash-exp) or
[Vertex AI](https://cloud.google.com/vertex-ai/generative-ai/docs/gemini-v2).

The <code>[google-generativeai](https://pypi.org/project/google-generativeai)</code>
package will continue to support the original Gemini models.
It <em>can</em> also be used with Gemini 2 models, just with a limited feature
set. All new features will be developed in the new Google GenAI SDK.

<!-- 
[START update]
# With Gemini-2 we're launching a new SDK, see this doc for details.
# https://ai.google.dev/gemini-api/docs/migrate
[END update]
 -->

<table align="left">
  <td>
    <a target="_blank" href="https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started.ipynb">
        <img src="https://ai.google.dev/site-assets/images/docs/colab_logo_32px.png" />
        Try the new SDK in Google Colab
    </a>
  </td>
</table>
</br></br>

## Install the SDK

**Before**

```
pip install -U -q "google-generativeai"
```

**After**

```
pip install -U -q "google-genai"
```

## Authenticate

Authenticate with API key. You can
[create](https://aistudio.google.com/app/apikey)
your API key using Google AI studio.


The old SDK implicitly handled the API client object behind the scenes. In the
new SDK you create the API client and use it to call the API.

Remember, in either case the SDK will pick
up your API key from the `GOOGLE_API_KEY` environment variable if you don't pass
one to `configure`/`Client`.

<pre class="devsite-terminal"><code>export GOOGLE_API_KEY=...</code></pre>

**Before**

```python
import google.generativeai as genai

genai.configure(api_key=...)
```

**After**

```python
from google import genai

client = genai.Client(api_key=...)
```

## Generate content

The new SDK provides access to all the API methods through the `Client` object.
Except for a few stateful special cases (`chat`, live-api `session`s) these are all
stateless functions. For utility and uniformity objects returned are `pydantic`
classes.

**Before**

```python
import google.generativeai as genai

model = genai.GenerativeModel('gemini-1.5-flash')
response = model.generate_content(
    'Tell me a story in 300 words'
)
print(response.text)
```

**After**

```python
from google import genai
client = genai.Client()

response = client.models.generate_content(
    model='gemini-2.0-flash', 
    contents='Tell me a story in 300 words.'
)
print(response.text)

print(response.model_dump_json(
    exclude_none=True, indent=4))
```


Many of the same convenience features exist in the new SDK. For example
`PIL.Image` objects are automatically converted:

**Before**

```python
import google.generativeai as genai

model = genai.GenerativeModel('gemini-1.5-flash')
response = model.generate_content([
    'Tell me a story based on this image',
    Image.open(image_path)
])
print(response.text)
```

**After**

```python
from google import genai
from PIL import Image

client = genai.Client()

response = client.models.generate_content(
    model='gemini-2.0-flash',
    contents=[
        'Tell me a story based on this image',
        Image.open(image_path)
    ]
)
print(response.text)
```


### Streaming

Streaming methods are each separate functions named with a `_stream` suffix.

**Before**

```python
import google.generativeai as genai

response = model.generate_content(
    "Write a cute story about cats.",
    stream=True)
for chunk in response:
    print(chunk.text)
```

**After**

```python
from google import genai
client = genai.Client()

for chunk in client.models.generate_content_stream(
  model='gemini-2.0-flash',
  contents='Tell me a story in 300 words.'
):
    print(chunk.text)
```


## Optional arguments

For all methods in the new SDK the required arguments are provided as keyword
arguments. All optional inputs are provided in the `config` argument.

The `config` can always be passed as a dictionary or, for better autocomplete and
stricter typing, each method has a `Config` class in the `google.genai.types`
module. For utility and uniformity, everything in the `types` module is defined
as a `pydantic` class. 

**Before**

```python
import google.generativeai as genai

model = genai.GenerativeModel(
   'gemini-1.5-flash',
    system_instruction='you are a story teller for kids under 5 years old',
    generation_config=genai.GenerationConfig(
       max_output_tokens=400,
       top_k=2,
       top_p=0.5,
       temperature=0.5,
       response_mime_type='application/json',
       stop_sequences=['\n'],
    )
)
response = model.generate_content('tell me a story in 100 words')

```

**After**

```python
from google import genai
from google.genai import types
client = genai.Client()

response = client.models.generate_content(
  model='gemini-2.0-flash',
  contents='Tell me a story in 100 words.',
  config=types.GenerateContentConfig(
      system_instruction='you are a story teller for kids under 5 years old',
      max_output_tokens= 400,
      top_k= 2,
      top_p= 0.5,
      temperature= 0.5,
      response_mime_type= 'application/json',
      stop_sequences= ['\n'],
      seed=42,
   ),
)
```


### Example: Safety settings

Generate response with safety settings:

**Before**

```python
import google.generativeai as genai

model = genai.GenerativeModel('gemini-1.5-flash')
response = model.generate_content(
    'say something bad',
    safety_settings={
        'HATE': 'BLOCK_ONLY_HIGH',
        'HARASSMENT': 'BLOCK_ONLY_HIGH',
   }
)
```

**After**

```python
from google import genai
from google.genai import types
client = genai.Client()

response = client.models.generate_content(
  model='gemini-2.0-flash',
  contents='say something bad',
  config=types.GenerateContentConfig(
      safety_settings= [
          types.SafetySetting(
              category='HARM_CATEGORY_HATE_SPEECH',
              threshold='BLOCK_ONLY_HIGH'
          ),
      ]
  ),
)
```


## Async

To use the new SDK with `asyncio`, there is a separate `async` implementation of
every method under `client.aio`.

**Before**

```python
import google.generativeai as genai

model = genai.GenerativeModel('gemini-1.5-flash')
response = model.generate_content_async(
    'tell me a story in 100 words'
)
```

**After**

```python
from google import genai
client = genai.Client()

response = await client.aio.models.generate_content(
    model='gemini-2.0-flash', 
    contents='Tell me a story in 300 words.'
)
```

## Chat

Starts a chat and sends a message to the model:

**Before**

```python
import google.generativeai as genai

model = genai.GenerativeModel('gemini-1.5-flash')
chat = model.start_chat()

response = chat.send_message(
    "Tell me a story in 100 words")
response = chat.send_message(
    "What happened after that?")
```

**After**

```python
from google import genai
client = genai.Client()

chat = client.chats.create(model='gemini-2.0-flash')

response = chat.send_message(
    message='Tell me a story in 100 words')
response = chat.send_message(
    message='What happened after that?')
```


## Function calling

In the New SDK, automatic function calling is the default. Here we disable it. 

**Before**

```python
import google.generativeai as genai
from enum import Enum 

def get_current_weather(location: str) -> str:
    """Get the current whether in a given location.

    Args:
        location: required, The city and state, e.g. San Franciso, CA
        unit: celsius or fahrenheit
    """
    print(f'Called with: {location=}')
    return "23C"

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    tools=[get_current_weather]
)

response = model.generate_content("What is the weather in San Francisco?")
function_call = response.candidates[0].parts[0].function_call
```

**After**

```python
from google import genai
from google.genai import types
client = genai.Client()

def get_current_weather(location: str) -> str:
    """Get the current whether in a given location.

    Args:
        location: required, The city and state, e.g. San Franciso, CA
        unit: celsius or fahrenheit
    """
    print(f'Called with: {location=}')
    return "23C"

response = client.models.generate_content(
   model='gemini-2.0-flash',
   contents="What is the weather like in Boston?",
   config=types.GenerateContentConfig(
       tools=[get_current_weather],
       automatic_function_calling={'disable': True},
   ),
)

function_call = response.candidates[0].content.parts[0].function_call
```

### Automatic function calling

The old SDK only supports automatic function calling in chat. In the new SDK
this is the default behavior in `generate_content`.

**Before**

```python
import google.generativeai as genai

def get_current_weather(city: str) -> str:
    return "23C"

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    tools=[get_current_weather]
)

chat = model.start_chat(
    enable_automatic_function_calling=True)
result = chat.send_message("What is the weather in San Francisco?")
```

**After**

```python
from google import genai
from google.genai import types
client = genai.Client()

def get_current_weather(city: str) -> str:
    return "23C"

response = client.models.generate_content(
   model='gemini-2.0-flash',
   contents="What is the weather like in Boston?",
   config=types.GenerateContentConfig(
       tools=[get_current_weather] 
   ),
)
```

## Code execution

Code execution is a tool that allows the model to generate Python code, run it,
and return the result.

**Before**

```python
import google.generativeai as genai

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    tools="code_execution"
)

result = model.generate_content(
  "What is the sum of the first 50 prime numbers? Generate and run code for "
  "the calculation, and make sure you get all 50.")
```

**After**

```python
from google import genai
from google.genai import types
client = genai.Client()

response = client.models.generate_content(
    model='gemini-2.0-flash',
    contents='What is the sum of the first 50 prime numbers? Generate and run '
             'code for the calculation, and make sure you get all 50.',
    config=types.GenerateContentConfig(
        tools=[types.Tool(code_execution=types.CodeExecution())],
    ),
)
```

## Search grounding

`GoogleSearch` (Gemini>=2.0) and `GoogleSearchRetrieval` (Gemini < 2.0) are tools
that allow the model to retrieve public web data for grounding, powered by Google.

**Before**

```python
import google.generativeai as genai

model = genai.GenerativeModel('gemini-1.5-flash')
response = model.generate_content(
    contents="what is the Google stock price?",
    tools='google_search_retrieval'
)
```

**After**

```python
from google import genai
from google.genai import types
client = genai.Client()

response = client.models.generate_content(
    model='gemini-2.0-flash',
    contents='What is the Google stock price?',
    config=types.GenerateContentConfig(
        tools=[
            types.Tool(
                google_search=types.GoogleSearch()
            )
        ]
    )
)
```

## JSON response

Generate answers in JSON format.

By specifying a `response_schema` and setting
`response_mime_type="application/json"` users can constrain the model to produce a
`JSON` response following a given structure. The new SDK uses `pydantic` classes
to provide the schema (although you can pass a `genai.types.Schema`, or equivalent
`dict`). When possible, the SDK will parse the returned JSON, and return the
result in `response.parsed`. If you provided a `pydantic` class as the schema the
SDK will convert that `JSON` to an instance of the class.

**Before**

```python
import google.generativeai as genai
import typing_extensions as typing

class CountryInfo(typing.TypedDict):
    name: str
    population: int
    capital: str
    continent: str
    major_cities: list[str]
    gdp: int
    official_language: str
    total_area_sq_mi: int

model = genai.GenerativeModel(model_name="gemini-1.5-flash")
result = model.generate_content(
    "Give me information of the United States",
     generation_config=genai.GenerationConfig(
         response_mime_type="application/json",
         response_schema = CountryInfo
     ),
)

```

**After**

```python
from google import genai
from pydantic import BaseModel
client = genai.Client()

class CountryInfo(BaseModel):
    name: str
    population: int
    capital: str
    continent: str
    major_cities: list[str]
    gdp: int
    official_language: str
    total_area_sq_mi: int

response = client.models.generate_content( 
    model='gemini-2.0-flash', 
    contents='Give me information of the United States.', 
    config={ 
        'response_mime_type': 'application/json',
        'response_schema': CountryInfo, 
    }, 
 )

response.parsed
```

## Files

### Upload

Upload a file:

**Before**

```python
import requests
import pathlib
import google.generativeai as genai

# Download file
response = requests.get(
    'https://storage.googleapis.com/generativeai-downloads/data/a11.txt')
pathlib.Path('a11.txt').write_text(response.text)

file = genai.upload_file(path='a11.txt')

model = genai.GenerativeModel('gemini-1.5-flash')
response = model.generate_content([
    'Can you summarize this file:', 
    my_file
])
print(response.text)
```

**After**

```python
import requests
import pathlib
from google import genai
client = genai.Client()

# Download file
response = requests.get(
    'https://storage.googleapis.com/generativeai-downloads/data/a11.txt')
pathlib.Path('a11.txt').write_text(response.text)

my_file = client.files.upload(file='a11.txt')

response = client.models.generate_content(
    model='gemini-2.0-flash', 
    contents=[
        'Can you summarize this file:', 
        my_file
    ]
)
print(response.text)
```

### List and get

List uploaded files and get an uploaded file with a file name:

**Before**

```python
import google.generativeai as genai

for file in genai.list_files():
  print(file.name)

file = genai.get_file(name=file.name)
```

**After**

```python
from google import genai
client = genai.Client()

for file in client.files.list():
    print(file.name)

file = client.files.get(name=file.name)
```


### Delete

Delete a file:

**Before**

```python
import pathlib
import google.generativeai as genai

pathlib.Path('dummy.txt').write_text(dummy)
dummy_file = genai.upload_file(path='dummy.txt')

file = genai.delete_file(name=dummy_file.name)
```

**After**

```python
import pathlib
from google import genai
client = genai.Client()

pathlib.Path('dummy.txt').write_text(dummy)
dummy_file = client.files.upload(file='dummy.txt')

response = client.files.delete(name=dummy_file.name)
```


## Context caching

Context caching allows the user to pass the content to the model once, cache the
input tokens, and then refer to the cached tokens in subsequent calls to lower the
cost.

**Before**

```python
import requests
import pathlib
import google.generativeai as genai
from google.generativeai import caching

# Download file
response = requests.get(
    'https://storage.googleapis.com/generativeai-downloads/data/a11.txt')
pathlib.Path('a11.txt').write_text(response.text)


# Upload file
document = genai.upload_file(path="a11.txt")

# Create cache
apollo_cache = caching.CachedContent.create(
    model="gemini-1.5-flash-001",
    system_instruction="You are an expert at analyzing transcripts.",
    contents=[document],
)

# Generate response
apollo_model = genai.GenerativeModel.from_cached_content(
    cached_content=apollo_cache
)
response = apollo_model.generate_content("Find a lighthearted moment from this transcript")
```

**After**

```python
import requests
import pathlib
from google import genai
from google.genai import types
client = genai.Client()

# Check which models support caching.
for m in client.models.list():
  for action in m.supported_actions:
    if action == "createCachedContent":
      print(m.name) 
      break

# Download file
response = requests.get(
    'https://storage.googleapis.com/generativeai-downloads/data/a11.txt')
pathlib.Path('a11.txt').write_text(response.text)


# Upload file
document = client.files.upload(file='a11.txt')

# Create cache
model='gemini-1.5-flash-001'
apollo_cache = client.caches.create(
      model=model,
      config={
          'contents': [document],
          'system_instruction': 'You are an expert at analyzing transcripts.',
      },
  )

# Generate response
response = client.models.generate_content(
    model=model,
    contents='Find a lighthearted moment from this transcript',
    config=types.GenerateContentConfig(
        cached_content=apollo_cache.name,
    )
)
```

## Count tokens

Count the number of tokens in a request.

**Before**

```python
import google.generativeai as genai

model = genai.GenerativeModel('gemini-1.5-flash')
response = model.count_tokens(
    'The quick brown fox jumps over the lazy dog.')

```

**After**

```python
from google import genai
client = genai.Client()

response = client.models.count_tokens(
    model='gemini-2.0-flash',
    contents='The quick brown fox jumps over the lazy dog.',
)
```

## Generate images

Generate images:

**Before**

```python
#pip install https://github.com/google-gemini/generative-ai-python@imagen
import google.generativeai as genai

imagen = genai.ImageGenerationModel(
    "imagen-3.0-generate-001")
gen_images = imagen.generate_images(
    prompt="Robot holding a red skateboard",
    number_of_images=1,
    safety_filter_level="block_only_high",
    person_generation="allow_adult",
    aspect_ratio="3:4",
    negative_prompt="Outside",
)
```

**After**

```python
from google import genai
client = genai.Client()

gen_images = client.models.generate_image(
    model='imagen-3.0-generate-001',
    prompt='Robot holding a red skateboard',
    config=types.GenerateImageConfig(
        number_of_images= 1,
        safety_filter_level= "BLOCK_ONLY_HIGH",
        person_generation= "ALLOW_ADULT",
        aspect_ratio= "3:4",
        negative_prompt= "Outside",
    )
)

for n, image in enumerate(gen_images.generated_images):
    pathlib.Path(f'{n}.png').write_bytes(
        image.image.image_bytes)
```


## Embed content

Generate content embeddings.

**Before**

```python
import google.generativeai as genai

response = genai.embed_content(
   model='models/text-embedding-004',
   content='Hello world'
)
```

**After**

```python
from google import genai
client = genai.Client()

response = client.models.embed_content(
   model='text-embedding-004',
   contents='Hello world',
)
```

## Tune a Model

Create and use a tuned model.

The new SDK simplifies tuning with `client.tunings.tune`, which launches the
tuning job and polls until the job is complete.

**Before**

```python
import google.generativeai as genai
import random

# create tuning model
train_data = {} 
for i in range(1, 6): 
   key = f'input {i}' 
   value = f'output {i}' 
   train_data[key] = value

name = f'generate-num-{random.randint(0,10000)}'
operation = genai.create_tuned_model(
    source_model='models/gemini-1.5-flash-001-tuning',
    training_data=train_data,
    id = name,
    epoch_count = 5,
    batch_size=4,
    learning_rate=0.001,
)
# wait for tuning complete
tuningProgress = operation.result()

# generate content with the tuned model
model = genai.GenerativeModel(model_name=f'tunedModels/{name}')
response = model.generate_content('55')
```

**After**

```python
from google import genai
from google.genai import types

client = genai.Client()

# Check which models are available for tuning.
for m in client.models.list():
  for action in m.supported_actions:
    if action == "createTunedModel":
      print(m.name) 
      break

# create tuning model
training_dataset=types.TuningDataset(
        examples=[
            types.TuningExample(
                text_input=f'input {i}',
                output=f'output {i}',
            )
            for i in range(5)
        ],
    )
tuning_job = client.tunings.tune(
    base_model='models/gemini-1.5-flash-001-tuning',
    training_dataset=training_dataset,
    config=types.CreateTuningJobConfig(
        epoch_count= 5,
        batch_size=4,
        learning_rate=0.001,
        tuned_model_display_name="test tuned model"
    )
)

# generate content with the tuned model
response = client.models.generate_content(
    model=tuning_job.tuned_model.model,
    contents='55', 
)
```

