"""Validate the checked-in notebook without running cells or downloading images."""

import ast
import json
from pathlib import Path
import unittest


NOTEBOOK = Path(__file__).resolve().parents[1] / "cervical-cytology-ml.ipynb"


class NotebookSourceTests(unittest.TestCase):
    def setUp(self):
        self.notebook = json.loads(NOTEBOOK.read_text(encoding="utf-8"))
        self.code = [
            (i, "".join(cell["source"]), cell)
            for i, cell in enumerate(self.notebook["cells"])
            if cell["cell_type"] == "code"
        ]

    def test_python_cells_parse(self):
        self.assertEqual(self.notebook["nbformat"], 4)
        self.assertTrue(self.code)
        for i, source, _ in self.code:
            with self.subTest(cell=i):
                python = "\n".join(
                    "" if line.startswith("%pip ") else line
                    for line in source.splitlines()
                )
                ast.parse(python, filename=f"{NOTEBOOK.name}:cell {i}")

    def test_notebook_has_no_saved_execution_outputs(self):
        for i, _, cell in self.code:
            with self.subTest(cell=i):
                self.assertIsNone(cell["execution_count"])
                self.assertEqual(cell["outputs"], [])


if __name__ == "__main__":
    unittest.main()
