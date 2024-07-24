description: Request to batch delete Chunk\ s.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="google.generativeai.protos.BatchDeleteChunksRequest" />
<meta itemprop="path" content="Stable" />
</div>

# google.generativeai.protos.BatchDeleteChunksRequest

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/googleapis/google-cloud-python/tree/main/packages/google-ai-generativelanguage/google/ai/generativelanguage_v1beta/types/retriever_service.py#L699-L721">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Request to batch delete ``Chunk``\ s.

<!-- Placeholder for "Used in" -->




<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`parent`<a id="parent"></a>
</td>
<td>
`str`

Optional. The name of the ``Document`` containing the
``Chunk``\ s to delete. The parent field in every
``DeleteChunkRequest`` must match this value. Example:
``corpora/my-corpus-123/documents/the-doc-abc``
</td>
</tr><tr>
<td>
`requests`<a id="requests"></a>
</td>
<td>
`MutableSequence[google.ai.generativelanguage.DeleteChunkRequest]`

Required. The request messages specifying the ``Chunk``\ s
to delete.
</td>
</tr>
</table>



