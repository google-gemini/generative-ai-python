description: Request for listing Document\ s.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="google.generativeai.protos.ListDocumentsRequest" />
<meta itemprop="path" content="Stable" />
</div>

# google.generativeai.protos.ListDocumentsRequest

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/googleapis/google-cloud-python/tree/main/packages/google-ai-generativelanguage/google/ai/generativelanguage_v1beta/types/retriever_service.py#L387-L423">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Request for listing ``Document``\ s.

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

Required. The name of the ``Corpus`` containing
``Document``\ s. Example: ``corpora/my-corpus-123``
</td>
</tr><tr>
<td>
`page_size`<a id="page_size"></a>
</td>
<td>
`int`

Optional. The maximum number of ``Document``\ s to return
(per page). The service may return fewer ``Document``\ s.

If unspecified, at most 10 ``Document``\ s will be returned.
The maximum size limit is 20 ``Document``\ s per page.
</td>
</tr><tr>
<td>
`page_token`<a id="page_token"></a>
</td>
<td>
`str`

Optional. A page token, received from a previous
``ListDocuments`` call.

Provide the ``next_page_token`` returned in the response as
an argument to the next request to retrieve the next page.

When paginating, all other parameters provided to
``ListDocuments`` must match the call that provided the page
token.
</td>
</tr>
</table>



