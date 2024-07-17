description: Content filtering metadata associated with processing a single request.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="google.generativeai.types.ContentFilterDict" />
<meta itemprop="path" content="Stable" />
</div>

# google.generativeai.types.ContentFilterDict

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/google/generative-ai-python/blob/master/google/generativeai/types/safety_types.py#L149-L153">
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



