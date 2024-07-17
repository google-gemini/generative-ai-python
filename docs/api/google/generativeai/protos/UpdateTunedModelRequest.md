description: Request to update a TunedModel.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="google.generativeai.protos.UpdateTunedModelRequest" />
<meta itemprop="path" content="Stable" />
</div>

# google.generativeai.protos.UpdateTunedModelRequest

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/googleapis/google-cloud-python/tree/main/packages/google-ai-generativelanguage/google/ai/generativelanguage_v1beta/types/model_service.py#L296-L315">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Request to update a TunedModel.

<!-- Placeholder for "Used in" -->




<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`tuned_model`<a id="tuned_model"></a>
</td>
<td>
`google.ai.generativelanguage.TunedModel`

Required. The tuned model to update.
</td>
</tr><tr>
<td>
`update_mask`<a id="update_mask"></a>
</td>
<td>
`google.protobuf.field_mask_pb2.FieldMask`

Required. The list of fields to update.
</td>
</tr>
</table>



