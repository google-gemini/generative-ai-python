description: Request to delete a Document.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="google.generativeai.protos.DeleteDocumentRequest" />
<meta itemprop="path" content="Stable" />
</div>

# google.generativeai.protos.DeleteDocumentRequest

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/googleapis/google-cloud-python/tree/main/packages/google-ai-generativelanguage/google/ai/generativelanguage_v1beta/types/retriever_service.py#L362-L384">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Request to delete a ``Document``.

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

Required. The resource name of the ``Document`` to delete.
Example: ``corpora/my-corpus-123/documents/the-doc-abc``
</td>
</tr><tr>
<td>
`force`<a id="force"></a>
</td>
<td>
`bool`

Optional. If set to true, any ``Chunk``\ s and objects
related to this ``Document`` will also be deleted.

If false (the default), a ``FAILED_PRECONDITION`` error will
be returned if ``Document`` contains any ``Chunk``\ s.
</td>
</tr>
</table>



