description: Request for ListFiles.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="google.generativeai.protos.ListFilesRequest" />
<meta itemprop="path" content="Stable" />
</div>

# google.generativeai.protos.ListFilesRequest

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/googleapis/google-cloud-python/tree/main/packages/google-ai-generativelanguage/google/ai/generativelanguage_v1beta/types/file_service.py#L67-L86">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Request for ``ListFiles``.

<!-- Placeholder for "Used in" -->




<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`page_size`<a id="page_size"></a>
</td>
<td>
`int`

Optional. Maximum number of ``File``\ s to return per page.
If unspecified, defaults to 10. Maximum ``page_size`` is
100.
</td>
</tr><tr>
<td>
`page_token`<a id="page_token"></a>
</td>
<td>
`str`

Optional. A page token from a previous ``ListFiles`` call.
</td>
</tr>
</table>



