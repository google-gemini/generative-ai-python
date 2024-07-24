description: User provided filter to limit retrieval based on Chunk or Document level metadata values.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="google.generativeai.protos.MetadataFilter" />
<meta itemprop="path" content="Stable" />
</div>

# google.generativeai.protos.MetadataFilter

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/googleapis/google-cloud-python/tree/main/packages/google-ai-generativelanguage/google/ai/generativelanguage_v1beta/types/retriever.py#L205-L230">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



User provided filter to limit retrieval based on ``Chunk`` or ``Document`` level metadata values.

<!-- Placeholder for "Used in" -->
 Example (genre = drama OR genre
= action): key = "document.custom_metadata.genre" conditions =
[{string_value = "drama", operation = EQUAL}, {string_value =
"action", operation = EQUAL}]



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`key`<a id="key"></a>
</td>
<td>
`str`

Required. The key of the metadata to filter
on.
</td>
</tr><tr>
<td>
`conditions`<a id="conditions"></a>
</td>
<td>
`MutableSequence[google.ai.generativelanguage.Condition]`

Required. The ``Condition``\ s for the given key that will
trigger this filter. Multiple ``Condition``\ s are joined by
logical ORs.
</td>
</tr>
</table>



