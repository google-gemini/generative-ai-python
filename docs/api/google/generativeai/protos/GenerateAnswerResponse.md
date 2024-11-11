
# google.generativeai.protos.GenerateAnswerResponse

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent">
<td>
  <a target="_blank" href="https://github.com/googleapis/google-cloud-python/tree/main/packages/google-ai-generativelanguage/google/ai/generativelanguage_v1beta/types/generative_service.py#L1283-L1395">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Response from the model for a grounded answer.

<!-- Placeholder for "Used in" -->




<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>

`answer`<a id="answer"></a>

</td>
<td>

`google.ai.generativelanguage.Candidate`

Candidate answer from the model.

Note: The model *always* attempts to provide a grounded
answer, even when the answer is unlikely to be answerable
from the given passages. In that case, a low-quality or
ungrounded answer may be provided, along with a low
``answerable_probability``.

</td>
</tr><tr>
<td>

`answerable_probability`<a id="answerable_probability"></a>

</td>
<td>

`float`

Output only. The model's estimate of the probability that
its answer is correct and grounded in the input passages.

A low ``answerable_probability`` indicates that the answer
might not be grounded in the sources.

When ``answerable_probability`` is low, you may want to:

-  Display a message to the effect of "We couldn’t answer
   that question" to the user.
-  Fall back to a general-purpose LLM that answers the
   question from world knowledge. The threshold and nature
   of such fallbacks will depend on individual use cases.
   ``0.5`` is a good starting threshold.


</td>
</tr><tr>
<td>

`input_feedback`<a id="input_feedback"></a>

</td>
<td>

`google.ai.generativelanguage.GenerateAnswerResponse.InputFeedback`

Output only. Feedback related to the input data used to
answer the question, as opposed to the model-generated
response to the question.

The input data can be one or more of the following:

-  Question specified by the last entry in
   ``GenerateAnswerRequest.content``
-  Conversation history specified by the other entries in
   ``GenerateAnswerRequest.content``
-  Grounding sources
   (<a href="../../../google/generativeai/protos/GenerateAnswerRequest.md#semantic_retriever"><code>GenerateAnswerRequest.semantic_retriever</code></a> or
   <a href="../../../google/generativeai/protos/GenerateAnswerRequest.md#inline_passages"><code>GenerateAnswerRequest.inline_passages</code></a>)


</td>
</tr>
</table>



## Child Classes
[`class InputFeedback`](../../../google/generativeai/protos/GenerateAnswerResponse/InputFeedback.md)

