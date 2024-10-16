
# google.generativeai.protos.GenerationConfig

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent">
<td>
  <a target="_blank" href="https://github.com/googleapis/google-cloud-python/tree/main/packages/google-ai-generativelanguage/google/ai/generativelanguage_v1beta/types/generative_service.py#L221-L425">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Configuration options for model generation and outputs.

<!-- Placeholder for "Used in" -->
 Not
all parameters are configurable for every model.





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

Optional. The set of character sequences (up to 5) that will
stop output generation. If specified, the API will stop at
the first appearance of a ``stop_sequence``. The stop
sequence will not be included as part of the response.

</td>
</tr><tr>
<td>

`max_output_tokens`<a id="max_output_tokens"></a>

</td>
<td>

`int`

Optional. The maximum number of tokens to include in a
response candidate.

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

The model uses combined Top-k and Top-p (nucleus) sampling.

Tokens are sorted based on their assigned probabilities so
that only the most likely tokens are considered. Top-k
sampling directly limits the maximum number of tokens to
consider, while Nucleus sampling limits the number of tokens
based on the cumulative probability.

Note: The default value varies by ``Model`` and is specified
by the\ <a href="../../../google/generativeai/protos/Model.md#top_p"><code>Model.top_p</code></a> attribute returned from the
``getModel`` function. An empty ``top_k`` attribute
indicates that the model doesn't apply top-k sampling and
doesn't allow setting ``top_k`` on requests.


</td>
</tr><tr>
<td>

`top_k`<a id="top_k"></a>

</td>
<td>

`int`

Optional. The maximum number of tokens to consider when
sampling.

Gemini models use Top-p (nucleus) sampling or a combination
of Top-k and nucleus sampling. Top-k sampling considers the
set of ``top_k`` most probable tokens. Models running with
nucleus sampling don't allow top_k setting.

Note: The default value varies by ``Model`` and is specified
by the\ <a href="../../../google/generativeai/protos/Model.md#top_p"><code>Model.top_p</code></a> attribute returned from the
``getModel`` function. An empty ``top_k`` attribute
indicates that the model doesn't apply top-k sampling and
doesn't allow setting ``top_k`` on requests.


</td>
</tr><tr>
<td>

`response_mime_type`<a id="response_mime_type"></a>

</td>
<td>

`str`

Optional. MIME type of the generated candidate text.
Supported MIME types are: ``text/plain``: (default) Text
output. ``application/json``: JSON response in the response
candidates. ``text/x.enum``: ENUM as a string response in
the response candidates. Refer to the
`docs <https://ai.google.dev/gemini-api/docs/prompting_with_media#plain_text_formats>`__
for a list of all supported text MIME types.

</td>
</tr><tr>
<td>

`response_schema`<a id="response_schema"></a>

</td>
<td>

`google.ai.generativelanguage.Schema`

Optional. Output schema of the generated candidate text.
Schemas must be a subset of the `OpenAPI
schema <https://spec.openapis.org/oas/v3.0.3#schema>`__ and
can be objects, primitives or arrays.

If set, a compatible ``response_mime_type`` must also be
set. Compatible MIME types: ``application/json``: Schema for
JSON response. Refer to the `JSON text generation
guide <https://ai.google.dev/gemini-api/docs/json-mode>`__
for more details.

</td>
</tr><tr>
<td>

`presence_penalty`<a id="presence_penalty"></a>

</td>
<td>

`float`

Optional. Presence penalty applied to the next token's
logprobs if the token has already been seen in the response.

This penalty is binary on/off and not dependant on the
number of times the token is used (after the first). Use
[frequency_penalty][google.ai.generativelanguage.v1beta.GenerationConfig.frequency_penalty]
for a penalty that increases with each use.

A positive penalty will discourage the use of tokens that
have already been used in the response, increasing the
vocabulary.

A negative penalty will encourage the use of tokens that
have already been used in the response, decreasing the
vocabulary.


</td>
</tr><tr>
<td>

`frequency_penalty`<a id="frequency_penalty"></a>

</td>
<td>

`float`

Optional. Frequency penalty applied to the next token's
logprobs, multiplied by the number of times each token has
been seen in the respponse so far.

A positive penalty will discourage the use of tokens that
have already been used, proportional to the number of times
the token has been used: The more a token is used, the more
dificult it is for the model to use that token again
increasing the vocabulary of responses.

Caution: A *negative* penalty will encourage the model to
reuse tokens proportional to the number of times the token
has been used. Small negative values will reduce the
vocabulary of a response. Larger negative values will cause
the model to start repeating a common token until it hits
the
[max_output_tokens][google.ai.generativelanguage.v1beta.GenerationConfig.max_output_tokens]
limit: "...the the the the the...".


</td>
</tr><tr>
<td>

`response_logprobs`<a id="response_logprobs"></a>

</td>
<td>

`bool`

Optional. If true, export the logprobs
results in response.


</td>
</tr><tr>
<td>

`logprobs`<a id="logprobs"></a>

</td>
<td>

`int`

Optional. Only valid if
[response_logprobs=True][google.ai.generativelanguage.v1beta.GenerationConfig.response_logprobs].
This sets the number of top logprobs to return at each
decoding step in the
[Candidate.logprobs_result][google.ai.generativelanguage.v1beta.Candidate.logprobs_result].

This field is a member of `oneof`_ ``_logprobs``.

</td>
</tr>
</table>



