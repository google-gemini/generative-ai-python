description: Batch request to get embeddings from the model for a list of prompts.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="google.generativeai.protos.BatchEmbedContentsRequest" />
<meta itemprop="path" content="Stable" />
</div>

# google.generativeai.protos.BatchEmbedContentsRequest

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/googleapis/google-cloud-python/tree/main/packages/google-ai-generativelanguage/google/ai/generativelanguage_v1beta/types/generative_service.py#L1056-L1083">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Batch request to get embeddings from the model for a list of prompts.

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

Required. The model's resource name. This serves as an ID
for the Model to use.

This name should match a model name returned by the
``ListModels`` method.

Format: ``models/{model}``
</td>
</tr><tr>
<td>
`requests`<a id="requests"></a>
</td>
<td>
`MutableSequence[google.ai.generativelanguage.EmbedContentRequest]`

Required. Embed requests for the batch. The model in each of
these requests must match the model specified
<a href="../../../google/generativeai/protos/BatchEmbedContentsRequest.md#model"><code>BatchEmbedContentsRequest.model</code></a>.
</td>
</tr>
</table>



