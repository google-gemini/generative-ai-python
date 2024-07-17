description: Configuration for retrieving grounding content from a Corpus or Document created using the Semantic Retriever API.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="google.generativeai.protos.SemanticRetrieverConfig" />
<meta itemprop="path" content="Stable" />
</div>

# google.generativeai.protos.SemanticRetrieverConfig

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/googleapis/google-cloud-python/tree/main/packages/google-ai-generativelanguage/google/ai/generativelanguage_v1beta/types/generative_service.py#L328-L380">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Configuration for retrieving grounding content from a ``Corpus`` or ``Document`` created using the Semantic Retriever API.

<!-- Placeholder for "Used in" -->





<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`source`<a id="source"></a>
</td>
<td>
`str`

Required. Name of the resource for retrieval,
e.g. corpora/123 or corpora/123/documents/abc.
</td>
</tr><tr>
<td>
`query`<a id="query"></a>
</td>
<td>
`google.ai.generativelanguage.Content`

Required. Query to use for similarity matching ``Chunk``\ s
in the given resource.
</td>
</tr><tr>
<td>
`metadata_filters`<a id="metadata_filters"></a>
</td>
<td>
`MutableSequence[google.ai.generativelanguage.MetadataFilter]`

Optional. Filters for selecting ``Document``\ s and/or
``Chunk``\ s from the resource.
</td>
</tr><tr>
<td>
`max_chunks_count`<a id="max_chunks_count"></a>
</td>
<td>
`int`

Optional. Maximum number of relevant ``Chunk``\ s to
retrieve.

</td>
</tr><tr>
<td>
`minimum_relevance_score`<a id="minimum_relevance_score"></a>
</td>
<td>
`float`

Optional. Minimum relevance score for retrieved relevant
``Chunk``\ s.

</td>
</tr>
</table>



