description: Metadata about the state and progress of creating a tuned model returned from the long-running operation

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="google.generativeai.protos.CreateTunedModelMetadata" />
<meta itemprop="path" content="Stable" />
</div>

# google.generativeai.protos.CreateTunedModelMetadata

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/googleapis/google-cloud-python/tree/main/packages/google-ai-generativelanguage/google/ai/generativelanguage_v1beta/types/model_service.py#L254-L293">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Metadata about the state and progress of creating a tuned model returned from the long-running operation

<!-- Placeholder for "Used in" -->




<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`tuned_model`<a id="tuned_model"></a>
</td>
<td>
`str`

Name of the tuned model associated with the
tuning operation.
</td>
</tr><tr>
<td>
`total_steps`<a id="total_steps"></a>
</td>
<td>
`int`

The total number of tuning steps.
</td>
</tr><tr>
<td>
`completed_steps`<a id="completed_steps"></a>
</td>
<td>
`int`

The number of steps completed.
</td>
</tr><tr>
<td>
`completed_percent`<a id="completed_percent"></a>
</td>
<td>
`float`

The completed percentage for the tuning
operation.
</td>
</tr><tr>
<td>
`snapshots`<a id="snapshots"></a>
</td>
<td>
`MutableSequence[google.ai.generativelanguage.TuningSnapshot]`

Metrics collected during tuning.
</td>
</tr>
</table>



