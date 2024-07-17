description: Calls the API to count the number of tokens in the text prompt.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="google.generativeai.count_text_tokens" />
<meta itemprop="path" content="Stable" />
</div>

# google.generativeai.count_text_tokens

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/google/generative-ai-python/blob/master/google/generativeai/text.py#L255-L276">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Calls the API to count the number of tokens in the text prompt.


<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>google.generativeai.count_text_tokens(
    model: model_types.AnyModelNameOptions,
    prompt: str,
    client: (glm.TextServiceClient | None) = None,
    request_options: (helper_types.RequestOptionsType | None) = None
) -> text_types.TokenCount
</code></pre>



<!-- Placeholder for "Used in" -->
