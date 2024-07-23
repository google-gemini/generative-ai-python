description: Request to update the Permission.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="google.generativeai.protos.UpdatePermissionRequest" />
<meta itemprop="path" content="Stable" />
</div>

# google.generativeai.protos.UpdatePermissionRequest

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/googleapis/google-cloud-python/tree/main/packages/google-ai-generativelanguage/google/ai/generativelanguage_v1beta/types/permission_service.py#L149-L173">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Request to update the ``Permission``.

<!-- Placeholder for "Used in" -->




<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`permission`<a id="permission"></a>
</td>
<td>
`google.ai.generativelanguage.Permission`

Required. The permission to update.

The permission's ``name`` field is used to identify the
permission to update.
</td>
</tr><tr>
<td>
`update_mask`<a id="update_mask"></a>
</td>
<td>
`google.protobuf.field_mask_pb2.FieldMask`

Required. The list of fields to update. Accepted ones:

-  role (<a href="../../../google/generativeai/protos/Permission.md#role"><code>Permission.role</code></a> field)
</td>
</tr>
</table>



