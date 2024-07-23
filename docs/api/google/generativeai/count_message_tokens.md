description: Calls the API to calculate the number of tokens used in the prompt.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="google.generativeai.count_message_tokens" />
<meta itemprop="path" content="Stable" />
</div>

# google.generativeai.count_message_tokens

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/google/generative-ai-python/blob/master/google/generativeai/discuss.py#L576-L599">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Calls the API to calculate the number of tokens used in the prompt.


<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>google.generativeai.count_message_tokens(
    *,
    prompt: discuss_types.MessagePromptOptions = None,
    context: (str | None) = None,
    examples: (discuss_types.ExamplesOptions | None) = None,
    messages: (discuss_types.MessagesOptions | None) = None,
    model: model_types.AnyModelNameOptions = DEFAULT_DISCUSS_MODEL,
    client: (glm.DiscussServiceAsyncClient | None) = None,
    request_options: (helper_types.RequestOptionsType | None) = None
) -> discuss_types.TokenCount
</code></pre>



<!-- Placeholder for "Used in" -->
