description: Identifier for a part within a GroundingPassage.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="google.generativeai.protos.AttributionSourceId.GroundingPassageId" />
<meta itemprop="path" content="Stable" />
</div>

# google.generativeai.protos.AttributionSourceId.GroundingPassageId

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/googleapis/google-cloud-python/tree/main/packages/google-ai-generativelanguage/google/ai/generativelanguage_v1beta/types/generative_service.py#L633-L652">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Identifier for a part within a ``GroundingPassage``.

<!-- Placeholder for "Used in" -->




<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`passage_id`<a id="passage_id"></a>
</td>
<td>
`str`

Output only. ID of the passage matching the
``GenerateAnswerRequest``'s <a href="../../../../google/generativeai/protos/GroundingPassage.md#id"><code>GroundingPassage.id</code></a>.
</td>
</tr><tr>
<td>
`part_index`<a id="part_index"></a>
</td>
<td>
`int`

Output only. Index of the part within the
``GenerateAnswerRequest``'s <a href="../../../../google/generativeai/protos/GroundingPassage.md#content"><code>GroundingPassage.content</code></a>.
</td>
</tr>
</table>



