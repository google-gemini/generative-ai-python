description: Request to generate a completion from the model.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="google.generativeai.protos.GenerateContentRequest" />
<meta itemprop="path" content="Stable" />
</div>

# google.generativeai.protos.GenerateContentRequest

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/googleapis/google-cloud-python/tree/main/packages/google-ai-generativelanguage/google/ai/generativelanguage_v1beta/types/generative_service.py#L89-L196">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Request to generate a completion from the model.

<!-- Placeholder for "Used in" -->




<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`model`<a id="model"></a>
</td>
<td>
`str`

Required. The name of the ``Model`` to use for generating
the completion.

Format: ``name=models/{model}``.
</td>
</tr><tr>
<td>
`system_instruction`<a id="system_instruction"></a>
</td>
<td>
`google.ai.generativelanguage.Content`

Optional. Developer set system instruction.
Currently, text only.

</td>
</tr><tr>
<td>
`contents`<a id="contents"></a>
</td>
<td>
`MutableSequence[google.ai.generativelanguage.Content]`

Required. The content of the current
conversation with the model.
For single-turn queries, this is a single
instance. For multi-turn queries, this is a
repeated field that contains conversation
history + latest request.
</td>
</tr><tr>
<td>
`tools`<a id="tools"></a>
</td>
<td>
`MutableSequence[google.ai.generativelanguage.Tool]`

Optional. A list of ``Tools`` the model may use to generate
the next response.

A ``Tool`` is a piece of code that enables the system to
interact with external systems to perform an action, or set
of actions, outside of knowledge and scope of the model. The
only supported tool is currently ``Function``.
</td>
</tr><tr>
<td>
`tool_config`<a id="tool_config"></a>
</td>
<td>
`google.ai.generativelanguage.ToolConfig`

Optional. Tool configuration for any ``Tool`` specified in
the request.
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
<a href="../../../google/generativeai/protos/GenerateContentRequest.md#contents"><code>GenerateContentRequest.contents</code></a> and
<a href="../../../google/generativeai/protos/GenerateContentResponse.md#candidates"><code>GenerateContentResponse.candidates</code></a>. There should not be
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
`generation_config`<a id="generation_config"></a>
</td>
<td>
`google.ai.generativelanguage.GenerationConfig`

Optional. Configuration options for model
generation and outputs.

</td>
</tr><tr>
<td>
`cached_content`<a id="cached_content"></a>
</td>
<td>
`str`

Optional. The name of the cached content used as context to
serve the prediction. Note: only used in explicit caching,
where users can have control over caching (e.g. what content
to cache) and enjoy guaranteed cost savings. Format:
``cachedContents/{cachedContent}``

</td>
</tr>
</table>



