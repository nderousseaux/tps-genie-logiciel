# -*- coding: utf-8 -*-
from unittest import TestCase
from unittest.mock import Mock
from solver import ProblemSolver


class ProblemSolverTest(TestCase):
    def setUp(self):
        mock_convert = Mock()
        mock_convert.convert.return_value = ''

        mock_display = Mock()

        self.solver = ProblemSolver(mock_convert, mock_display)

    def tearDown(self):
        self.solver = None

    def test_fizz_buzz(self):
        self.solver.solve()
        assert self.solver.converter.convert.call_count == 100
