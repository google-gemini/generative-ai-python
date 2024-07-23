description: User provided metadata stored as key-value pairs.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="google.generativeai.protos.CustomMetadata" />
<meta itemprop="path" content="Stable" />
</div>

# google.generativeai.protos.CustomMetadata

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/googleapis/google-cloud-python/tree/main/packages/google-ai-generativelanguage/google/ai/generativelanguage_v1beta/types/retriever.py#L155-L202">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



User provided metadata stored as key-value pairs.

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

The string value of the metadata to store.

This field is a member of `oneof`_ ``value``.
</td>
</tr><tr>
<td>
`string_list_value`<a id="string_list_value"></a>
</td>
<td>
`google.ai.generativelanguage.StringList`

The StringList value of the metadata to
store.

This field is a member of `oneof`_ ``value``.
</td>
</tr><tr>
<td>
`numeric_value`<a id="numeric_value"></a>
</td>
<td>
`float`

The numeric value of the metadata to store.

This field is a member of `oneof`_ ``value``.
</td>
</tr><tr>
<td>
`key`<a id="key"></a>
</td>
<td>
`str`

Required. The key of the metadata to store.
</td>
</tr>
</table>



