description: Calls the API to list all available models.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="google.generativeai.list_models" />
<meta itemprop="path" content="Stable" />
</div>

# google.generativeai.list_models

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/google/generative-ai-python/blob/master/google/generativeai/models.py#L175-L206">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Calls the API to list all available models.


<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>google.generativeai.list_models(
    *,
    page_size: (int | None) = 50,
    client: (glm.ModelServiceClient | None) = None,
    request_options: (helper_types.RequestOptionsType | None) = None
) -> model_types.ModelsIterable
</code></pre>



<!-- Placeholder for "Used in" -->

```
import pprint
for model in genai.list_models():
    pprint.pprint(model)
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`page_size`<a id="page_size"></a>
</td>
<td>
How many `types.Models` to fetch per page (api call).
</td>
</tr><tr>
<td>
`client`<a id="client"></a>
</td>
<td>
You may pass a `glm.ModelServiceClient` instead of using the default client.
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
<tr><th colspan="2"><h2 class="add-link">Yields</h2></th></tr>
<tr class="alt">
<td colspan="2">
<a href="../../google/generativeai/types/Model.md"><code>types.Model</code></a> objects.
</td>
</tr>

</table>

