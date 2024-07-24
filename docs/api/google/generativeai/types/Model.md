description: A dataclass representation of a <a href="../../../google/generativeai/protos/Model.md"><code>protos.Model</code></a>.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="google.generativeai.types.Model" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__eq__"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="max_temperature"/>
<meta itemprop="property" content="temperature"/>
<meta itemprop="property" content="top_k"/>
<meta itemprop="property" content="top_p"/>
</div>

# google.generativeai.types.Model

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/google/generative-ai-python/blob/master/google/generativeai/types/model_types.py#L91-L122">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



A dataclass representation of a <a href="../../../google/generativeai/protos/Model.md"><code>protos.Model</code></a>.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>google.generativeai.types.Model(
    name: str,
    base_model_id: str,
    version: str,
    display_name: str,
    description: str,
    input_token_limit: int,
    output_token_limit: int,
    supported_generation_methods: list[str],
    temperature: (float | None) = None,
    max_temperature: (float | None) = None,
    top_p: (float | None) = None,
    top_k: (int | None) = None
)
</code></pre>



<!-- Placeholder for "Used in" -->




<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`name`<a id="name"></a>
</td>
<td>
The resource name of the `Model`. Format: `models/{model}` with a `{model}` naming
convention of: "{base_model_id}-{version}". For example: `models/chat-bison-001`.
</td>
</tr><tr>
<td>
`base_model_id`<a id="base_model_id"></a>
</td>
<td>
The base name of the model. For example: `chat-bison`.
</td>
</tr><tr>
<td>
`version`<a id="version"></a>
</td>
<td>
 The major version number of the model. For example: `001`.
</td>
</tr><tr>
<td>
`display_name`<a id="display_name"></a>
</td>
<td>
The human-readable name of the model. E.g. `"Chat Bison"`. The name can be up
to 128 characters long and can consist of any UTF-8 characters.
</td>
</tr><tr>
<td>
`description`<a id="description"></a>
</td>
<td>
A short description of the model.
</td>
</tr><tr>
<td>
`input_token_limit`<a id="input_token_limit"></a>
</td>
<td>
Maximum number of input tokens allowed for this model.
</td>
</tr><tr>
<td>
`output_token_limit`<a id="output_token_limit"></a>
</td>
<td>
Maximum number of output tokens available for this model.
</td>
</tr><tr>
<td>
`supported_generation_methods`<a id="supported_generation_methods"></a>
</td>
<td>
lists which methods are supported by the model. The method
names are defined as Pascal case strings, such as `generateMessage` which correspond to
API methods.
</td>
</tr><tr>
<td>
`temperature`<a id="temperature"></a>
</td>
<td>
Dataclass field
</td>
</tr><tr>
<td>
`max_temperature`<a id="max_temperature"></a>
</td>
<td>
Dataclass field
</td>
</tr><tr>
<td>
`top_p`<a id="top_p"></a>
</td>
<td>
Dataclass field
</td>
</tr><tr>
<td>
`top_k`<a id="top_k"></a>
</td>
<td>
Dataclass field
</td>
</tr>
</table>



## Methods

<h3 id="__eq__"><code>__eq__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__eq__(
    other
)
</code></pre>

Return self==value.






<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Class Variables</h2></th></tr>

<tr>
<td>
max_temperature<a id="max_temperature"></a>
</td>
<td>
`None`
</td>
</tr><tr>
<td>
temperature<a id="temperature"></a>
</td>
<td>
`None`
</td>
</tr><tr>
<td>
top_k<a id="top_k"></a>
</td>
<td>
`None`
</td>
</tr><tr>
<td>
top_p<a id="top_p"></a>
</td>
<td>
`None`
</td>
</tr>
</table>

