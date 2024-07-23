description: A set of tuning examples. Can be training or validation data.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="google.generativeai.protos.TuningExamples" />
<meta itemprop="path" content="Stable" />
</div>

# google.generativeai.protos.TuningExamples

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/googleapis/google-cloud-python/tree/main/packages/google-ai-generativelanguage/google/ai/generativelanguage_v1beta/types/tuned_model.py#L354-L368">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



A set of tuning examples. Can be training or validation data.

<!-- Placeholder for "Used in" -->




<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`examples`<a id="examples"></a>
</td>
<td>
`MutableSequence[google.ai.generativelanguage.TuningExample]`

Required. The examples. Example input can be
for text or discuss, but all examples in a set
must be of the same type.
</td>
</tr>
</table>



