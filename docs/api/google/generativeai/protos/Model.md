
# google.generativeai.protos.Model

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent">
<td>
  <a target="_blank" href="https://github.com/googleapis/google-cloud-python/tree/main/packages/google-ai-generativelanguage/google/ai/generativelanguage_v1beta/types/model.py#L30-L168">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Information about a Generative Language Model.

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

`str`

Required. The resource name of the ``Model``. Refer to
`Model
variants <https://ai.google.dev/gemini-api/docs/models/gemini#model-variations>`__
for all allowed values.

Format: ``models/{model}`` with a ``{model}`` naming
convention of:

-  "{base_model_id}-{version}"

Examples:

-  ``models/gemini-1.5-flash-001``

</td>
</tr><tr>
<td>

`base_model_id`<a id="base_model_id"></a>

</td>
<td>

`str`

Required. The name of the base model, pass this to the
generation request.

Examples:

-  ``gemini-1.5-flash``

</td>
</tr><tr>
<td>

`version`<a id="version"></a>

</td>
<td>

`str`

Required. The version number of the model.

This represents the major version (``1.0`` or ``1.5``)

</td>
</tr><tr>
<td>

`display_name`<a id="display_name"></a>

</td>
<td>

`str`

The human-readable name of the model. E.g.
"Gemini 1.5 Flash".
The name can be up to 128 characters long and
can consist of any UTF-8 characters.

</td>
</tr><tr>
<td>

`description`<a id="description"></a>

</td>
<td>

`str`

A short description of the model.

</td>
</tr><tr>
<td>

`input_token_limit`<a id="input_token_limit"></a>

</td>
<td>

`int`

Maximum number of input tokens allowed for
this model.

</td>
</tr><tr>
<td>

`output_token_limit`<a id="output_token_limit"></a>

</td>
<td>

`int`

Maximum number of output tokens available for
this model.

</td>
</tr><tr>
<td>

`supported_generation_methods`<a id="supported_generation_methods"></a>

</td>
<td>

`MutableSequence[str]`

The model's supported generation methods.

The corresponding API method names are defined as Pascal
case strings, such as ``generateMessage`` and
``generateContent``.

</td>
</tr><tr>
<td>

`temperature`<a id="temperature"></a>

</td>
<td>

`float`

Controls the randomness of the output.

Values can range over ``[0.0,max_temperature]``, inclusive.
A higher value will produce responses that are more varied,
while a value closer to ``0.0`` will typically result in
less surprising responses from the model. This value
specifies default to be used by the backend while making the
call to the model.


</td>
</tr><tr>
<td>

`max_temperature`<a id="max_temperature"></a>

</td>
<td>

`float`

The maximum temperature this model can use.


</td>
</tr><tr>
<td>

`top_p`<a id="top_p"></a>

</td>
<td>

`float`

For `Nucleus
sampling <https://ai.google.dev/gemini-api/docs/prompting-strategies#top-p>`__.

Nucleus sampling considers the smallest set of tokens whose
probability sum is at least ``top_p``. This value specifies
default to be used by the backend while making the call to
the model.


</td>
</tr><tr>
<td>

`top_k`<a id="top_k"></a>

</td>
<td>

`int`

For Top-k sampling.

Top-k sampling considers the set of ``top_k`` most probable
tokens. This value specifies default to be used by the
backend while making the call to the model. If empty,
indicates the model doesn't use top-k sampling, and
``top_k`` isn't allowed as a generation parameter.


</td>
</tr>
</table>



