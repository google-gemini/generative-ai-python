description: Identifier for a Chunk retrieved via Semantic Retriever specified in the GenerateAnswerRequest using SemanticRetrieverConfig.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="google.generativeai.protos.AttributionSourceId.SemanticRetrieverChunk" />
<meta itemprop="path" content="Stable" />
</div>

# google.generativeai.protos.AttributionSourceId.SemanticRetrieverChunk

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/googleapis/google-cloud-python/tree/main/packages/google-ai-generativelanguage/google/ai/generativelanguage_v1beta/types/generative_service.py#L654-L676">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Identifier for a ``Chunk`` retrieved via Semantic Retriever specified in the ``GenerateAnswerRequest`` using ``SemanticRetrieverConfig``.

<!-- Placeholder for "Used in" -->




<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`source`<a id="source"></a>
</td>
<td>
`str`

Output only. Name of the source matching the request's
<a href="../../../../google/generativeai/protos/SemanticRetrieverConfig.md#source"><code>SemanticRetrieverConfig.source</code></a>. Example: ``corpora/123``
or ``corpora/123/documents/abc``
</td>
</tr><tr>
<td>
`chunk`<a id="chunk"></a>
</td>
<td>
`str`

Output only. Name of the ``Chunk`` containing the attributed
text. Example: ``corpora/123/documents/abc/chunks/xyz``
</td>
</tr>
</table>



