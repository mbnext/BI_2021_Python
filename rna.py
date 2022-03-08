class Rna:
    def __init__(self, sequence: str):
        self.sequence = sequence
        self.i = 0
        for letter in set(self.sequence):
            if letter not in 'AUGCaugc':
                raise NameError("Your sequence contains wrong letter " + letter)

    def __repr__(self):
        return self.sequence

    def gc_content(self):
        n = len(self.sequence)
        counter = 0
        for letter in self.sequence:
            if letter in 'GCgc':
                counter += 1
        gc_content_value = counter / n
        return gc_content_value

    def reverse_complement(self):
        rna_complement_dict = {'A': 'U', 'U': 'A', 'C': 'G', 'G': 'C',
                               'a': 'u', 'u': 'a', 'c': 'g', 'g': 'c'}
        reverse_complement_sequence = ''
        reversed_seq = reversed(self.sequence)
        for letter in reversed_seq:
            reverse_complement_sequence += rna_complement_dict[letter]
        return reverse_complement_sequence

    def __iter__(self):
        return self

    def __next__(self):
        while self.i <= len(self.sequence) - 1:
            res = self.sequence[self.i]
            self.i += 1
            return res
        raise StopIteration

    def __eq__(self, other):
        if not isinstance(other, Rna):
            return NotImplemented
        return self.sequence == other.sequence

    def __hash__(self):
        return hash(self.sequence)
