description: All of the structured input text passed to the model as a prompt.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="google.generativeai.protos.MessagePrompt" />
<meta itemprop="path" content="Stable" />
</div>

# google.generativeai.protos.MessagePrompt

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/googleapis/google-cloud-python/tree/main/packages/google-ai-generativelanguage/google/ai/generativelanguage_v1beta/types/discuss_service.py#L214-L277">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



All of the structured input text passed to the model as a prompt.

<!-- Placeholder for "Used in" -->

A ``MessagePrompt`` contains a structured set of fields that provide
context for the conversation, examples of user input/model output
message pairs that prime the model to respond in different ways, and
the conversation history or list of messages representing the
alternating turns of the conversation between the user and the
model.



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`context`<a id="context"></a>
</td>
<td>
`str`

Optional. Text that should be provided to the model first to
ground the response.

If not empty, this ``context`` will be given to the model
first before the ``examples`` and ``messages``. When using a
``context`` be sure to provide it with every request to
maintain continuity.

This field can be a description of your prompt to the model
to help provide context and guide the responses. Examples:
"Translate the phrase from English to French." or "Given a
statement, classify the sentiment as happy, sad or neutral."

Anything included in this field will take precedence over
message history if the total input size exceeds the model's
``input_token_limit`` and the input request is truncated.
</td>
</tr><tr>
<td>
`examples`<a id="examples"></a>
</td>
<td>
`MutableSequence[google.ai.generativelanguage.Example]`

Optional. Examples of what the model should generate.

This includes both user input and the response that the
model should emulate.

These ``examples`` are treated identically to conversation
messages except that they take precedence over the history
in ``messages``: If the total input size exceeds the model's
``input_token_limit`` the input will be truncated. Items
will be dropped from ``messages`` before ``examples``.
</td>
</tr><tr>
<td>
`messages`<a id="messages"></a>
</td>
<td>
`MutableSequence[google.ai.generativelanguage.Message]`

Required. A snapshot of the recent conversation history
sorted chronologically.

Turns alternate between two authors.

If the total input size exceeds the model's
``input_token_limit`` the input will be truncated: The
oldest items will be dropped from ``messages``.
</td>
</tr>
</table>



