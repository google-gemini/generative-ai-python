description: Calls the API to initiate a chat with a model using provided parameters

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="google.generativeai.chat" />
<meta itemprop="path" content="Stable" />
</div>

# google.generativeai.chat

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/google/generative-ai-python/blob/master/google/generativeai/discuss.py#L312-L408">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Calls the API to initiate a chat with a model using provided parameters


<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>google.generativeai.chat(
    *,
    model: (model_types.AnyModelNameOptions | None) = &#x27;models/chat-bison-001&#x27;,
    context: (str | None) = None,
    examples: (discuss_types.ExamplesOptions | None) = None,
    messages: (discuss_types.MessagesOptions | None) = None,
    temperature: (float | None) = None,
    candidate_count: (int | None) = None,
    top_p: (float | None) = None,
    top_k: (float | None) = None,
    prompt: (discuss_types.MessagePromptOptions | None) = None,
    client: (glm.DiscussServiceClient | None) = None,
    request_options: (helper_types.RequestOptionsType | None) = None
) -> discuss_types.ChatResponse
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
`context`<a id="context"></a>
</td>
<td>
Text that should be provided to the model first, to ground the response.

If not empty, this `context` will be given to the model first before the
`examples` and `messages`.

This field can be a description of your prompt to the model to help provide
context and guide the responses.

Examples:

* "Translate the phrase from English to French."
* "Given a statement, classify the sentiment as happy, sad or neutral."

Anything included in this field will take precedence over history in `messages`
if the total input size exceeds the model's <a href="../../google/generativeai/protos/Model.md#input_token_limit"><code>Model.input_token_limit</code></a>.
</td>
</tr><tr>
<td>
`examples`<a id="examples"></a>
</td>
<td>
Examples of what the model should generate.

This includes both the user input and the response that the model should
emulate.

These `examples` are treated identically to conversation messages except
that they take precedence over the history in `messages`:
If the total input size exceeds the model's `input_token_limit` the input
will be truncated. Items will be dropped from `messages` before `examples`
</td>
</tr><tr>
<td>
`messages`<a id="messages"></a>
</td>
<td>
A snapshot of the conversation history sorted chronologically.

Turns alternate between two authors.

If the total input size exceeds the model's `input_token_limit` the input
will be truncated: The oldest items will be dropped from `messages`.
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
`top_k`<a id="top_k"></a>
</td>
<td>
The API uses combined [nucleus](https://arxiv.org/abs/1904.09751) and
top-k sampling.

`top_k` sets the maximum number of tokens to sample from on each step.
</td>
</tr><tr>
<td>
`top_p`<a id="top_p"></a>
</td>
<td>
The API uses combined [nucleus](https://arxiv.org/abs/1904.09751) and
top-k sampling.

`top_p` configures the nucleus sampling. It sets the maximum cumulative
 probability of tokens to sample from.

 For example, if the sorted probabilities are
 `[0.5, 0.2, 0.1, 0.1, 0.05, 0.05]` a `top_p` of `0.8` will sample
 as `[0.625, 0.25, 0.125, 0, 0, 0]`.

 Typical values are in the `[0.9, 1.0]` range.
</td>
</tr><tr>
<td>
`prompt`<a id="prompt"></a>
</td>
<td>
You may pass a <a href="../../google/generativeai/types/MessagePromptOptions.md"><code>types.MessagePromptOptions</code></a> **instead** of a
setting `context`/`examples`/`messages`, but not both.
</td>
</tr><tr>
<td>
`client`<a id="client"></a>
</td>
<td>
If you're not relying on the default client, you pass a
`glm.DiscussServiceClient` instead.
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
A <a href="../../google/generativeai/types/ChatResponse.md"><code>types.ChatResponse</code></a> containing the model's reply.
</td>
</tr>

</table>

