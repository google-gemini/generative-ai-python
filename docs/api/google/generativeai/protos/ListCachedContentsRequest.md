description: Request to list CachedContents.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="google.generativeai.protos.ListCachedContentsRequest" />
<meta itemprop="path" content="Stable" />
</div>

# google.generativeai.protos.ListCachedContentsRequest

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/googleapis/google-cloud-python/tree/main/packages/google-ai-generativelanguage/google/ai/generativelanguage_v1beta/types/cache_service.py#L40-L68">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Request to list CachedContents.

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

Optional. The maximum number of cached
contents to return. The service may return fewer
than this value. If unspecified, some default
(under maximum) number of items will be
returned. The maximum value is 1000; values
above 1000 will be coerced to 1000.
</td>
</tr><tr>
<td>
`page_token`<a id="page_token"></a>
</td>
<td>
`str`

Optional. A page token, received from a previous
``ListCachedContents`` call. Provide this to retrieve the
subsequent page.

When paginating, all other parameters provided to
``ListCachedContents`` must match the call that provided the
page token.
</td>
</tr>
</table>



