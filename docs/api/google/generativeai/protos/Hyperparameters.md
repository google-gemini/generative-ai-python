description: Hyperparameters controlling the tuning process.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="google.generativeai.protos.Hyperparameters" />
<meta itemprop="path" content="Stable" />
</div>

# google.generativeai.protos.Hyperparameters

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/googleapis/google-cloud-python/tree/main/packages/google-ai-generativelanguage/google/ai/generativelanguage_v1beta/types/tuned_model.py#L270-L331">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Hyperparameters controlling the tuning process.

<!-- Placeholder for "Used in" -->
 Read more at
https://ai.google.dev/docs/model_tuning_guidance

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
`learning_rate`<a id="learning_rate"></a>
</td>
<td>
`float`

Optional. Immutable. The learning rate
hyperparameter for tuning. If not set, a default
of 0.001 or 0.0002 will be calculated based on
the number of training examples.

This field is a member of `oneof`_ ``learning_rate_option``.
</td>
</tr><tr>
<td>
`learning_rate_multiplier`<a id="learning_rate_multiplier"></a>
</td>
<td>
`float`

Optional. Immutable. The learning rate multiplier is used to
calculate a final learning_rate based on the default
(recommended) value. Actual learning rate :=
learning_rate_multiplier \* default learning rate Default
learning rate is dependent on base model and dataset size.
If not set, a default of 1.0 will be used.

This field is a member of `oneof`_ ``learning_rate_option``.
</td>
</tr><tr>
<td>
`epoch_count`<a id="epoch_count"></a>
</td>
<td>
`int`

Immutable. The number of training epochs. An
epoch is one pass through the training data. If
not set, a default of 5 will be used.

</td>
</tr><tr>
<td>
`batch_size`<a id="batch_size"></a>
</td>
<td>
`int`

Immutable. The batch size hyperparameter for
tuning. If not set, a default of 4 or 16 will be
used based on the number of training examples.

</td>
</tr>
</table>



