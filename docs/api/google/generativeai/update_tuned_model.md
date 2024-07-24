description: Calls the API to push updates to a specified tuned model where only certain attributes are updatable.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="google.generativeai.update_tuned_model" />
<meta itemprop="path" content="Stable" />
</div>

# google.generativeai.update_tuned_model

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/google/generative-ai-python/blob/master/google/generativeai/models.py#L393-L443">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Calls the API to push updates to a specified tuned model where only certain attributes are updatable.


<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>google.generativeai.update_tuned_model(
    tuned_model: (str | protos.TunedModel),
    updates: (dict[str, Any] | None) = None,
    *,
    client: (glm.ModelServiceClient | None) = None,
    request_options: (helper_types.RequestOptionsType | None) = None
) -> model_types.TunedModel
</code></pre>



<!-- Placeholder for "Used in" -->
