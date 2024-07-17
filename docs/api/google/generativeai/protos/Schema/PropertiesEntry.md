description: The abstract base class for a message.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="google.generativeai.protos.Schema.PropertiesEntry" />
<meta itemprop="path" content="Stable" />
</div>

# google.generativeai.protos.Schema.PropertiesEntry

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/googleapis/google-cloud-python/tree/main/packages/google-ai-generativelanguage/google/ai/generativelanguage_v1beta/types/content.py">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



The abstract base class for a message.

<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>
<tr class="alt">
<td colspan="2">
mapping (Union[dict, ~.Message]): A dictionary or message to be
used to determine the values for this message.
</td>
</tr>
<tr>
<td>
`ignore_unknown_fields`<a id="ignore_unknown_fields"></a>
</td>
<td>
`Optional(bool`

If True, do not raise errors for
    unknown fields. Only applied if `mapping` is a mapping type or there
    are keyword parameters.
</td>
</tr><tr>
<td>
`kwargs`<a id="kwargs"></a>
</td>
<td>
`dict`

Keys and values corresponding to the fields of the
    message.
</td>
</tr>
</table>





<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`key`<a id="key"></a>
</td>
<td>
`string key`
</td>
</tr><tr>
<td>
`value`<a id="value"></a>
</td>
<td>
`Schema value`
</td>
</tr>
</table>



