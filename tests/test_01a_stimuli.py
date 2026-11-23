"""Run with: python -m unittest discover -s tests -v"""
import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
MODULE = ROOT / 'experiments' / '01a-first-person' / 'technical_preview.py'
spec = importlib.util.spec_from_file_location('technical_preview', MODULE)
preview = importlib.util.module_from_spec(spec)
spec.loader.exec_module(preview)


class StimulusTests(unittest.TestCase):
    def test_three_pairs(self):
        self.assertEqual(len(preview.load_stimuli()), 3)

    def test_unique_ids_and_nonempty_text(self):
        rows = preview.load_stimuli()
        self.assertEqual(len({r['pair_id'] for r in rows}), len(rows))
        for row in rows:
            for field in ('user_prompt', 'control_text', 'treatment_text'):
                self.assertTrue(row[field].strip())

    def test_first_person_only_in_treatment(self):
        for row in preview.load_stimuli():
            self.assertTrue(row['treatment_text'].startswith('I suggest '))
            self.assertNotIn('I suggest ', row['control_text'])

    def test_preview_deterministic(self):
        self.assertEqual(preview.sample_preview(seed=7), preview.sample_preview(seed=7))


if __name__ == '__main__':
    unittest.main()
