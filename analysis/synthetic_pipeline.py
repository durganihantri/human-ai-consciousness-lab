"""Generate condition-independent synthetic UI test records and descriptive summaries.

Not participant data; not scientific evidence. Standard-library Python only.
"""
import argparse
import csv
import json
import random
from collections import Counter
from pathlib import Path

FIELDS = ('AG1', 'EX1', 'AN1', 'TR1')
PAIRS = ('A01', 'A02', 'A03')
CONDITIONS = ('impersonal', 'first_person')


def generate(n=60, seed=20261123):
    if n < 1:
        raise ValueError('n must be positive')
    rng = random.Random(seed)
    rows = []
    for i in range(n):
        row = {
            'record_type': 'synthetic_test_only',
            'test_id': f'TEST-{i+1:04d}',
            'pair_id': PAIRS[i % len(PAIRS)],
            'condition': CONDITIONS[(i // len(PAIRS)) % len(CONDITIONS)],
        }
        row.update({key: rng.randint(1, 7) for key in FIELDS})
        rows.append(row)
    rng.shuffle(rows)
    return rows


def summarize(rows):
    result = {'notice': 'SYNTHETIC TEST DATA ONLY — NOT EMPIRICAL FINDINGS',
              'count': len(rows), 'by_condition': {}}
    for condition in CONDITIONS:
        subset = [r for r in rows if r['condition'] == condition]
        result['by_condition'][condition] = {
            'n': len(subset),
            'mean_ratings': {k: round(sum(r[k] for r in subset) / len(subset), 3)
                             if subset else None for k in FIELDS},
            'scenarios': dict(Counter(r['pair_id'] for r in subset))}
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path('synthetic-output'))
    parser.add_argument('--n', type=int, default=60)
    parser.add_argument('--seed', type=int, default=20261123)
    args = parser.parse_args()
    rows = generate(args.n, args.seed)
    args.output.mkdir(parents=True, exist_ok=True)
    with (args.output / 'synthetic-records.csv').open('w', newline='', encoding='utf8') as f:
        writer = csv.DictWriter(f, fieldnames=['record_type', 'test_id', 'pair_id', 'condition', *FIELDS])
        writer.writeheader(); writer.writerows(rows)
    (args.output / 'synthetic-summary.json').write_text(json.dumps(summarize(rows), indent=2), encoding='utf8')
    print('Created SYNTHETIC test outputs:', args.output)


if __name__ == '__main__':
    main()

