description: Request for listing permissions.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="google.generativeai.protos.ListPermissionsRequest" />
<meta itemprop="path" content="Stable" />
</div>

# google.generativeai.protos.ListPermissionsRequest

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/googleapis/google-cloud-python/tree/main/packages/google-ai-generativelanguage/google/ai/generativelanguage_v1beta/types/permission_service.py#L80-L117">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Request for listing permissions.

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

Required. The parent resource of the permissions. Formats:
``tunedModels/{tuned_model}`` ``corpora/{corpus}``
</td>
</tr><tr>
<td>
`page_size`<a id="page_size"></a>
</td>
<td>
`int`

Optional. The maximum number of ``Permission``\ s to return
(per page). The service may return fewer permissions.

If unspecified, at most 10 permissions will be returned.
This method returns at most 1000 permissions per page, even
if you pass larger page_size.
</td>
</tr><tr>
<td>
`page_token`<a id="page_token"></a>
</td>
<td>
`str`

Optional. A page token, received from a previous
``ListPermissions`` call.

Provide the ``page_token`` returned by one request as an
argument to the next request to retrieve the next page.

When paginating, all other parameters provided to
``ListPermissions`` must match the call that provided the
page token.
</td>
</tr>
</table>



