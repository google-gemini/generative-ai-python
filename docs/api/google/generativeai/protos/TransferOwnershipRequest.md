description: Request to transfer the ownership of the tuned model.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="google.generativeai.protos.TransferOwnershipRequest" />
<meta itemprop="path" content="Stable" />
</div>

# google.generativeai.protos.TransferOwnershipRequest

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/googleapis/google-cloud-python/tree/main/packages/google-ai-generativelanguage/google/ai/generativelanguage_v1beta/types/permission_service.py#L192-L213">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Request to transfer the ownership of the tuned model.

<!-- Placeholder for "Used in" -->




<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`name`<a id="name"></a>
</td>
<td>
`str`

Required. The resource name of the tuned model to transfer
ownership.

Format: ``tunedModels/my-model-id``
</td>
</tr><tr>
<td>
`email_address`<a id="email_address"></a>
</td>
<td>
`str`

Required. The email address of the user to
whom the tuned model is being transferred to.
</td>
</tr>
</table>



