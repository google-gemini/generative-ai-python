description: Supported programming languages for the generated code.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="google.generativeai.protos.ExecutableCode.Language" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__abs__"/>
<meta itemprop="property" content="__add__"/>
<meta itemprop="property" content="__and__"/>
<meta itemprop="property" content="__bool__"/>
<meta itemprop="property" content="__eq__"/>
<meta itemprop="property" content="__floordiv__"/>
<meta itemprop="property" content="__ge__"/>
<meta itemprop="property" content="__gt__"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__invert__"/>
<meta itemprop="property" content="__le__"/>
<meta itemprop="property" content="__lshift__"/>
<meta itemprop="property" content="__lt__"/>
<meta itemprop="property" content="__mod__"/>
<meta itemprop="property" content="__mul__"/>
<meta itemprop="property" content="__ne__"/>
<meta itemprop="property" content="__neg__"/>
<meta itemprop="property" content="__new__"/>
<meta itemprop="property" content="__or__"/>
<meta itemprop="property" content="__pos__"/>
<meta itemprop="property" content="__pow__"/>
<meta itemprop="property" content="__radd__"/>
<meta itemprop="property" content="__rand__"/>
<meta itemprop="property" content="__rfloordiv__"/>
<meta itemprop="property" content="__rlshift__"/>
<meta itemprop="property" content="__rmod__"/>
<meta itemprop="property" content="__rmul__"/>
<meta itemprop="property" content="__ror__"/>
<meta itemprop="property" content="__rpow__"/>
<meta itemprop="property" content="__rrshift__"/>
<meta itemprop="property" content="__rshift__"/>
<meta itemprop="property" content="__rsub__"/>
<meta itemprop="property" content="__rtruediv__"/>
<meta itemprop="property" content="__rxor__"/>
<meta itemprop="property" content="__sub__"/>
<meta itemprop="property" content="__truediv__"/>
<meta itemprop="property" content="__xor__"/>
<meta itemprop="property" content="as_integer_ratio"/>
<meta itemprop="property" content="bit_count"/>
<meta itemprop="property" content="bit_length"/>
<meta itemprop="property" content="conjugate"/>
<meta itemprop="property" content="from_bytes"/>
<meta itemprop="property" content="to_bytes"/>
<meta itemprop="property" content="LANGUAGE_UNSPECIFIED"/>
<meta itemprop="property" content="PYTHON"/>
</div>

# google.generativeai.protos.ExecutableCode.Language

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/googleapis/google-cloud-python/tree/main/packages/google-ai-generativelanguage/google/ai/generativelanguage_v1beta/types/content.py#L270-L282">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Supported programming languages for the generated code.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>google.generativeai.protos.ExecutableCode.Language(
    *args, **kwds
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Values</h2></th></tr>

<tr>
<td>
`LANGUAGE_UNSPECIFIED`<a id="LANGUAGE_UNSPECIFIED"></a>
</td>
<td>
`0`

Unspecified language. This value should not
be used.
</td>
</tr><tr>
<td>
`PYTHON`<a id="PYTHON"></a>
</td>
<td>
`1`

Python >= 3.10, with numpy and simpy
available.
</td>
</tr>
</table>





<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`denominator`<a id="denominator"></a>
</td>
<td>
the denominator of a rational number in lowest terms
</td>
</tr><tr>
<td>
`imag`<a id="imag"></a>
</td>
<td>
the imaginary part of a complex number
</td>
</tr><tr>
<td>
`numerator`<a id="numerator"></a>
</td>
<td>
the numerator of a rational number in lowest terms
</td>
</tr><tr>
<td>
`real`<a id="real"></a>
</td>
<td>
the real part of a complex number
</td>
</tr>
</table>



## Methods

<h3 id="as_integer_ratio"><code>as_integer_ratio</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>as_integer_ratio()
</code></pre>

Return integer ratio.

Return a pair of integers, whose ratio is exactly equal to the original int
and with a positive denominator.

```
>>> (10).as_integer_ratio()
(10, 1)
>>> (-10).as_integer_ratio()
(-10, 1)
>>> (0).as_integer_ratio()
(0, 1)
```

<h3 id="bit_count"><code>bit_count</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>bit_count()
</code></pre>

Number of ones in the binary representation of the absolute value of self.

Also known as the population count.

```
>>> bin(13)
'0b1101'
>>> (13).bit_count()
3
```

<h3 id="bit_length"><code>bit_length</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>bit_length()
</code></pre>

Number of bits necessary to represent self in binary.

```
>>> bin(37)
'0b100101'
>>> (37).bit_length()
6
```

<h3 id="conjugate"><code>conjugate</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>conjugate()
</code></pre>

Returns self, the complex conjugate of any int.


<h3 id="from_bytes"><code>from_bytes</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>from_bytes(
    byteorder=&#x27;big&#x27;, *, signed=False
)
</code></pre>

Return the integer represented by the given array of bytes.

bytes
  Holds the array of bytes to convert.  The argument must either
  support the buffer protocol or be an iterable object producing bytes.
  Bytes and bytearray are examples of built-in objects that support the
  buffer protocol.
