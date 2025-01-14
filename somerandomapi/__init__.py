"""
**[UNFINISHED]** An API wrapper for somerandomapi.ml

License
-------
MIT License

Copyright (c) [year] [fullname]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from . import http
from .structures.welcome import welcome as Welcome
from .structures.animals import AnimalMeta as Animal
from .structures.animals import AnimalResponse
from .structures.anime import AnimeMeta as Anime
from .structures.anime import AnimeResponse
from .structures.filters import FilterMeta as Filter
from .structures.filters import (
    FilterData,
    FilterBrightness,
    FilterColor,
    FilterThreshold,
)


__all__ = [
    "Animal",
    "AnimalResponse",
    "Welcome",
    "Anime",
    "AnimeResponse",
    "Filter",
    "FilterData",
    "FilterBrightness",
    "FilterColor",
    "FilterThreshold",
]

#TODO
# # FilterData = NamedTuple("FilterData", "types", "names", "rows")

# __pdoc__ = {
#     "structures": False,
#     "http": False,
#     "constants": False,
#     "sync_async_handler": False,
# }