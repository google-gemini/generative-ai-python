description: Response from ListChunks containing a paginated list of Chunk\ s.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="google.generativeai.protos.ListChunksResponse" />
<meta itemprop="path" content="Stable" />
</div>

# google.generativeai.protos.ListChunksResponse

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/googleapis/google-cloud-python/tree/main/packages/google-ai-generativelanguage/google/ai/generativelanguage_v1beta/types/retriever_service.py#L764-L790">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Response from ``ListChunks`` containing a paginated list of ``Chunk``\ s.

<!-- Placeholder for "Used in" -->
 The ``Chunk``\ s are sorted by ascending
``chunk.create_time``.



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`chunks`<a id="chunks"></a>
</td>
<td>
`MutableSequence[google.ai.generativelanguage.Chunk]`

The returned ``Chunk``\ s.
</td>
</tr><tr>
<td>
`next_page_token`<a id="next_page_token"></a>
</td>
<td>
`str`

A token, which can be sent as ``page_token`` to retrieve the
next page. If this field is omitted, there are no more
pages.
</td>
</tr>
</table>



