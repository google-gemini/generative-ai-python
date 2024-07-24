description: Raw media bytes.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="google.generativeai.protos.Blob" />
<meta itemprop="path" content="Stable" />
</div>

# google.generativeai.protos.Blob

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/googleapis/google-cloud-python/tree/main/packages/google-ai-generativelanguage/google/ai/generativelanguage_v1beta/types/content.py#L206-L231">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Raw media bytes.

<!-- Placeholder for "Used in" -->

Text should not be sent as raw bytes, use the 'text' field.



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`mime_type`<a id="mime_type"></a>
</td>
<td>
`str`

The IANA standard MIME type of the source data. Examples:

-  image/png
-  image/jpeg If an unsupported MIME type is provided, an
   error will be returned. For a complete list of supported
   types, see `Supported file
   formats <https://ai.google.dev/gemini-api/docs/prompting_with_media#supported_file_formats>`__.
</td>
</tr><tr>
<td>
`data`<a id="data"></a>
</td>
<td>
`bytes`

Raw bytes for media formats.
</td>
</tr>
</table>



