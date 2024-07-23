description: The response from the model, including candidate completions.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="google.generativeai.protos.GenerateTextResponse" />
<meta itemprop="path" content="Stable" />
</div>

# google.generativeai.protos.GenerateTextResponse

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/googleapis/google-cloud-python/tree/main/packages/google-ai-generativelanguage/google/ai/generativelanguage_v1beta/types/text_service.py#L188-L226">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



The response from the model, including candidate completions.

<!-- Placeholder for "Used in" -->




<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`candidates`<a id="candidates"></a>
</td>
<td>
`MutableSequence[google.ai.generativelanguage.TextCompletion]`

Candidate responses from the model.
</td>
</tr><tr>
<td>
`filters`<a id="filters"></a>
</td>
<td>
`MutableSequence[google.ai.generativelanguage.ContentFilter]`

A set of content filtering metadata for the prompt and
response text.

This indicates which ``SafetyCategory``\ (s) blocked a
candidate from this response, the lowest ``HarmProbability``
that triggered a block, and the HarmThreshold setting for
that category. This indicates the smallest change to the
``SafetySettings`` that would be necessary to unblock at
least 1 response.

The blocking is configured by the ``SafetySettings`` in the
request (or the default ``SafetySettings`` of the API).
</td>
</tr><tr>
<td>
`safety_feedback`<a id="safety_feedback"></a>
</td>
<td>
`MutableSequence[google.ai.generativelanguage.SafetyFeedback]`

Returns any safety feedback related to
content filtering.
</td>
</tr>
</table>



