# test_with_unittest.py

import math
import pytest

from LateRide import solution


def test_1():
  num = 240
  assert solution(num) == 4


def test_2():
  num = 808
  assert solution(num) == 14


def test_3():
  num = 1439
  assert solution(num) == 19


def test_4():
  num = 0
  assert solution(num) == 0


def test_5():
  num = 23
  assert solution(num) == 5


def test_6():
  num = 8
  assert solution(num) == 8
