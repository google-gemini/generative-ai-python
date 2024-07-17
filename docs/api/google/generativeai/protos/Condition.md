description: Filter condition applicable to a single key.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="google.generativeai.protos.Condition" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="Operator"/>
</div>

# google.generativeai.protos.Condition

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/googleapis/google-cloud-python/tree/main/packages/google-ai-generativelanguage/google/ai/generativelanguage_v1beta/types/retriever.py#L233-L307">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Filter condition applicable to a single key.

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
`string_value`<a id="string_value"></a>
</td>
<td>
`str`

The string value to filter the metadata on.

This field is a member of `oneof`_ ``value``.
</td>
</tr><tr>
<td>
`numeric_value`<a id="numeric_value"></a>
</td>
<td>
`float`

The numeric value to filter the metadata on.

This field is a member of `oneof`_ ``value``.
</td>
</tr><tr>
<td>
`operation`<a id="operation"></a>
</td>
<td>
`google.ai.generativelanguage.Condition.Operator`

Required. Operator applied to the given
key-value pair to trigger the condition.
</td>
</tr>
</table>



## Child Classes
[`class Operator`](../../../google/generativeai/protos/Condition/Operator.md)

