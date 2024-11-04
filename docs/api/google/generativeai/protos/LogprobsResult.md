
# google.generativeai.protos.LogprobsResult

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent">
<td>
  <a target="_blank" href="https://github.com/googleapis/google-cloud-python/tree/main/packages/google-ai-generativelanguage/google/ai/generativelanguage_v1beta/types/generative_service.py#L760-L831">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Logprobs Result

<!-- Placeholder for "Used in" -->




<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>

`top_candidates`<a id="top_candidates"></a>

</td>
<td>

`MutableSequence[google.ai.generativelanguage.LogprobsResult.TopCandidates]`

Length = total number of decoding steps.

</td>
</tr><tr>
<td>

`chosen_candidates`<a id="chosen_candidates"></a>

</td>
<td>

`MutableSequence[google.ai.generativelanguage.LogprobsResult.Candidate]`

Length = total number of decoding steps. The chosen
candidates may or may not be in top_candidates.

</td>
</tr>
</table>



## Child Classes
[`class Candidate`](../../../google/generativeai/protos/LogprobsResult/Candidate.md)

[`class TopCandidates`](../../../google/generativeai/protos/LogprobsResult/TopCandidates.md)

