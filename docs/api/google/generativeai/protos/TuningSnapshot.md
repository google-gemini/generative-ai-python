description: Record for a single tuning step.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="google.generativeai.protos.TuningSnapshot" />
<meta itemprop="path" content="Stable" />
</div>

# google.generativeai.protos.TuningSnapshot

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/googleapis/google-cloud-python/tree/main/packages/google-ai-generativelanguage/google/ai/generativelanguage_v1beta/types/tuned_model.py#L396-L428">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Record for a single tuning step.

<!-- Placeholder for "Used in" -->




<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`step`<a id="step"></a>
</td>
<td>
`int`

Output only. The tuning step.
</td>
</tr><tr>
<td>
`epoch`<a id="epoch"></a>
</td>
<td>
`int`

Output only. The epoch this step was part of.
</td>
</tr><tr>
<td>
`mean_loss`<a id="mean_loss"></a>
</td>
<td>
`float`

Output only. The mean loss of the training
examples for this step.
</td>
</tr><tr>
<td>
`compute_time`<a id="compute_time"></a>
</td>
<td>
`google.protobuf.timestamp_pb2.Timestamp`

Output only. The timestamp when this metric
was computed.
</td>
</tr>
</table>



