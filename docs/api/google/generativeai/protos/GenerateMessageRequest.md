description: Request to generate a message response from the model.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="google.generativeai.protos.GenerateMessageRequest" />
<meta itemprop="path" content="Stable" />
</div>

# google.generativeai.protos.GenerateMessageRequest

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/googleapis/google-cloud-python/tree/main/packages/google-ai-generativelanguage/google/ai/generativelanguage_v1beta/types/discuss_service.py#L38-L121">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Request to generate a message response from the model.

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

Required. The name of the model to use.

Format: ``name=models/{model}``.
</td>
</tr><tr>
<td>
`prompt`<a id="prompt"></a>
</td>
<td>
`google.ai.generativelanguage.MessagePrompt`

Required. The structured textual input given
to the model as a prompt.
Given a
prompt, the model will return what it predicts
is the next message in the discussion.
</td>
</tr><tr>
<td>
`temperature`<a id="temperature"></a>
</td>
<td>
`float`

Optional. Controls the randomness of the output.

Values can range over ``[0.0,1.0]``, inclusive. A value
closer to ``1.0`` will produce responses that are more
varied, while a value closer to ``0.0`` will typically
result in less surprising responses from the model.

</td>
</tr><tr>
<td>
`candidate_count`<a id="candidate_count"></a>
</td>
<td>
`int`

Optional. The number of generated response messages to
return.

This value must be between ``[1, 8]``, inclusive. If unset,
this will default to ``1``.

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

Nucleus sampling considers the smallest set of tokens whose
probability sum is at least ``top_p``.

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
tokens.

</td>
</tr>
</table>



