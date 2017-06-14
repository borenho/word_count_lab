from collections import Counter


def words(maneno):
    
    return dict(Counter(maneno.replace(',', '').replace('.', '').split()))
        