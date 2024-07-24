description: A response candidate generated from the model.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="google.generativeai.protos.Candidate" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="FinishReason"/>
</div>

# google.generativeai.protos.Candidate

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/googleapis/google-cloud-python/tree/main/packages/google-ai-generativelanguage/google/ai/generativelanguage_v1beta/types/generative_service.py#L506-L609">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



A response candidate generated from the model.

<!-- Placeholder for "Used in" -->




<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`index`<a id="index"></a>
</td>
<td>
`int`

Output only. Index of the candidate in the
list of candidates.

</td>
</tr><tr>
<td>
`content`<a id="content"></a>
</td>
<td>
`google.ai.generativelanguage.Content`

Output only. Generated content returned from
the model.
</td>
</tr><tr>
<td>
`finish_reason`<a id="finish_reason"></a>
</td>
<td>
`google.ai.generativelanguage.Candidate.FinishReason`

Optional. Output only. The reason why the
model stopped generating tokens.
If empty, the model has not stopped generating
the tokens.
</td>
</tr><tr>
<td>
`safety_ratings`<a id="safety_ratings"></a>
</td>
<td>
`MutableSequence[google.ai.generativelanguage.SafetyRating]`

List of ratings for the safety of a response
candidate.
There is at most one rating per category.
</td>
</tr><tr>
<td>
`citation_metadata`<a id="citation_metadata"></a>
</td>
<td>
`google.ai.generativelanguage.CitationMetadata`

Output only. Citation information for model-generated
candidate.

This field may be populated with recitation information for
any text included in the ``content``. These are passages
that are "recited" from copyrighted material in the
foundational LLM's training data.
</td>
</tr><tr>
<td>
`token_count`<a id="token_count"></a>
</td>
<td>
`int`

Output only. Token count for this candidate.
</td>
</tr><tr>
<td>
`grounding_attributions`<a id="grounding_attributions"></a>
</td>
<td>
`MutableSequence[google.ai.generativelanguage.GroundingAttribution]`

Output only. Attribution information for sources that
contributed to a grounded answer.

This field is populated for ``GenerateAnswer`` calls.
</td>
</tr>
</table>



## Child Classes
[`class FinishReason`](../../../google/generativeai/protos/Candidate/FinishReason.md)

