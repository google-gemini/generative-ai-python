description: Response from ListModel containing a paginated list of Models.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="google.generativeai.protos.ListModelsResponse" />
<meta itemprop="path" content="Stable" />
</div>

# google.generativeai.protos.ListModelsResponse

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/googleapis/google-cloud-python/tree/main/packages/google-ai-generativelanguage/google/ai/generativelanguage_v1beta/types/model_service.py#L94-L119">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Response from ``ListModel`` containing a paginated list of Models.

<!-- Placeholder for "Used in" -->




<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`models`<a id="models"></a>
</td>
<td>
`MutableSequence[google.ai.generativelanguage.Model]`

The returned Models.
</td>
</tr><tr>
<td>
`next_page_token`<a id="next_page_token"></a>
</td>
<td>
`str`

A token, which can be sent as ``page_token`` to retrieve the
next page.

If this field is omitted, there are no more pages.
</td>
</tr>
</table>