byteorder
  The byte order used to represent the integer.  If byteorder is 'big',
  the most significant byte is at the beginning of the byte array.  If
  byteorder is 'little', the most significant byte is at the end of the
  byte array.  To request the native byte order of the host system, use
  `sys.byteorder' as the byte order value.  Default is to use 'big'.
signed
  Indicates whether two's complement is used to represent the integer.

<h3 id="to_bytes"><code>to_bytes</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>to_bytes(
    length=1, byteorder=&#x27;big&#x27;, *, signed=False
)
</code></pre>

Return an array of bytes representing an integer.

length
  Length of bytes object to use.  An OverflowError is raised if the
  integer is not representable with the given number of bytes.  Default
  is length 1.
byteorder
  The byte order used to represent the integer.  If byteorder is 'big',
  the most significant byte is at the beginning of the byte array.  If
  byteorder is 'little', the most significant byte is at the end of the
  byte array.  To request the native byte order of the host system, use
  `sys.byteorder' as the byte order value.  Default is to use 'big'.
signed
  Determines whether two's complement is used to represent the integer.
  If signed is False and a negative integer is given, an OverflowError
  is raised.

<h3 id="__abs__"><code>__abs__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__abs__()
</code></pre>

abs(self)


<h3 id="__add__"><code>__add__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__add__(
    value, /
)
</code></pre>

Return self+value.


<h3 id="__and__"><code>__and__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__and__(
    value, /
)
</code></pre>

Return self&value.


<h3 id="__bool__"><code>__bool__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__bool__()
</code></pre>

True if self else False


<h3 id="__eq__"><code>__eq__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__eq__(
    other
)
</code></pre>

Return self==value.


<h3 id="__floordiv__"><code>__floordiv__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__floordiv__(
    value, /
)
</code></pre>

Return self//value.


<h3 id="__ge__"><code>__ge__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__ge__(
    other
)
</code></pre>

Return self>=value.


<h3 id="__gt__"><code>__gt__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__gt__(
    other
)
</code></pre>

Return self>value.


<h3 id="__invert__"><code>__invert__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__invert__()
</code></pre>

~self


<h3 id="__le__"><code>__le__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__le__(
    other
)
</code></pre>

Return self<=value.


<h3 id="__lshift__"><code>__lshift__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__lshift__(
    value, /
)
</code></pre>

Return self<<value.


<h3 id="__lt__"><code>__lt__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__lt__(
    other
)
</code></pre>

Return self<value.


<h3 id="__mod__"><code>__mod__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__mod__(
    value, /
)
</code></pre>

Return self%value.


<h3 id="__mul__"><code>__mul__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__mul__(
    value, /
)
</code></pre>

Return self*value.


<h3 id="__ne__"><code>__ne__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__ne__(
    other
)
</code></pre>

Return self!=value.


<h3 id="__neg__"><code>__neg__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__neg__()
</code></pre>

-self


<h3 id="__or__"><code>__or__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__or__(
    value, /
)
</code></pre>

Return self|value.


<h3 id="__pos__"><code>__pos__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__pos__()
</code></pre>

+self


<h3 id="__pow__"><code>__pow__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__pow__(
    value, mod, /
)
</code></pre>

Return pow(self, value, mod).


<h3 id="__radd__"><code>__radd__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__radd__(
    value, /
)
</code></pre>

Return value+self.


<h3 id="__rand__"><code>__rand__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__rand__(
    value, /
)
</code></pre>

Return value&self.


<h3 id="__rfloordiv__"><code>__rfloordiv__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__rfloordiv__(
    value, /
)
</code></pre>

Return value//self.


<h3 id="__rlshift__"><code>__rlshift__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__rlshift__(
    value, /
)
</code></pre>

Return value<<self.


<h3 id="__rmod__"><code>__rmod__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__rmod__(
    value, /
)
</code></pre>

Return value%self.


<h3 id="__rmul__"><code>__rmul__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__rmul__(
    value, /
)
</code></pre>

Return value*self.


<h3 id="__ror__"><code>__ror__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__ror__(
    value, /
)
</code></pre>

Return value|self.


<h3 id="__rpow__"><code>__rpow__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__rpow__(
    value, mod, /
)
</code></pre>

Return pow(value, self, mod).


<h3 id="__rrshift__"><code>__rrshift__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__rrshift__(
    value, /
)
</code></pre>

Return value>>self.


<h3 id="__rshift__"><code>__rshift__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__rshift__(
    value, /
)
</code></pre>

Return self>>value.


<h3 id="__rsub__"><code>__rsub__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__rsub__(
    value, /
)
</code></pre>

Return value-self.


<h3 id="__rtruediv__"><code>__rtruediv__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__rtruediv__(
    value, /
)
</code></pre>

Return value/self.


<h3 id="__rxor__"><code>__rxor__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__rxor__(
    value, /
)
</code></pre>

Return value^self.


<h3 id="__sub__"><code>__sub__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__sub__(
    value, /
)
</code></pre>

Return self-value.


<h3 id="__truediv__"><code>__truediv__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__truediv__(
    value, /
)
</code></pre>

Return self/value.


<h3 id="__xor__"><code>__xor__</code></h3>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__xor__(
    value, /
)
</code></pre>

Return self^value.






<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Class Variables</h2></th></tr>

<tr>
<td>
LANGUAGE_UNSPECIFIED<a id="LANGUAGE_UNSPECIFIED"></a>
</td>
<td>
`<Language.LANGUAGE_UNSPECIFIED: 0>`
</td>
</tr><tr>
<td>
PYTHON<a id="PYTHON"></a>
</td>
<td>
`<Language.PYTHON: 1>`
</td>
</tr>
</table>

