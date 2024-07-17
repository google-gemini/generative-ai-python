description: Output text returned from a model.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="google.generativeai.protos.TextCompletion" />
<meta itemprop="path" content="Stable" />
</div>

# google.generativeai.protos.TextCompletion

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/googleapis/google-cloud-python/tree/main/packages/google-ai-generativelanguage/google/ai/generativelanguage_v1beta/types/text_service.py#L246-L283">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Output text returned from a model.

<!-- Placeholder for "Used in" -->




<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`output`<a id="output"></a>
</td>
<td>
`str`

Output only. The generated text returned from
the model.
</td>
</tr><tr>
<td>
`safety_ratings`<a id="safety_ratings"></a>
</td>
<td>
`MutableSequence[google.ai.generativelanguage.SafetyRating]`

Ratings for the safety of a response.

There is at most one rating per category.
</td>
</tr><tr>
<td>
`citation_metadata`<a id="citation_metadata"></a>
</td>
<td>
`google.ai.generativelanguage.CitationMetadata`

Output only. Citation information for model-generated
``output`` in this ``TextCompletion``.

This field may be populated with attribution information for
any text included in the ``output``.

</td>
</tr>
</table>



