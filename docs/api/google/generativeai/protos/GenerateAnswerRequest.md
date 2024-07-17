description: Request to generate a grounded answer from the model.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="google.generativeai.protos.GenerateAnswerRequest" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="AnswerStyle"/>
</div>

# google.generativeai.protos.GenerateAnswerRequest

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/googleapis/google-cloud-python/tree/main/packages/google-ai-generativelanguage/google/ai/generativelanguage_v1beta/types/generative_service.py#L716-L840">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Request to generate a grounded answer from the model.

<!-- Placeholder for "Used in" -->

This message has `oneof`_ fields (mutually exclusive fields).
For each oneof, at most one member field can be set at the same time.
Setting any member of the oneof automatically clears all other
members.




<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`inline_passages`<a id="inline_passages"></a>
</td>
<td>
`google.ai.generativelanguage.GroundingPassages`

Passages provided inline with the request.

This field is a member of `oneof`_ ``grounding_source``.
</td>
</tr><tr>
<td>
`semantic_retriever`<a id="semantic_retriever"></a>
</td>
<td>
`google.ai.generativelanguage.SemanticRetrieverConfig`

Content retrieved from resources created via
the Semantic Retriever API.

This field is a member of `oneof`_ ``grounding_source``.
</td>
</tr><tr>
<td>
`model`<a id="model"></a>
</td>
<td>
`str`

Required. The name of the ``Model`` to use for generating
the grounded response.

Format: ``model=models/{model}``.
</td>
</tr><tr>
<td>
`contents`<a id="contents"></a>
</td>
<td>
`MutableSequence[google.ai.generativelanguage.Content]`

Required. The content of the current conversation with the
model. For single-turn queries, this is a single question to
answer. For multi-turn queries, this is a repeated field
that contains conversation history and the last ``Content``
in the list containing the question.

Note: GenerateAnswer currently only supports queries in
English.
</td>
</tr><tr>
<td>
`answer_style`<a id="answer_style"></a>
</td>
<td>
`google.ai.generativelanguage.GenerateAnswerRequest.AnswerStyle`

Required. Style in which answers should be
returned.
</td>
</tr><tr>
<td>
`safety_settings`<a id="safety_settings"></a>
</td>
<td>
`MutableSequence[google.ai.generativelanguage.SafetySetting]`

Optional. A list of unique ``SafetySetting`` instances for
blocking unsafe content.

This will be enforced on the
<a href="../../../google/generativeai/protos/GenerateAnswerRequest.md#contents"><code>GenerateAnswerRequest.contents</code></a> and
``GenerateAnswerResponse.candidate``. There should not be
more than one setting for each ``SafetyCategory`` type. The
API will block any contents and responses that fail to meet
the thresholds set by these settings. This list overrides
the default settings for each ``SafetyCategory`` specified
in the safety_settings. If there is no ``SafetySetting`` for
a given ``SafetyCategory`` provided in the list, the API
will use the default safety setting for that category. Harm
categories HARM_CATEGORY_HATE_SPEECH,
HARM_CATEGORY_SEXUALLY_EXPLICIT,
HARM_CATEGORY_DANGEROUS_CONTENT, HARM_CATEGORY_HARASSMENT
are supported.
</td>
</tr><tr>
<td>
`temperature`<a id="temperature"></a>
</td>
<td>
`float`

Optional. Controls the randomness of the output.

Values can range from [0.0,1.0], inclusive. A value closer
to 1.0 will produce responses that are more varied and
creative, while a value closer to 0.0 will typically result
in more straightforward responses from the model. A low
temperature (~0.2) is usually recommended for
Attributed-Question-Answering use cases.

</td>
</tr>
</table>



## Child Classes
[`class AnswerStyle`](../../../google/generativeai/protos/GenerateAnswerRequest/AnswerStyle.md)

