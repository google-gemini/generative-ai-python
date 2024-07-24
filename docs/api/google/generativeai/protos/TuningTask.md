description: Tuning tasks that create tuned models.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="google.generativeai.protos.TuningTask" />
<meta itemprop="path" content="Stable" />
</div>

# google.generativeai.protos.TuningTask

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/googleapis/google-cloud-python/tree/main/packages/google-ai-generativelanguage/google/ai/generativelanguage_v1beta/types/tuned_model.py#L222-L267">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Tuning tasks that create tuned models.

<!-- Placeholder for "Used in" -->




<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`start_time`<a id="start_time"></a>
</td>
<td>
`google.protobuf.timestamp_pb2.Timestamp`

Output only. The timestamp when tuning this
model started.
</td>
</tr><tr>
<td>
`complete_time`<a id="complete_time"></a>
</td>
<td>
`google.protobuf.timestamp_pb2.Timestamp`

Output only. The timestamp when tuning this
model completed.
</td>
</tr><tr>
<td>
`snapshots`<a id="snapshots"></a>
</td>
<td>
`MutableSequence[google.ai.generativelanguage.TuningSnapshot]`

Output only. Metrics collected during tuning.
</td>
</tr><tr>
<td>
`training_data`<a id="training_data"></a>
</td>
<td>
`google.ai.generativelanguage.Dataset`

Required. Input only. Immutable. The model
training data.
</td>
</tr><tr>
<td>
`hyperparameters`<a id="hyperparameters"></a>
</td>
<td>
`google.ai.generativelanguage.Hyperparameters`

Immutable. Hyperparameters controlling the
tuning process. If not provided, default values
will be used.
</td>
</tr>
</table>



