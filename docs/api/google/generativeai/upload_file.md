description: Calls the API to upload a file using a supported file service.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="google.generativeai.upload_file" />
<meta itemprop="path" content="Stable" />
</div>

# google.generativeai.upload_file

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/google/generative-ai-python/blob/master/google/generativeai/files.py#L34-L74">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Calls the API to upload a file using a supported file service.


<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>google.generativeai.upload_file(
    path: (str | pathlib.Path | os.PathLike),
    *,
    mime_type: (str | None) = None,
    name: (str | None) = None,
    display_name: (str | None) = None,
    resumable: bool = True
) -> file_types.File
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`path`<a id="path"></a>
</td>
<td>
The path to the file to be uploaded.
</td>
</tr><tr>
<td>
`mime_type`<a id="mime_type"></a>
</td>
<td>
The MIME type of the file. If not provided, it will be
inferred from the file extension.
</td>
</tr><tr>
<td>
`name`<a id="name"></a>
</td>
<td>
The name of the file in the destination (e.g., 'files/sample-image').
If not provided, a system generated ID will be created.
</td>
</tr><tr>
<td>
`display_name`<a id="display_name"></a>
</td>
<td>
Optional display name of the file.
</td>
</tr><tr>
<td>
`resumable`<a id="resumable"></a>
</td>
<td>
Whether to use the resumable upload protocol. By default, this is enabled.
See details at
https://googleapis.github.io/google-api-python-client/docs/epy/googleapiclient.http.MediaFileUpload-class.html#resumable
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>

<tr>
<td>
`file_types.File`<a id="file_types.File"></a>
</td>
<td>
The response of the uploaded file.
</td>
</tr>
</table>

