description: A simple dataclass used to configure the generation parameters of <a href="../../../google/generativeai/GenerativeModel.md#generate_content"><code>GenerativeModel.generate_content</code></a>.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="google.generativeai.types.GenerationConfig" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__eq__"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="candidate_count"/>
<meta itemprop="property" content="max_output_tokens"/>
<meta itemprop="property" content="response_mime_type"/>
<meta itemprop="property" content="response_schema"/>
<meta itemprop="property" content="stop_sequences"/>
<meta itemprop="property" content="temperature"/>
<meta itemprop="property" content="top_k"/>
<meta itemprop="property" content="top_p"/>
</div>

# google.generativeai.types.GenerationConfig

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/google/generative-ai-python/blob/master/google/generativeai/types/generation_types.py#L91-L168">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



A simple dataclass used to configure the generation parameters of <a href="../../../google/generativeai/GenerativeModel.md#generate_content"><code>GenerativeModel.generate_content</code></a>.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Main aliases</b>
<p>`google.generativeai.GenerationConfig`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>google.generativeai.types.GenerationConfig(
    candidate_count: (int | None) = None,
    stop_sequences: (Iterable[str] | None) = None,
    max_output_tokens: (int | None) = None,
    temperature: (float | None) = None,
    top_p: (float | None) = None,
    top_k: (int | None) = None,
    response_mime_type: (str | None) = None,
    response_schema: (protos.Schema | Mapping[str, Any] | None) = None
)
</code></pre>



<!-- Placeholder for "Used in" -->




<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`candidate_count`<a id="candidate_count"></a>
</td>
<td>
    Number of generated responses to return.
</td>
</tr><tr>
<td>
`stop_sequences`<a id="stop_sequences"></a>
</td>
<td>
    The set of character sequences (up
to 5) that will stop output generation. If
specified, the API will stop at the first
appearance of a stop sequence. The stop sequence
will not be included as part of the response.
</td>
</tr><tr>
<td>
`max_output_tokens`<a id="max_output_tokens"></a>
</td>
<td>
    The maximum number of tokens to include in a
candidate.

If unset, this will default to output_token_limit specified
in the model's specification.
</td>
</tr><tr>
<td>
`temperature`<a id="temperature"></a>
</td>
<td>
    Controls the randomness of the output. Note: The
default value varies by model, see the <a href="../../../google/generativeai/protos/Model.md#temperature"><code>Model.temperature</code></a>
attribute of the `Model` returned the `genai.get_model`
function.

Values can range from [0.0,1.0], inclusive. A value closer
to 1.0 will produce responses that are more varied and
creative, while a value closer to 0.0 will typically result
in more straightforward responses from the model.
</td>
</tr><tr>
<td>
`top_p`<a id="top_p"></a>
</td>
<td>
    Optional. The maximum cumulative probability of tokens to
consider when sampling.

The model uses combined Top-k and nucleus sampling.

Tokens are sorted based on their assigned probabilities so
that only the most likely tokens are considered. Top-k
sampling directly limits the maximum number of tokens to
consider, while Nucleus sampling limits number of tokens
based on the cumulative probability.

Note: The default value varies by model, see the
<a href="../../../google/generativeai/protos/Model.md#top_p"><code>Model.top_p</code></a> attribute of the `Model` returned the
`genai.get_model` function.
</td>
</tr><tr>
<td>
`top_k`<a id="top_k"></a>
</td>
<td>
`int`

Optional. The maximum number of tokens to consider when
sampling.

The model uses combined Top-k and nucleus sampling.

Top-k sampling considers the set of `top_k` most probable
tokens. Defaults to 40.

Note: The default value varies by model, see the
<a href="../../../google/generativeai/protos/Model.md#top_k"><code>Model.top_k</code></a> attribute of the `Model` returned the
`genai.get_model` function.
</td>
</tr><tr>
<td>
`response_mime_type`<a id="response_mime_type"></a>
</td>
<td>
    Optional. Output response mimetype of the generated candidate text.

Supported mimetype:
    `text/plain`: (default) Text output.
    `application/json`: JSON response in the candidates.
</td>
</tr><tr>
<td>
`response_schema`<a id="response_schema"></a>
</td>
<td>
    Optional. Specifies the format of the JSON requested if response_mime_type is
`application/json`.
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
candidate_count<a id="candidate_count"></a>
</td>
<td>
`None`
</td>
</tr><tr>
<td>
max_output_tokens<a id="max_output_tokens"></a>
</td>
<td>
`None`
</td>
</tr><tr>
<td>
response_mime_type<a id="response_mime_type"></a>
</td>
<td>
`None`
</td>
</tr><tr>
<td>
response_schema<a id="response_schema"></a>
</td>
<td>
`None`
</td>
</tr><tr>
<td>
stop_sequences<a id="stop_sequences"></a>
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

