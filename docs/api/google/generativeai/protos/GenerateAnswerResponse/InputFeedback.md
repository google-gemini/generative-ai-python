
# google.generativeai.protos.GenerateAnswerResponse.InputFeedback

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent">
<td>
  <a target="_blank" href="https://github.com/googleapis/google-cloud-python/tree/main/packages/google-ai-generativelanguage/google/ai/generativelanguage_v1beta/types/generative_service.py#L1332-L1378">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Feedback related to the input data used to answer the question, as opposed to the model-generated response to the question.

<!-- Placeholder for "Used in" -->





<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>

`block_reason`<a id="block_reason"></a>

</td>
<td>

`google.ai.generativelanguage.GenerateAnswerResponse.InputFeedback.BlockReason`

Optional. If set, the input was blocked and
no candidates are returned. Rephrase the input.


</td>
</tr><tr>
<td>

`safety_ratings`<a id="safety_ratings"></a>

</td>
<td>

`MutableSequence[google.ai.generativelanguage.SafetyRating]`

Ratings for safety of the input.
There is at most one rating per category.

</td>
</tr>
</table>



## Child Classes
[`class BlockReason`](../../../../google/generativeai/protos/GenerateAnswerResponse/InputFeedback/BlockReason.md)

