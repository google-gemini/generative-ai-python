description: Batch request to get a text embedding from the model.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="google.generativeai.protos.BatchEmbedTextRequest" />
<meta itemprop="path" content="Stable" />
</div>

# google.generativeai.protos.BatchEmbedTextRequest

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/googleapis/google-cloud-python/tree/main/packages/google-ai-generativelanguage/google/ai/generativelanguage_v1beta/types/text_service.py#L329-L358">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Batch request to get a text embedding from the model.

<!-- Placeholder for "Used in" -->




<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`model`<a id="model"></a>
</td>
<td>
`str`

Required. The name of the ``Model`` to use for generating
the embedding. Examples: models/embedding-gecko-001
</td>
</tr><tr>
<td>
`texts`<a id="texts"></a>
</td>
<td>
`MutableSequence[str]`

Optional. The free-form input texts that the
model will turn into an embedding. The current
limit is 100 texts, over which an error will be
thrown.
</td>
</tr><tr>
<td>
`requests`<a id="requests"></a>
</td>
<td>
`MutableSequence[google.ai.generativelanguage.EmbedTextRequest]`

Optional. Embed requests for the batch. Only one of
``texts`` or ``requests`` can be set.
</td>
</tr>
</table>



