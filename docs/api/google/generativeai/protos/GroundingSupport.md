
# google.generativeai.protos.GroundingSupport

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent">
<td>
  <a target="_blank" href="https://github.com/googleapis/google-cloud-python/tree/main/packages/google-ai-generativelanguage/google/ai/generativelanguage_v1beta/types/generative_service.py#L1112-L1148">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Grounding support.

<!-- Placeholder for "Used in" -->




<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>

`segment`<a id="segment"></a>

</td>
<td>

`google.ai.generativelanguage.Segment`

Segment of the content this support belongs
to.


</td>
</tr><tr>
<td>

`grounding_chunk_indices`<a id="grounding_chunk_indices"></a>

</td>
<td>

`MutableSequence[int]`

A list of indices (into 'grounding_chunk') specifying the
citations associated with the claim. For instance [1,3,4]
means that grounding_chunk[1], grounding_chunk[3],
grounding_chunk[4] are the retrieved content attributed to
the claim.

</td>
</tr><tr>
<td>

`confidence_scores`<a id="confidence_scores"></a>

</td>
<td>

`MutableSequence[float]`

Confidence score of the support references. Ranges from 0 to
1. 1 is the most confident. This list must have the same
size as the grounding_chunk_indices.

</td>
</tr>
</table>



