#!/usr/bin/env python3
# thoth-solver
# Copyright(C) 2018 - 2021 Fridolin Pokorny
#
# This program is free software: you can redistribute it and / or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

"""Thoth's solver package."""

from .python import get_ecosystem_solver
from .python import PythonDependencyParser
from .python import PythonReleasesFetcher
from .python import PythonSolver
from .python import resolve

__version__ = "1.10.3"
__title__ = "thoth-solver"
__author__ = "Fridolin Pokorny"

__all__ = ["resolve", "get_ecosystem_solver", "PythonDependencyParser", "PythonReleasesFetcher", "PythonSolver"]
