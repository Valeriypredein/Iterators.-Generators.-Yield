class FlatIterator:

    def __init__(self, list_of_list):
        self.list = list_of_list
        self.new_list = []
        self.counter = 0


    def __iter__(self):
        return self

    def __next__(self):
        if self.counter >= len(self.list):
            if self.new_list:
                self.list, self.counter = self.new_list.pop()
                return next(self)
            else:
                raise StopIteration
        item = self.list[self.counter]
        self.counter += 1

        if type(item) is not list:
            return item
        else:
            self.new_list.append((self.list, self.counter))
            self.list = item
            self.counter = 0
            return next(self)


def test_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

    print(list(FlatIterator(list_of_lists_2)))

if __name__ == '__main__':
    test_3()