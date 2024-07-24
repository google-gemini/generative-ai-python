description: Request to generate a text completion response from the model.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="google.generativeai.protos.GenerateTextRequest" />
<meta itemprop="path" content="Stable" />
</div>

# google.generativeai.protos.GenerateTextRequest

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/googleapis/google-cloud-python/tree/main/packages/google-ai-generativelanguage/google/ai/generativelanguage_v1beta/types/text_service.py#L42-L185">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Request to generate a text completion response from the model.

<!-- Placeholder for "Used in" -->





<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`model`<a id="model"></a>
</td>
<td>
`str`

Required. The name of the ``Model`` or ``TunedModel`` to use
for generating the completion. Examples:
models/text-bison-001 tunedModels/sentence-translator-u3b7m
</td>
</tr><tr>
<td>
`prompt`<a id="prompt"></a>
</td>
<td>
`google.ai.generativelanguage.TextPrompt`

Required. The free-form input text given to
the model as a prompt.
Given a prompt, the model will generate a
TextCompletion response it predicts as the
completion of the input text.
</td>
</tr><tr>
<td>
`temperature`<a id="temperature"></a>
</td>
<td>
`float`

Optional. Controls the randomness of the output. Note: The
default value varies by model, see the <a href="../../../google/generativeai/protos/Model.md#temperature"><code>Model.temperature</code></a>
attribute of the ``Model`` returned the ``getModel``
function.

Values can range from [0.0,1.0], inclusive. A value closer
to 1.0 will produce responses that are more varied and
creative, while a value closer to 0.0 will typically result
in more straightforward responses from the model.

</td>
</tr><tr>
<td>
`candidate_count`<a id="candidate_count"></a>
</td>
<td>
`int`

Optional. Number of generated responses to return.

This value must be between [1, 8], inclusive. If unset, this
will default to 1.

</td>
</tr><tr>
<td>
`max_output_tokens`<a id="max_output_tokens"></a>
</td>
<td>
`int`

Optional. The maximum number of tokens to include in a
candidate.

If unset, this will default to output_token_limit specified
in the ``Model`` specification.

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
<a href="../../../google/generativeai/protos/Model.md#top_p"><code>Model.top_p</code></a> attribute of the ``Model`` returned the
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

The model uses combined Top-k and nucleus sampling.

Top-k sampling considers the set of ``top_k`` most probable
tokens. Defaults to 40.

Note: The default value varies by model, see the
<a href="../../../google/generativeai/protos/Model.md#top_k"><code>Model.top_k</code></a> attribute of the ``Model`` returned the
``getModel`` function.

</td>
</tr><tr>
<td>
`safety_settings`<a id="safety_settings"></a>
</td>
<td>
`MutableSequence[google.ai.generativelanguage.SafetySetting]`

Optional. A list of unique ``SafetySetting`` instances for
blocking unsafe content.

that will be enforced on the <a href="../../../google/generativeai/protos/GenerateTextRequest.md#prompt"><code>GenerateTextRequest.prompt</code></a>
and <a href="../../../google/generativeai/protos/GenerateTextResponse.md#candidates"><code>GenerateTextResponse.candidates</code></a>. There should not be
more than one setting for each ``SafetyCategory`` type. The
API will block any prompts and responses that fail to meet
the thresholds set by these settings. This list overrides
the default settings for each ``SafetyCategory`` specified
in the safety_settings. If there is no ``SafetySetting`` for
a given ``SafetyCategory`` provided in the list, the API
will use the default safety setting for that category. Harm
categories HARM_CATEGORY_DEROGATORY, HARM_CATEGORY_TOXICITY,
HARM_CATEGORY_VIOLENCE, HARM_CATEGORY_SEXUAL,
HARM_CATEGORY_MEDICAL, HARM_CATEGORY_DANGEROUS are supported
in text service.
</td>
</tr><tr>
<td>
`stop_sequences`<a id="stop_sequences"></a>
</td>
<td>
`MutableSequence[str]`

The set of character sequences (up to 5) that
will stop output generation. If specified, the
API will stop at the first appearance of a stop
sequence. The stop sequence will not be included
as part of the response.
</td>
</tr>
</table>



