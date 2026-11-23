"""Offline, synthetic preview only. No participant data collection or network use."""
import csv
import random
from pathlib import Path

STIMULI = Path(__file__).with_name('stimuli.csv')


def load_stimuli(path=STIMULI):
    with Path(path).open(encoding='utf-8', newline='') as f:
        rows = list(csv.DictReader(f))
    required = {'pair_id', 'scenario', 'user_prompt', 'control_text', 'treatment_text'}
    if not rows or not required.issubset(rows[0]):
        raise ValueError('Stimulus file is empty or missing required columns')
    if len({row['pair_id'] for row in rows}) != len(rows):
        raise ValueError('Duplicate pair IDs')
    return rows


def sample_preview(seed=42):
    rng = random.Random(seed)
    row = rng.choice(load_stimuli())
    condition = rng.choice(('control', 'treatment'))
    return {'pair_id': row['pair_id'], 'scenario': row['scenario'],
            'condition': condition, 'user_prompt': row['user_prompt'],
            'response': row[f'{condition}_text']}


if __name__ == '__main__':
    preview = sample_preview()
    print('SYNTHETIC TECHNICAL PREVIEW — NOT HUMAN RESEARCH')
    for key, value in preview.items():
        print(f'{key}: {value}')
