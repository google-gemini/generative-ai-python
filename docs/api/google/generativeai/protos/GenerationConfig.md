description: Configuration options for model generation and outputs.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="google.generativeai.protos.GenerationConfig" />
<meta itemprop="path" content="Stable" />
</div>

# google.generativeai.protos.GenerationConfig

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/googleapis/google-cloud-python/tree/main/packages/google-ai-generativelanguage/google/ai/generativelanguage_v1beta/types/generative_service.py#L199-L325">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Configuration options for model generation and outputs.

<!-- Placeholder for "Used in" -->
 Not
all parameters may be configurable for every model.





<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`candidate_count`<a id="candidate_count"></a>
</td>
<td>
`int`

Optional. Number of generated responses to
return.
Currently, this value can only be set to 1. If
unset, this will default to 1.

</td>
</tr><tr>
<td>
`stop_sequences`<a id="stop_sequences"></a>
</td>
<td>
`MutableSequence[str]`

Optional. The set of character sequences (up
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
`int`

Optional. The maximum number of tokens to include in a
candidate.

Note: The default value varies by model, see the
<a href="../../../google/generativeai/protos/Model.md#output_token_limit"><code>Model.output_token_limit</code></a> attribute of the ``Model``
returned from the ``getModel`` function.

</td>
</tr><tr>
<td>
`temperature`<a id="temperature"></a>
</td>
<td>
`float`

Optional. Controls the randomness of the output.

Note: The default value varies by model, see the
<a href="../../../google/generativeai/protos/Model.md#temperature"><code>Model.temperature</code></a> attribute of the ``Model`` returned
from the ``getModel`` function.

Values can range from [0.0, 2.0].

</td>
</tr><tr>
<td>
`top_p`<a id="top_p"></a>
</td>
<td>
`float`

Optional. The maximum cumulative probability of tokens to
consider when sampling.

The model uses combined Top-k and nucleus sampling.

Tokens are sorted based on their assigned probabilities so
that only the most likely tokens are considered. Top-k
sampling directly limits the maximum number of tokens to
consider, while Nucleus sampling limits number of tokens
based on the cumulative probability.

Note: The default value varies by model, see the
<a href="../../../google/generativeai/protos/Model.md#top_p"><code>Model.top_p</code></a> attribute of the ``Model`` returned from the
``getModel`` function.

</td>
</tr><tr>
<td>
`top_k`<a id="top_k"></a>
</td>
<td>
`int`

Optional. The maximum number of tokens to consider when
sampling.

Models use nucleus sampling or combined Top-k and nucleus
sampling. Top-k sampling considers the set of ``top_k`` most
probable tokens. Models running with nucleus sampling don't
allow top_k setting.

Note: The default value varies by model, see the
<a href="../../../google/generativeai/protos/Model.md#top_k"><code>Model.top_k</code></a> attribute of the ``Model`` returned from the
``getModel`` function. Empty ``top_k`` field in ``Model``
indicates the model doesn't apply top-k sampling and doesn't
allow setting ``top_k`` on requests.

</td>
</tr><tr>
<td>
`response_mime_type`<a id="response_mime_type"></a>
</td>
<td>
`str`

Optional. Output response mimetype of the generated
candidate text. Supported mimetype: ``text/plain``:
(default) Text output. ``application/json``: JSON response
in the candidates.
</td>
</tr><tr>
<td>
`response_schema`<a id="response_schema"></a>
</td>
<td>
`google.ai.generativelanguage.Schema`

Optional. Output response schema of the generated candidate
text when response mime type can have schema. Schema can be
objects, primitives or arrays and is a subset of `OpenAPI
schema <https://spec.openapis.org/oas/v3.0.3#schema>`__.

If set, a compatible response_mime_type must also be set.
Compatible mimetypes: ``application/json``: Schema for JSON
response.
</td>
</tr>
</table>



