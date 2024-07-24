description: Request to create a Chunk.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="google.generativeai.protos.CreateChunkRequest" />
<meta itemprop="path" content="Stable" />
</div>

# google.generativeai.protos.CreateChunkRequest

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/googleapis/google-cloud-python/tree/main/packages/google-ai-generativelanguage/google/ai/generativelanguage_v1beta/types/retriever_service.py#L538-L558">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Request to create a ``Chunk``.

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

Required. The name of the ``Document`` where this ``Chunk``
will be created. Example:
``corpora/my-corpus-123/documents/the-doc-abc``
</td>
</tr><tr>
<td>
`chunk`<a id="chunk"></a>
</td>
<td>
`google.ai.generativelanguage.Chunk`

Required. The ``Chunk`` to create.
</td>
</tr>
</table>



