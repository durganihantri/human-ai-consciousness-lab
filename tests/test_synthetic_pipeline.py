"""Run from repo root: python -m unittest discover -s tests -v"""
import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('synthetic_pipeline', ROOT / 'analysis' / 'synthetic_pipeline.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

class SyntheticPipelineTests(unittest.TestCase):
    def test_reproducible(self):
        self.assertEqual(module.generate(24, 7), module.generate(24, 7))
    def test_no_personal_data(self):
        for row in module.generate(12):
            self.assertEqual(row['record_type'], 'synthetic_test_only')
            self.assertEqual(set(row), {'record_type', 'test_id', 'pair_id', 'condition', *module.FIELDS})
    def test_balanced_by_condition(self):
        rows = module.generate(60)
        summary = module.summarize(rows)
        self.assertEqual(summary['by_condition']['impersonal']['n'], 30)
        self.assertEqual(summary['by_condition']['first_person']['n'], 30)
    def test_bounds(self):
        for row in module.generate(120):
            self.assertTrue(all(1 <= row[key] <= 7 for key in module.FIELDS))
    def test_bad_n(self):
        with self.assertRaises(ValueError):
            module.generate(0)
