"""Split datasets into train and test partitions.

Usage example
-------------
>>> from datasci_ai.train_test_split import split
>>> train, test = split([1, 2, 3, 4], test_size=0.25, seed=1)
>>> len(test)
1
"""

from __future__ import annotations

import random
from typing import Sequence, TypeVar

T = TypeVar("T")

__all__ = ["split"]


def split(data: Sequence[T], *, test_size: float = 0.2, seed: int | None = None) -> tuple[list[T], list[T]]:
    """Return ``(train, test)`` partitions of ``data``."""

    if not 0 < test_size < 1:
        raise ValueError("test_size must be between 0 and 1")
    indices = list(range(len(data)))
    rng = random.Random(seed)
    rng.shuffle(indices)
    test_count = max(1, int(len(data) * test_size))
    test_idx = indices[:test_count]
    train_idx = indices[test_count:]
    train = [data[i] for i in train_idx]
    test = [data[i] for i in test_idx]
    return train, test
