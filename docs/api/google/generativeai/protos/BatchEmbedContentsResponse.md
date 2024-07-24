description: The response to a BatchEmbedContentsRequest.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="google.generativeai.protos.BatchEmbedContentsResponse" />
<meta itemprop="path" content="Stable" />
</div>

# google.generativeai.protos.BatchEmbedContentsResponse

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/googleapis/google-cloud-python/tree/main/packages/google-ai-generativelanguage/google/ai/generativelanguage_v1beta/types/generative_service.py#L1086-L1100">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



The response to a ``BatchEmbedContentsRequest``.

<!-- Placeholder for "Used in" -->




<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`embeddings`<a id="embeddings"></a>
</td>
<td>
`MutableSequence[google.ai.generativelanguage.ContentEmbedding]`

Output only. The embeddings for each request,
in the same order as provided in the batch
request.
</td>
</tr>
</table>



