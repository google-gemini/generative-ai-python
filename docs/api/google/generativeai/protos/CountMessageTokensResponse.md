description: A response from CountMessageTokens.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="google.generativeai.protos.CountMessageTokensResponse" />
<meta itemprop="path" content="Stable" />
</div>

# google.generativeai.protos.CountMessageTokensResponse

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/googleapis/google-cloud-python/tree/main/packages/google-ai-generativelanguage/google/ai/generativelanguage_v1beta/types/discuss_service.py#L337-L353">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



A response from ``CountMessageTokens``.

<!-- Placeholder for "Used in" -->

It returns the model's ``token_count`` for the ``prompt``.



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`token_count`<a id="token_count"></a>
</td>
<td>
`int`

The number of tokens that the ``model`` tokenizes the
``prompt`` into.

Always non-negative.
</td>
</tr>
</table>



