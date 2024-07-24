description: Safety feedback for an entire request.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="google.generativeai.protos.SafetyFeedback" />
<meta itemprop="path" content="Stable" />
</div>

# google.generativeai.protos.SafetyFeedback

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/googleapis/google-cloud-python/tree/main/packages/google-ai-generativelanguage/google/ai/generativelanguage_v1beta/types/safety.py#L131-L157">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Safety feedback for an entire request.

<!-- Placeholder for "Used in" -->

This field is populated if content in the input and/or response
is blocked due to safety settings. SafetyFeedback may not exist
for every HarmCategory. Each SafetyFeedback will return the
safety settings used by the request as well as the lowest
HarmProbability that should be allowed in order to return a
result.



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`rating`<a id="rating"></a>
</td>
<td>
`google.ai.generativelanguage.SafetyRating`

Safety rating evaluated from content.
</td>
</tr><tr>
<td>
`setting`<a id="setting"></a>
</td>
<td>
`google.ai.generativelanguage.SafetySetting`

Safety settings applied to the request.
</td>
</tr>
</table>



