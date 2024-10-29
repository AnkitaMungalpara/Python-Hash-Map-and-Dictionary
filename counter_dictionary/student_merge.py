from collections import defaultdict, Counter

def merge_with_defaultdict(*dicts):
    result = defaultdict(int)
    for d in dicts:
        for k, v in d.items():
            result[k]+=v
    return dict(result)



def merge_with_counter(*dicts):
    result = Counter()
    for d in dicts:
        result.update(d)
    return dict(result)


