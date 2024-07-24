description: Content filtering metadata associated with processing a single request.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="google.generativeai.protos.ContentFilter" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="BlockedReason"/>
</div>

# google.generativeai.protos.ContentFilter

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/googleapis/google-cloud-python/tree/main/packages/google-ai-generativelanguage/google/ai/generativelanguage_v1beta/types/safety.py#L83-L128">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Content filtering metadata associated with processing a single request.

<!-- Placeholder for "Used in" -->
ContentFilter contains a reason and an optional supporting
string. The reason may be unspecified.





<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`reason`<a id="reason"></a>
</td>
<td>
`google.ai.generativelanguage.ContentFilter.BlockedReason`

The reason content was blocked during request
processing.
</td>
</tr><tr>
<td>
`message`<a id="message"></a>
</td>
<td>
`str`

A string that describes the filtering
behavior in more detail.

</td>
</tr>
</table>



## Child Classes
[`class BlockedReason`](../../../google/generativeai/types/BlockedReason.md)

