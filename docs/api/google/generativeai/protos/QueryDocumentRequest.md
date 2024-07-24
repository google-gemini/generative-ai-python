description: Request for querying a Document.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="google.generativeai.protos.QueryDocumentRequest" />
<meta itemprop="path" content="Stable" />
</div>

# google.generativeai.protos.QueryDocumentRequest

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/googleapis/google-cloud-python/tree/main/packages/google-ai-generativelanguage/google/ai/generativelanguage_v1beta/types/retriever_service.py#L455-L519">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Request for querying a ``Document``.

<!-- Placeholder for "Used in" -->




<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`name`<a id="name"></a>
</td>
<td>
`str`

Required. The name of the ``Document`` to query. Example:
``corpora/my-corpus-123/documents/the-doc-abc``
</td>
</tr><tr>
<td>
`query`<a id="query"></a>
</td>
<td>
`str`

Required. Query string to perform semantic
search.
</td>
</tr><tr>
<td>
`results_count`<a id="results_count"></a>
</td>
<td>
`int`

Optional. The maximum number of ``Chunk``\ s to return. The
service may return fewer ``Chunk``\ s.

If unspecified, at most 10 ``Chunk``\ s will be returned.
The maximum specified result count is 100.
</td>
</tr><tr>
<td>
`metadata_filters`<a id="metadata_filters"></a>
</td>
<td>
`MutableSequence[google.ai.generativelanguage.MetadataFilter]`

Optional. Filter for ``Chunk`` metadata. Each
``MetadataFilter`` object should correspond to a unique key.
Multiple ``MetadataFilter`` objects are joined by logical
"AND"s.

Note: ``Document``-level filtering is not supported for this
request because a ``Document`` name is already specified.

Example query: (year >= 2020 OR year < 2010) AND (genre =
drama OR genre = action)

``MetadataFilter`` object list: metadata_filters = [ {key =
"chunk.custom_metadata.year" conditions = [{int_value =
2020, operation = GREATER_EQUAL}, {int_value = 2010,
operation = LESS}}, {key = "chunk.custom_metadata.genre"
conditions = [{string_value = "drama", operation = EQUAL},
{string_value = "action", operation = EQUAL}}]

Example query for a numeric range of values: (year > 2015
AND year <= 2020)

``MetadataFilter`` object list: metadata_filters = [ {key =
"chunk.custom_metadata.year" conditions = [{int_value =
2015, operation = GREATER}]}, {key =
"chunk.custom_metadata.year" conditions = [{int_value =
2020, operation = LESS_EQUAL}]}]

Note: "AND"s for the same key are only supported for numeric
values. String values only support "OR"s for the same key.
</td>
</tr>
</table>



