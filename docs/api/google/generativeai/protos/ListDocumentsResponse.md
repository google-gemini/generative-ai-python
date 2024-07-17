description: Response from ListDocuments containing a paginated list of Document\ s.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="google.generativeai.protos.ListDocumentsResponse" />
<meta itemprop="path" content="Stable" />
</div>

# google.generativeai.protos.ListDocumentsResponse

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/googleapis/google-cloud-python/tree/main/packages/google-ai-generativelanguage/google/ai/generativelanguage_v1beta/types/retriever_service.py#L426-L452">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Response from ``ListDocuments`` containing a paginated list of ``Document``\ s.

<!-- Placeholder for "Used in" -->
 The ``Document``\ s are sorted by ascending
``document.create_time``.



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`documents`<a id="documents"></a>
</td>
<td>
`MutableSequence[google.ai.generativelanguage.Document]`

The returned ``Document``\ s.
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



