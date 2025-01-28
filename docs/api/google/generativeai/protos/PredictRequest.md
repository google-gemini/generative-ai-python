
# google.generativeai.protos.PredictRequest

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent">
<td>
  <a target="_blank" href="https://github.com/googleapis/google-cloud-python/tree/main/packages/google-ai-generativelanguage/google/ai/generativelanguage_v1beta/types/prediction_service.py#L32-L61">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Request message for [PredictionService.Predict][google.ai.generativelanguage.v1beta.PredictionService.Predict].

<!-- Placeholder for "Used in" -->




<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>

`model`<a id="model"></a>

</td>
<td>

`str`

Required. The name of the model for prediction. Format:
``name=models/{model}``.

</td>
</tr><tr>
<td>

`instances`<a id="instances"></a>

</td>
<td>

`MutableSequence[google.protobuf.struct_pb2.Value]`

Required. The instances that are the input to
the prediction call.

</td>
</tr><tr>
<td>

`parameters`<a id="parameters"></a>

</td>
<td>

`google.protobuf.struct_pb2.Value`

Optional. The parameters that govern the
prediction call.

</td>
</tr>
</table>



