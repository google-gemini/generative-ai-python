description: Captures default client configuration.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="google.generativeai.configure" />
<meta itemprop="path" content="Stable" />
</div>

# google.generativeai.configure

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/google/generative-ai-python/blob/master/google/generativeai/client.py#L273-L312">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Captures default client configuration.


<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>google.generativeai.configure(
    *,
    api_key: (str | None) = None,
    credentials: (ga_credentials.Credentials | dict | None) = None,
    transport: (str | None) = None,
    client_options: (client_options_lib.ClientOptions | dict | None) = None,
    client_info: (gapic_v1.client_info.ClientInfo | None) = None,
    default_metadata: Sequence[tuple[str, str]] = ()
)
</code></pre>



<!-- Placeholder for "Used in" -->

If no API key has been provided (either directly, or on `client_options`) and the
`GOOGLE_API_KEY` environment variable is set, it will be used as the API key.

Note: Not all arguments are detailed below. Refer to the `*ServiceClient` classes in
`google.ai.generativelanguage` for details on the other arguments.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`transport`<a id="transport"></a>
</td>
<td>
A string, one of: [`rest`, `grpc`, `grpc_asyncio`].
</td>
</tr><tr>
<td>
`api_key`<a id="api_key"></a>
</td>
<td>
The API-Key to use when creating the default clients (each service uses
a separate client). This is a shortcut for `client_options={"api_key": api_key}`.
If omitted, and the `GOOGLE_API_KEY` environment variable is set, it will be
used.
</td>
</tr><tr>
<td>
`default_metadata`<a id="default_metadata"></a>
</td>
<td>
Default (key, value) metadata pairs to send with every request.
when using `transport="rest"` these are sent as HTTP headers.
</td>
</tr>
</table>

