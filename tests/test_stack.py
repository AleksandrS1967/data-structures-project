"""Здесь надо написать тесты с использованием unittest для модуля stack."""

import unittest

from src.stack import Stack
stack = Stack()


class TestStack(unittest.TestCase):
    def test_push(self):
        stack.push('data_1')
        self.assertEqual(stack.top.data, 'data_1')

    def test_pop(self):
        self.assertEqual(stack.pop(), None)
        stack.push('data_1')
        stack.push('data_2')
        stack.pop()
        self.assertEqual(stack.pop(), 'data_1')