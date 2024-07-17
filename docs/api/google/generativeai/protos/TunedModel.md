description: A fine-tuned model created using ModelService.CreateTunedModel.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="google.generativeai.protos.TunedModel" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="State"/>
</div>

# google.generativeai.protos.TunedModel

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/googleapis/google-cloud-python/tree/main/packages/google-ai-generativelanguage/google/ai/generativelanguage_v1beta/types/tuned_model.py#L38-L195">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



A fine-tuned model created using ModelService.CreateTunedModel.

<!-- Placeholder for "Used in" -->

This message has `oneof`_ fields (mutually exclusive fields).
For each oneof, at most one member field can be set at the same time.
Setting any member of the oneof automatically clears all other
members.




<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`tuned_model_source`<a id="tuned_model_source"></a>
</td>
<td>
`google.ai.generativelanguage.TunedModelSource`

Optional. TunedModel to use as the starting
point for training the new model.

This field is a member of `oneof`_ ``source_model``.
</td>
</tr><tr>
<td>
`base_model`<a id="base_model"></a>
</td>
<td>
`str`

Immutable. The name of the ``Model`` to tune. Example:
``models/text-bison-001``

This field is a member of `oneof`_ ``source_model``.
</td>
</tr><tr>
<td>
`name`<a id="name"></a>
</td>
<td>
`str`

Output only. The tuned model name. A unique name will be
generated on create. Example: ``tunedModels/az2mb0bpw6i`` If
display_name is set on create, the id portion of the name
will be set by concatenating the words of the display_name
with hyphens and adding a random portion for uniqueness.
Example: display_name = "Sentence Translator" name =
"tunedModels/sentence-translator-u3b7m".
</td>
</tr><tr>
<td>
`display_name`<a id="display_name"></a>
</td>
<td>
`str`

Optional. The name to display for this model
in user interfaces. The display name must be up
to 40 characters including spaces.
</td>
</tr><tr>
<td>
`description`<a id="description"></a>
</td>
<td>
`str`

Optional. A short description of this model.
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

This value specifies default to be the one used by the base
model while creating the model.

</td>
</tr><tr>
<td>
`top_p`<a id="top_p"></a>
</td>
<td>
`float`

Optional. For Nucleus sampling.

Nucleus sampling considers the smallest set of tokens whose
probability sum is at least ``top_p``.

This value specifies default to be the one used by the base
model while creating the model.

</td>
</tr><tr>
<td>
`top_k`<a id="top_k"></a>
</td>
<td>
`int`

Optional. For Top-k sampling.

Top-k sampling considers the set of ``top_k`` most probable
tokens. This value specifies default to be used by the
backend while making the call to the model.

This value specifies default to be the one used by the base
model while creating the model.

</td>
</tr><tr>
<td>
`state`<a id="state"></a>
</td>
<td>
`google.ai.generativelanguage.TunedModel.State`

Output only. The state of the tuned model.
</td>
</tr><tr>
<td>
`create_time`<a id="create_time"></a>
</td>
<td>
`google.protobuf.timestamp_pb2.Timestamp`

Output only. The timestamp when this model
was created.
</td>
</tr><tr>
<td>
`update_time`<a id="update_time"></a>
</td>
<td>
`google.protobuf.timestamp_pb2.Timestamp`

Output only. The timestamp when this model
was updated.
</td>
</tr><tr>
<td>
`tuning_task`<a id="tuning_task"></a>
</td>
<td>
`google.ai.generativelanguage.TuningTask`

Required. The tuning task that creates the
tuned model.
</td>
</tr>
</table>



## Child Classes
[`class State`](../../../google/generativeai/types/TunedModelState.md)

