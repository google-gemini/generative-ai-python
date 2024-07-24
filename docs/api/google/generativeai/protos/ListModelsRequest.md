description: Request for listing all Models.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="google.generativeai.protos.ListModelsRequest" />
<meta itemprop="path" content="Stable" />
</div>

# google.generativeai.protos.ListModelsRequest

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/googleapis/google-cloud-python/tree/main/packages/google-ai-generativelanguage/google/ai/generativelanguage_v1beta/types/model_service.py#L62-L91">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Request for listing all Models.

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

The maximum number of ``Models`` to return (per page).

The service may return fewer models. If unspecified, at most
50 models will be returned per page. This method returns at
most 1000 models per page, even if you pass a larger
page_size.
</td>
</tr><tr>
<td>
`page_token`<a id="page_token"></a>
</td>
<td>
`str`

A page token, received from a previous ``ListModels`` call.

Provide the ``page_token`` returned by one request as an
argument to the next request to retrieve the next page.

When paginating, all other parameters provided to
``ListModels`` must match the call that provided the page
token.
</td>
</tr>
</table>



