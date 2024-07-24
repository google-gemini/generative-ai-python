description: Request to delete a Corpus.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="google.generativeai.protos.DeleteCorpusRequest" />
<meta itemprop="path" content="Stable" />
</div>

# google.generativeai.protos.DeleteCorpusRequest

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/googleapis/google-cloud-python/tree/main/packages/google-ai-generativelanguage/google/ai/generativelanguage_v1beta/types/retriever_service.py#L113-L135">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Request to delete a ``Corpus``.

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

Required. The resource name of the ``Corpus``. Example:
``corpora/my-corpus-123``
</td>
</tr><tr>
<td>
`force`<a id="force"></a>
</td>
<td>
`bool`

Optional. If set to true, any ``Document``\ s and objects
related to this ``Corpus`` will also be deleted.

If false (the default), a ``FAILED_PRECONDITION`` error will
be returned if ``Corpus`` contains any ``Document``\ s.
</td>
</tr>
</table>



