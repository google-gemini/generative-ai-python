description: Contains an ongoing conversation with the model.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="google.generativeai.ChatSession" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="rewind"/>
<meta itemprop="property" content="send_message"/>
<meta itemprop="property" content="send_message_async"/>
</div>

# google.generativeai.ChatSession

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/google/generative-ai-python/blob/master/google/generativeai/generative_models.py#L481-L875">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Contains an ongoing conversation with the model.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>google.generativeai.ChatSession(
    model: GenerativeModel,
    history: (Iterable[content_types.StrictContentType] | None) = None,
    enable_automatic_function_calling: bool = False
)
</code></pre>



<!-- Placeholder for "Used in" -->

```
>>> model = genai.GenerativeModel('models/gemini-pro')
>>> chat = model.start_chat()
>>> response = chat.send_message("Hello")
>>> print(response.text)
>>> response = chat.send_message("Hello again")
>>> print(response.text)
>>> response = chat.send_message(...
```

This `ChatSession` object collects the messages sent and received, in its
<a href="../../google/generativeai/ChatSession.md#history"><code>ChatSession.history</code></a> attribute.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Arguments</h2></th></tr>

<tr>
<td>
`model`<a id="model"></a>
</td>
<td>
The model to use in the chat.
</td>
</tr><tr>
<td>
`history`<a id="history"></a>
</td>
<td>
A chat history to initialize the object with.
</td>
</tr>
</table>





<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`history`<a id="history"></a>
</td>
<td>
The chat history.
</td>
</tr><tr>
<td>
`last`<a id="last"></a>
</td>
<td>
returns the last received `genai.GenerateContentResponse`
</td>
</tr>
</table>



## Methods

<h3 id="rewind"><code>rewind</code></h3>

<a target="_blank" class="external" href="https://github.com/google/generative-ai-python/blob/master/google/generativeai/generative_models.py#L785-L794">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>rewind() -> tuple[protos.Content, protos.Content]
</code></pre>

Removes the last request/response pair from the chat history.


<h3 id="send_message"><code>send_message</code></h3>

<a target="_blank" class="external" href="https://github.com/google/generative-ai-python/blob/master/google/generativeai/generative_models.py#L512-L604">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>send_message(
    content: content_types.ContentType,
    *,
    generation_config: generation_types.GenerationConfigType = None,
    safety_settings: safety_types.SafetySettingOptions = None,
    stream: bool = False,
    tools: (content_types.FunctionLibraryType | None) = None,
    tool_config: (content_types.ToolConfigType | None) = None,
    request_options: (helper_types.RequestOptionsType | None) = None
) -> generation_types.GenerateContentResponse
</code></pre>

Sends the conversation history with the added message and returns the model's response.

Appends the request and response to the conversation history.

```
>>> model = genai.GenerativeModel('models/gemini-pro')
>>> chat = model.start_chat()
>>> response = chat.send_message("Hello")
>>> print(response.text)
"Hello! How can I assist you today?"
>>> len(chat.history)
2
```

Call it with `stream=True` to receive response chunks as they are generated:

```
>>> chat = model.start_chat()
>>> response = chat.send_message("Explain quantum physics", stream=True)
>>> for chunk in response:
...   print(chunk.text, end='')
```

Once iteration over chunks is complete, the `response` and `ChatSession` are in states identical to the
`stream=False` case. Some properties are not available until iteration is complete.

Like <a href="../../google/generativeai/GenerativeModel.md#generate_content"><code>GenerativeModel.generate_content</code></a> this method lets you override the model's `generation_config` and
`safety_settings`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Arguments</th></tr>

<tr>
<td>
`content`
</td>
<td>
The message contents.
</td>
</tr><tr>
<td>
`generation_config`
</td>
<td>
Overrides for the model's generation config.
</td>
</tr><tr>
<td>
`safety_settings`
</td>
<td>
Overrides for the model's safety settings.
</td>
</tr><tr>
<td>
`stream`
</td>
<td>
If True, yield response chunks as they are generated.
</td>
</tr>
</table>



<h3 id="send_message_async"><code>send_message_async</code></h3>

<a target="_blank" class="external" href="https://github.com/google/generative-ai-python/blob/master/google/generativeai/generative_models.py#L671-L733">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>send_message_async(
    content,
    *,
    generation_config=None,
    safety_settings=None,
    stream=False,
    tools=None,
    tool_config=None,
    request_options=None
)
</code></pre>

The async version of <a href="../../google/generativeai/ChatSession.md#send_message"><code>ChatSession.send_message</code></a>.




