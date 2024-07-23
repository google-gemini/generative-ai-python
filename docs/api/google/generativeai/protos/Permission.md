description: Permission resource grants user, group or the rest of the world access to the PaLM API resource (e.g.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="google.generativeai.protos.Permission" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="GranteeType"/>
<meta itemprop="property" content="Role"/>
</div>

# google.generativeai.protos.Permission

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/googleapis/google-cloud-python/tree/main/packages/google-ai-generativelanguage/google/ai/generativelanguage_v1beta/types/permission.py#L30-L138">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Permission resource grants user, group or the rest of the world access to the PaLM API resource (e.g.

<!-- Placeholder for "Used in" -->
 a tuned model,
corpus).

A role is a collection of permitted operations that allows users
to perform specific actions on PaLM API resources. To make them
available to users, groups, or service accounts, you assign
roles. When you assign a role, you grant permissions that the
role contains.

There are three concentric roles. Each role is a superset of the
previous role's permitted operations:

- reader can use the resource (e.g. tuned model, corpus) for
  inference
- writer has reader's permissions and additionally can edit and
  share
- owner has writer's permissions and additionally can delete





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

Output only. Identifier. The permission name. A unique name
will be generated on create. Examples:
tunedModels/{tuned_model}/permissions/{permission}
corpora/{corpus}/permissions/{permission} Output only.
</td>
</tr><tr>
<td>
`grantee_type`<a id="grantee_type"></a>
</td>
<td>
`google.ai.generativelanguage.Permission.GranteeType`

Optional. Immutable. The type of the grantee.

</td>
</tr><tr>
<td>
`email_address`<a id="email_address"></a>
</td>
<td>
`str`

Optional. Immutable. The email address of the
user of group which this permission refers.
Field is not set when permission's grantee type
is EVERYONE.

</td>
</tr><tr>
<td>
`role`<a id="role"></a>
</td>
<td>
`google.ai.generativelanguage.Permission.Role`

Required. The role granted by this
permission.

</td>
</tr>
</table>



## Child Classes
[`class GranteeType`](../../../google/generativeai/protos/Permission/GranteeType.md)

[`class Role`](../../../google/generativeai/protos/Permission/Role.md)

