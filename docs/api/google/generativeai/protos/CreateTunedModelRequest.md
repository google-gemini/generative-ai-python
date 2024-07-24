description: Request to create a TunedModel.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="google.generativeai.protos.CreateTunedModelRequest" />
<meta itemprop="path" content="Stable" />
</div>

# google.generativeai.protos.CreateTunedModelRequest

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/googleapis/google-cloud-python/tree/main/packages/google-ai-generativelanguage/google/ai/generativelanguage_v1beta/types/model_service.py#L224-L251">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Request to create a TunedModel.

<!-- Placeholder for "Used in" -->




<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`tuned_model_id`<a id="tuned_model_id"></a>
</td>
<td>
`str`

Optional. The unique id for the tuned model if specified.
This value should be up to 40 characters, the first
character must be a letter, the last could be a letter or a
number. The id must match the regular expression:
`a-z <[a-z0-9-]{0,38}[a-z0-9]>`__?.

</td>
</tr><tr>
<td>
`tuned_model`<a id="tuned_model"></a>
</td>
<td>
`google.ai.generativelanguage.TunedModel`

Required. The tuned model to create.
</td>
</tr>
</table>



