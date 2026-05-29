"""Find repeated characters in a string."""

text = input('Enter a string: ').strip()
if not text:
    print('No input provided.')
else:
    counts = {}
    for ch in text:
        counts[ch] = counts.get(ch, 0) + 1

    repeated = [ch for ch, count in counts.items() if count > 1]
    if repeated:
        print('Repeated characters:', ' '.join(repeated))
    else:
        print('No repeated characters found.')
