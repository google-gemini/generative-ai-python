description: Calls the API to generate text based on the provided prompt.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="google.generativeai.generate_text" />
<meta itemprop="path" content="Stable" />
</div>

# google.generativeai.generate_text

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/google/generative-ai-python/blob/master/google/generativeai/text.py#L135-L205">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Calls the API to generate text based on the provided prompt.


<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>google.generativeai.generate_text(
    *,
    model: model_types.AnyModelNameOptions = DEFAULT_TEXT_MODEL,
    prompt: str,
    temperature: (float | None) = None,
    candidate_count: (int | None) = None,
    max_output_tokens: (int | None) = None,
    top_p: (float | None) = None,
    top_k: (float | None) = None,
    safety_settings: (palm_safety_types.SafetySettingOptions | None) = None,
    stop_sequences: (str | Iterable[str] | None) = None,
    client: (glm.TextServiceClient | None) = None,
    request_options: (helper_types.RequestOptionsType | None) = None
) -> text_types.Completion
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`model`<a id="model"></a>
</td>
<td>
Which model to call, as a string or a <a href="../../google/generativeai/types/Model.md"><code>types.Model</code></a>.
</td>
</tr><tr>
<td>
`prompt`<a id="prompt"></a>
</td>
<td>
Free-form input text given to the model. Given a prompt, the model will
generate text that completes the input text.
</td>
</tr><tr>
<td>
`temperature`<a id="temperature"></a>
</td>
<td>
Controls the randomness of the output. Must be positive.
Typical values are in the range: `[0.0,1.0]`. Higher values produce a
more random and varied response. A temperature of zero will be deterministic.
</td>
</tr><tr>
<td>
`candidate_count`<a id="candidate_count"></a>
</td>
<td>
The **maximum** number of generated response messages to return.
This value must be between `[1, 8]`, inclusive. If unset, this
will default to `1`.

Note: Only unique candidates are returned. Higher temperatures are more
likely to produce unique candidates. Setting `temperature=0.0` will always
return 1 candidate regardless of the `candidate_count`.
</td>
</tr><tr>
<td>
`max_output_tokens`<a id="max_output_tokens"></a>
</td>
<td>
Maximum number of tokens to include in a candidate. Must be greater
than zero. If unset, will default to 64.
</td>
</tr><tr>
<td>
`top_k`<a id="top_k"></a>
</td>
<td>
The API uses combined [nucleus](https://arxiv.org/abs/1904.09751) and top-k sampling.
`top_k` sets the maximum number of tokens to sample from on each step.
</td>
</tr><tr>
<td>
`top_p`<a id="top_p"></a>
</td>
<td>
The API uses combined [nucleus](https://arxiv.org/abs/1904.09751) and top-k sampling.
`top_p` configures the nucleus sampling. It sets the maximum cumulative
probability of tokens to sample from.
For example, if the sorted probabilities are
`[0.5, 0.2, 0.1, 0.1, 0.05, 0.05]` a `top_p` of `0.8` will sample
as `[0.625, 0.25, 0.125, 0, 0, 0]`.
</td>
</tr><tr>
<td>
`safety_settings`<a id="safety_settings"></a>
</td>
<td>
A list of unique `types.SafetySetting` instances for blocking unsafe content.
These will be enforced on the `prompt` and
`candidates`. There should not be more than one
setting for each `types.SafetyCategory` type. The API will block any prompts and
responses that fail to meet the thresholds set by these settings. This list
overrides the default settings for each `SafetyCategory` specified in the
safety_settings. If there is no `types.SafetySetting` for a given
`SafetyCategory` provided in the list, the API will use the default safety
setting for that category.
</td>
</tr><tr>
<td>
`stop_sequences`<a id="stop_sequences"></a>
</td>
<td>
A set of up to 5 character sequences that will stop output generation.
If specified, the API will stop at the first appearance of a stop
sequence. The stop sequence will not be included as part of the response.
</td>
</tr><tr>
<td>
`client`<a id="client"></a>
</td>
<td>
If you're not relying on a default client, you pass a `glm.TextServiceClient` instead.
</td>
</tr><tr>
<td>
`request_options`<a id="request_options"></a>
</td>
<td>
Options for the request.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A <a href="../../google/generativeai/types/Completion.md"><code>types.Completion</code></a> containing the model's text completion response.
</td>
</tr>

</table>

