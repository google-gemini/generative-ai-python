description: Request to create a Permission.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="google.generativeai.protos.CreatePermissionRequest" />
<meta itemprop="path" content="Stable" />
</div>

# google.generativeai.protos.CreatePermissionRequest

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/googleapis/google-cloud-python/tree/main/packages/google-ai-generativelanguage/google/ai/generativelanguage_v1beta/types/permission_service.py#L40-L59">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Request to create a ``Permission``.

<!-- Placeholder for "Used in" -->




<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`parent`<a id="parent"></a>
</td>
<td>
`str`

Required. The parent resource of the ``Permission``.
Formats: ``tunedModels/{tuned_model}`` ``corpora/{corpus}``
</td>
</tr><tr>
<td>
`permission`<a id="permission"></a>
</td>
<td>
`google.ai.generativelanguage.Permission`

Required. The permission to create.
</td>
</tr>
</table>



