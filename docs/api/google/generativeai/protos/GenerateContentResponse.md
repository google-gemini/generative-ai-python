description: Response from the model supporting multiple candidates.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="google.generativeai.protos.GenerateContentResponse" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="PromptFeedback"/>
<meta itemprop="property" content="UsageMetadata"/>
</div>

# google.generativeai.protos.GenerateContentResponse

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/googleapis/google-cloud-python/tree/main/packages/google-ai-generativelanguage/google/ai/generativelanguage_v1beta/types/generative_service.py#L383-L503">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Response from the model supporting multiple candidates.

<!-- Placeholder for "Used in" -->

Note on safety ratings and content filtering. They are reported for
both prompt in <a href="../../../google/generativeai/protos/GenerateContentResponse.md#prompt_feedback"><code>GenerateContentResponse.prompt_feedback</code></a> and for
each candidate in ``finish_reason`` and in ``safety_ratings``. The
API contract is that:

-  either all requested candidates are returned or no candidates at
   all
-  no candidates are returned only if there was something wrong with
   the prompt (see ``prompt_feedback``)
-  feedback on each candidate is reported on ``finish_reason`` and
   ``safety_ratings``.



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`candidates`<a id="candidates"></a>
</td>
<td>
`MutableSequence[google.ai.generativelanguage.Candidate]`

Candidate responses from the model.
</td>
</tr><tr>
<td>
`prompt_feedback`<a id="prompt_feedback"></a>
</td>
<td>
`google.ai.generativelanguage.GenerateContentResponse.PromptFeedback`

Returns the prompt's feedback related to the
content filters.
</td>
</tr><tr>
<td>
`usage_metadata`<a id="usage_metadata"></a>
</td>
<td>
`google.ai.generativelanguage.GenerateContentResponse.UsageMetadata`

Output only. Metadata on the generation
requests' token usage.
</td>
</tr>
</table>



## Child Classes
[`class PromptFeedback`](../../../google/generativeai/protos/GenerateContentResponse/PromptFeedback.md)

[`class UsageMetadata`](../../../google/generativeai/protos/GenerateContentResponse/UsageMetadata.md)

