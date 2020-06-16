"""Solution to 16.12 XML Encoding.

Since XML is very verbose, you are given a way of encoding it where each
tag gets mapped to a pre-defined integer value. The language/grammar is
as follows:

```
Element   -> Tag Attributes END Children END
Attribute -> Tag Value
END       -> 0
Tag       -> some predefined mapping to int
Value     -> string value
```

For example, the following XML might be converted into the compressed
string below (assuming a mapping of `family` -> 1, `person` -> 2,
`firstName` -> 3, `lastName -> 4`, `state` -> 5).

```
<family lastName="McDowell" state="CA">
    <person firstName="Gayle">Some Message</person>
</family>
```

Becomes:
`1 4 McDowell 5 CA 0 2 3 Gayle 0 Some Message 0 0`

Write code to print the encoded version of an XML element (passed in
`Element` and `Attribute` objects).
"""

from __future__ import annotations

import dataclasses
from typing import List, Optional

END = '0'


@dataclasses.dataclass
class Element:
    """An XML Element. Children are ignored if value is not None."""
    tag: int
    attributes: List[Attribute] = dataclasses.field(default_factory=list)
    value: Optional[str] = None
    children: List[Element] = dataclasses.field(default_factory=list)


@dataclasses.dataclass
class Attribute:
    """An XML Attribute."""
    tag: int
    value: str


def encode(element: Element) -> str:
    """Returns the encoded version of given XML element."""
    res = [str(element.tag)]
    res.extend(_encode_attribute(attribute)
               for attribute in element.attributes)
    res.append(END)
    if element.value is None:
        res.extend(encode(child) for child in element.children)
    else:
        res.append(element.value)
    res.append(END)
    return ' '.join(res)


def _encode_attribute(attribute: Attribute) -> str:
    return str(attribute.tag) + ' ' + attribute.value
