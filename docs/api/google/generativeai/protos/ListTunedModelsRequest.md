description: Request for listing TunedModels.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="google.generativeai.protos.ListTunedModelsRequest" />
<meta itemprop="path" content="Stable" />
</div>

# google.generativeai.protos.ListTunedModelsRequest

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/googleapis/google-cloud-python/tree/main/packages/google-ai-generativelanguage/google/ai/generativelanguage_v1beta/types/model_service.py#L138-L192">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Request for listing TunedModels.

<!-- Placeholder for "Used in" -->




<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`page_size`<a id="page_size"></a>
</td>
<td>
`int`

Optional. The maximum number of ``TunedModels`` to return
(per page). The service may return fewer tuned models.

If unspecified, at most 10 tuned models will be returned.
This method returns at most 1000 models per page, even if
you pass a larger page_size.
</td>
</tr><tr>
<td>
`page_token`<a id="page_token"></a>
</td>
<td>
`str`

Optional. A page token, received from a previous
``ListTunedModels`` call.

Provide the ``page_token`` returned by one request as an
argument to the next request to retrieve the next page.

When paginating, all other parameters provided to
``ListTunedModels`` must match the call that provided the
page token.
</td>
</tr><tr>
<td>
`filter`<a id="filter"></a>
</td>
<td>
`str`

Optional. A filter is a full text search over
the tuned model's description and display name.
By default, results will not include tuned
models shared with everyone.

Additional operators:

  - owner:me
  - writers:me
  - readers:me
  - readers:everyone

Examples:

  "owner:me" returns all tuned models to which
caller has owner role   "readers:me" returns all
tuned models to which caller has reader role
"readers:everyone" returns all tuned models that
are shared with everyone
</td>
</tr>
</table>



