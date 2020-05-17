"""Definition of a basic tree node for use in chapter 4 solutions."""

from collections import namedtuple
from typing import Optional


TreeNode = namedtuple('TreeNode', ['value', 'left', 'right'])


Tree = Optional[TreeNode]
