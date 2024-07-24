description: Instances of this class manage the response of the generate_content method.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="google.generativeai.types.GenerateContentResponse" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__iter__"/>
<meta itemprop="property" content="from_iterator"/>
<meta itemprop="property" content="from_response"/>
<meta itemprop="property" content="resolve"/>
<meta itemprop="property" content="to_dict"/>
</div>

# google.generativeai.types.GenerateContentResponse

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/google/generative-ai-python/blob/master/google/generativeai/types/generation_types.py#L553-L617">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Instances of this class manage the response of the `generate_content` method.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>google.generativeai.types.GenerateContentResponse(
    done: bool,
    iterator: (None | Iterable[protos.GenerateContentResponse] | AsyncIterable[protos.
        GenerateContentResponse]),
    result: protos.GenerateContentResponse,
    chunks: (Iterable[protos.GenerateContentResponse] | None) = None
)
</code></pre>



<!-- Placeholder for "Used in" -->

These are returned by <a href="../../../google/generativeai/GenerativeModel.md#generate_content"><code>GenerativeModel.generate_content</code></a> and <a href="../../../google/generativeai/ChatSession.md#send_message"><code>ChatSession.send_message</code></a>.
This object is based on the low level <a href="../../../google/generativeai/protos/GenerateContentResponse.md"><code>protos.GenerateContentResponse</code></a> class which just has `prompt_feedback`
and `candidates` attributes. This class adds several quick accessors for common use cases.

The same object type is returned for both `stream=True/False`.

### Streaming

When you pass `stream=True` to <a href="../../../google/generativeai/GenerativeModel.md#generate_content"><code>GenerativeModel.generate_content</code></a> or <a href="../../../google/generativeai/ChatSession.md#send_message"><code>ChatSession.send_message</code></a>,
iterate over this object to receive chunks of the response:

```
response = model.generate_content(..., stream=True):
for chunk in response:
  print(chunk.text)
```

<a href="../../../google/generativeai/protos/GenerateContentResponse.md#prompt_feedback"><code>GenerateContentResponse.prompt_feedback</code></a> is available immediately but
<a href="../../../google/generativeai/protos/GenerateContentResponse.md#candidates"><code>GenerateContentResponse.candidates</code></a>, and all the attributes derived from them (`.text`, `.parts`),
are only available after the iteration is complete.



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`candidates`<a id="candidates"></a>
</td>
<td>
The list of candidate responses.
</td>
</tr><tr>
<td>
`parts`<a id="parts"></a>
</td>
<td>
A quick accessor equivalent to `self.candidates[0].content.parts`
</td>
</tr><tr>
<td>
`prompt_feedback`<a id="prompt_feedback"></a>
</td>
<td>

</td>
</tr><tr>
<td>
`text`<a id="text"></a>
</td>
<td>
A quick accessor equivalent to `self.candidates[0].content.parts[0].text`
</td>
</tr><tr>
<td>
`usage_metadata`<a id="usage_metadata"></a>
</td>
<td>

</td>
</tr>
</table>



## Methods

<h3 id="from_iterator"><code>from_iterator</code></h3>

<a target="_blank" class="external" href="https://github.com/google/generative-ai-python/blob/master/google/generativeai/types/generation_types.py#L555-L565">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@classmethod</code>
<code>from_iterator(
    iterator: Iterable[protos.GenerateContentResponse]
)
</code></pre>




<h3 id="from_response"><code>from_response</code></h3>

<a target="_blank" class="external" href="https://github.com/google/generative-ai-python/blob/master/google/generativeai/types/generation_types.py#L567-L573">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@classmethod</code>
<code>from_response(
    response: protos.GenerateContentResponse
)
</code></pre>




<h3 id="resolve"><code>resolve</code></h3>

<a target="_blank" class="external" href="https://github.com/google/generative-ai-python/blob/master/google/generativeai/types/generation_types.py#L612-L617">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>resolve()
</code></pre>




<h3 id="to_dict"><code>to_dict</code></h3>

<a target="_blank" class="external" href="https://github.com/google/generative-ai-python/blob/master/google/generativeai/types/generation_types.py#L383-L393">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>to_dict()
</code></pre>

Returns the result as a JSON-compatible dict.

Note: This doesn't capture the iterator state when streaming, it only captures the accumulated
`GenerateContentResponse` fields.

```
>>> import json
>>> response = model.generate_content('Hello?')
>>> json.dumps(response.to_dict())
```

<h3 id="__iter__"><code>__iter__</code></h3>

<a target="_blank" class="external" href="https://github.com/google/generative-ai-python/blob/master/google/generativeai/types/generation_types.py#L575-L610">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__iter__()
</code></pre>






