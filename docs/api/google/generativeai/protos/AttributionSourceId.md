description: Identifier for the source contributing to this attribution.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="google.generativeai.protos.AttributionSourceId" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="GroundingPassageId"/>
<meta itemprop="property" content="SemanticRetrieverChunk"/>
</div>

# google.generativeai.protos.AttributionSourceId

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/googleapis/google-cloud-python/tree/main/packages/google-ai-generativelanguage/google/ai/generativelanguage_v1beta/types/generative_service.py#L612-L689">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Identifier for the source contributing to this attribution.

<!-- Placeholder for "Used in" -->

This message has `oneof`_ fields (mutually exclusive fields).
For each oneof, at most one member field can be set at the same time.
Setting any member of the oneof automatically clears all other
members.




<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`grounding_passage`<a id="grounding_passage"></a>
</td>
<td>
`google.ai.generativelanguage.AttributionSourceId.GroundingPassageId`

Identifier for an inline passage.

This field is a member of `oneof`_ ``source``.
</td>
</tr><tr>
<td>
`semantic_retriever_chunk`<a id="semantic_retriever_chunk"></a>
</td>
<td>
`google.ai.generativelanguage.AttributionSourceId.SemanticRetrieverChunk`

Identifier for a ``Chunk`` fetched via Semantic Retriever.

This field is a member of `oneof`_ ``source``.
</td>
</tr>
</table>



## Child Classes
[`class GroundingPassageId`](../../../google/generativeai/protos/AttributionSourceId/GroundingPassageId.md)

[`class SemanticRetrieverChunk`](../../../google/generativeai/protos/AttributionSourceId/SemanticRetrieverChunk.md)

