description: Calls the API to fetch a tuned model by name.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="google.generativeai.get_tuned_model" />
<meta itemprop="path" content="Stable" />
</div>

# google.generativeai.get_tuned_model

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/google/generative-ai-python/blob/master/google/generativeai/models.py#L105-L142">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Calls the API to fetch a tuned model by name.


<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>google.generativeai.get_tuned_model(
    name: model_types.TunedModelNameOptions,
    *,
    client=None,
    request_options: (helper_types.RequestOptionsType | None) = None
) -> model_types.TunedModel
</code></pre>



<!-- Placeholder for "Used in" -->

```
import pprint
model = genai.get_tuned_model('tunedModels/gemini-1.0-pro-001')
pprint.pprint(model)
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`name`<a id="name"></a>
</td>
<td>
The name of the model to fetch. Should start with `tunedModels/`
</td>
</tr><tr>
<td>
`client`<a id="client"></a>
</td>
<td>
The client to use.
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
A <a href="../../google/generativeai/types/TunedModel.md"><code>types.TunedModel</code></a>.
</td>
</tr>

</table>

