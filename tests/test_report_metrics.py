"""Check that the published comparison matches its held-out counts."""

from pathlib import Path
import re
import unittest


REPORT = Path(__file__).resolve().parents[1] / "research-report.md"
LABELS = [
    "Dyskeratotic",
    "Koilocytotic",
    "Metaplastic",
    "Parabasal",
    "Superficial-intermediate",
]


class PublishedResultsTests(unittest.TestCase):
    def test_holdout_metrics_match_the_confusion_matrix(self):
        report = REPORT.read_text(encoding="utf-8")
        lines = report.splitlines()
        header = next(i for i, line in enumerate(lines) if "| Actual" in line)
        self.assertEqual([part.strip() for part in lines[header].split("|")[2:-1]], LABELS)

        matrix = []
        for label, line in zip(LABELS, lines[header + 2 : header + 7], strict=True):
            row_label, *counts = [part.strip() for part in line.split("|")[1:-1]]
            self.assertEqual(row_label, label)
            self.assertEqual(len(counts), len(LABELS))
            matrix.append(list(map(int, counts)))

        support = [sum(row) for row in matrix]
        predicted = [sum(col) for col in zip(*matrix, strict=True)]
        correct_by_class = [row[i] for i, row in enumerate(matrix)]
        total = sum(support)
        correct = sum(correct_by_class)
        accuracy = correct / total
        balanced_accuracy = sum(tp / n for tp, n in zip(correct_by_class, support)) / len(LABELS)
        macro_f1 = sum(
            2 * tp / (actual + called)
            for tp, actual, called in zip(correct_by_class, support, predicted)
        ) / len(LABELS)

        headline = re.search(
            r"\*\*([\d.]+) macro F1\*\* on ([\d,]+) held-out crops, "
            r"with \*\*([\d.]+)% accuracy\*\* and \*\*([\d.]+)% balanced accuracy\*\*",
            report,
        )
        self.assertIsNotNone(headline, "Expected a results headline with all three metrics")
        f1, samples, acc, balanced = headline.groups()
        self.assertEqual(int(samples.replace(",", "")), total)
        self.assertEqual(f1, f"{macro_f1:.4f}")
        self.assertEqual(acc, f"{accuracy:.2%}".removesuffix("%"))
        self.assertEqual(balanced, f"{balanced_accuracy:.2%}".removesuffix("%"))
        self.assertIn(f"{correct} correct predictions and {total - correct} errors", report)


if __name__ == "__main__":
    unittest.main()
