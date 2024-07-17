description: Response for ListFiles.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="google.generativeai.protos.ListFilesResponse" />
<meta itemprop="path" content="Stable" />
</div>

# google.generativeai.protos.ListFilesResponse

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/googleapis/google-cloud-python/tree/main/packages/google-ai-generativelanguage/google/ai/generativelanguage_v1beta/types/file_service.py#L89-L112">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Response for ``ListFiles``.

<!-- Placeholder for "Used in" -->




<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`files`<a id="files"></a>
</td>
<td>
`MutableSequence[google.ai.generativelanguage.File]`

The list of ``File``\ s.
</td>
</tr><tr>
<td>
`next_page_token`<a id="next_page_token"></a>
</td>
<td>
`str`

A token that can be sent as a ``page_token`` into a
subsequent ``ListFiles`` call.
</td>
</tr>
</table>



