description: Safety rating for a piece of content.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="google.generativeai.protos.SafetyRating" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="HarmProbability"/>
</div>

# google.generativeai.protos.SafetyRating

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/googleapis/google-cloud-python/tree/main/packages/google-ai-generativelanguage/google/ai/generativelanguage_v1beta/types/safety.py#L160-L219">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Safety rating for a piece of content.

<!-- Placeholder for "Used in" -->

The safety rating contains the category of harm and the harm
probability level in that category for a piece of content.
Content is classified for safety across a number of harm
categories and the probability of the harm classification is
included here.



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`category`<a id="category"></a>
</td>
<td>
`google.ai.generativelanguage.HarmCategory`

Required. The category for this rating.
</td>
</tr><tr>
<td>
`probability`<a id="probability"></a>
</td>
<td>
`google.ai.generativelanguage.SafetyRating.HarmProbability`

Required. The probability of harm for this
content.
</td>
</tr><tr>
<td>
`blocked`<a id="blocked"></a>
</td>
<td>
`bool`

Was this content blocked because of this
rating?
</td>
</tr>
</table>



## Child Classes
[`class HarmProbability`](../../../google/generativeai/types/HarmProbability.md)

