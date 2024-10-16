
# google.generativeai.protos.CountTokensResponse

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent">
<td>
  <a target="_blank" href="https://github.com/googleapis/google-cloud-python/tree/main/packages/google-ai-generativelanguage/google/ai/generativelanguage_v1beta/types/generative_service.py#L1589-L1610">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



A response from ``CountTokens``.

<!-- Placeholder for "Used in" -->

It returns the model's ``token_count`` for the ``prompt``.



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>

`total_tokens`<a id="total_tokens"></a>

</td>
<td>

`int`

The number of tokens that the ``Model`` tokenizes the
``prompt`` into. Always non-negative.

</td>
</tr><tr>
<td>

`cached_content_token_count`<a id="cached_content_token_count"></a>

</td>
<td>

`int`

Number of tokens in the cached part of the
prompt (the cached content).

</td>
</tr>
</table>



