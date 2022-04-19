import unittest


class LinkedListItem:
    def __init__(self, value):
        self.value = value
        self.__next = None

    def get_next(self):
        return self.__next

    def set_next(self, next_item):
        self.__next = next_item

    def has_next(self):
        return self.__next is not None


class LinkedList:
    # без изменений
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__len = 0

    # без изменений
    def __getitem__(self, index):
        current = self.__head
        for _ in range(index):
            if current is None or current.has_next() is False:
                raise IndexError
            current = current.get_next()
        return current.value

    # без изменений
    def __len__(self):
        return self.__len

    # добавлено добавление по указанному индексу
    # 3. Добавить в методы `add` и `add_all` , поддержку вставки по произвольному индексу (опциональный второй параметр).
    # Например имея список: `[1, 2, 3, 4]`  вставка другого списка (`[5, 6]`) через `add_all` по индексу 1 приведет
    # к результату - `[1, 5, 6, 2, 3, 4]`
    def add(self, value, index=None):
        self.__len += 1
        new_item = LinkedListItem(value)
        if index is None:
            if not self.__head:
                self.__head = new_item
            else:
                self.__tail.set_next(new_item)
            self.__tail = new_item
        else:
            if index < 0 or index > self.__len - 1:
                raise IndexError("The index should be between 0 and the length of the list")
            elif index == 0:
                current = self.__head
                self.__head = new_item
                new_item.set_next(current.get_next())
            else:
                current = self.__head
                # идем до позиции вставки
                for _ in range(1, index):
                    current = current.get_next()
                # когда дошли до позиции вставки
                new_item.set_next(current.get_next())
                current.set_next(new_item)
                current = new_item
                # а дальше по идее ничего не меняется
        return self

    # без изменений
    def first(self):
        return self.__head.value

    # без изменений
    def last(self):
        return self.__tail.value

    # Возможность поиска наличия элемента через ключевое слово in
    def __contains__(self, value):
        current = self.__head
        while current:
            if current.value == value:
                return True
            current = current.get_next()
        return False

    # 2. Возможность добавления сразу нескольких элементов, метод можно назвать `add_all` или `extend`
    def add_all(self, values, index=None):
        if index is None:
            for value in values:
                self.__len += 1
                new_item = LinkedListItem(value)
                if not self.__head:
                    self.__head = new_item
                else:
                    self.__tail.set_next(new_item)
                self.__tail = new_item
        else:
            if index < 0 or index > self.__len - 1:
                raise IndexError("The index should be between 0 and the length of the list")
            current = self.__head
            # идем до позиции вставки
            for _ in range(1, index):
                current = current.get_next()
            # когда дошли до позиции вставки
            for value in values:
                self.__len += 1
                new_item = LinkedListItem(value)
                new_item.set_next(current.get_next())
                current.set_next(new_item)
                current = new_item
            # а дальше по идее ничего не меняется
        return self

    # 4. Добавить поддержку удаления элементов, метод `pop` , который может опционально принимать индекс удаляемого элемента.
    def pop(self, index=None):
        if index is None:
            current = self.__head
            item_to_pop = self.__tail
            # идем сначала до предпоследней позиции
            for _ in range(self.__len-2):
                current = current.get_next()
            self.__tail = current
            self.__len -= 1
        else:
            if index < 0 or index > self.__len - 1:
                raise IndexError("The index should be between 0 and the length of the list")
            elif index == 0:
                current = self.__head
                item_to_pop = self.__head
                self.__head = current.get_next()
                self.__len -= 1
            else:
                current = self.__head
                item_before = self.__head
                # идем сначала до индекса удаления
                for _ in range(index):
                    item_before = current
                    current = current.get_next()
                # дошли до позиции удаления
                item_to_pop = current
                current = item_before.set_next(item_to_pop.get_next())
                self.__len -= 1
                # дальше ничего не меняется
        return item_to_pop.value

    # 5. Добавить метод `remove_last_occurence` удаляющий последнее вхождение элемента в список.
    def remove_last_occurence(self, value):
        if value not in self:
            raise ValueError("There is no such value in the list")
        else:
            last_found_index = 0
            current = self.__head
            for i in range(self.__len):
                if current.value == value:
                    last_found_index = i
                    current = current.get_next()
                else:
                    current = current.get_next()
            item_to_delete = self.pop(index=last_found_index)
        return self


# тесты


class TestLinkedList(unittest.TestCase):
    def test_init(self):
        self.linked_list = LinkedList()
        self.assertEqual(self.linked_list.__len__(), 0, "Initial length should be 0")

    def test_add(self):
        self.linked_list = LinkedList()
        self.assertEqual(self.linked_list.__len__(), 0, "Initial length should be 0")
        self.linked_list.add('Richard')
        self.assertEqual(self.linked_list.__len__(), 1, "Length after the 1st addition should be 1")
        self.assertEqual(self.linked_list[0], 'Richard', "First element after the 1st addition should be 'Richard'")
        self.linked_list.add('Of')
        self.assertEqual(self.linked_list.__len__(), 2, "Length after the 2nd addition should be 2")
        self.assertEqual(self.linked_list[0], 'Richard', "First element after the 2nd addition should be 'Richard'")
        self.assertEqual(self.linked_list[1], 'Of', "Second element after the 2nd addition should be 'Of'")
        self.linked_list.add('Vain')
        self.assertEqual(self.linked_list.__len__(), 3, "Length after the 3rd addition should be 3")
        self.assertEqual(self.linked_list[0], 'Richard', "First element after the 3rd addition should be 'Richard'")
        self.assertEqual(self.linked_list[1], 'Of', "Second element after the 3rd addition should be 'Of'")
        self.assertEqual(self.linked_list[2], 'Vain', "Third element after the 3rd addition should be 'Vain'")
        self.linked_list.add('York Gave Battle in ', index=2)
        self.assertEqual(self.linked_list.__len__(), 4, "Length after the 4th addition should be 3")
        self.assertEqual(self.linked_list[0], 'Richard', "First element after the 4th addition should be 'Richard'")
        self.assertEqual(self.linked_list[1], 'Of', "Second element after the 4th addition should be 'Of'")
        self.assertEqual(self.linked_list[2], 'York Gave Battle in ',
                         "Third element after the 4th addition should be 'York Gave Battle in '")
        self.assertEqual(self.linked_list[3], 'Vain',
                         "Forth element after the 4th addition should be 'Vain'")

    def test_add_all(self):
        self.linked_list = LinkedList()
        self.assertEqual(self.linked_list.__len__(), 0, "Initial length should be zero")
        self.linked_list.add_all([1, 10, 100])
        self.assertEqual(self.linked_list.__len__(), 3, "Length after the 1st extension should be 3")
        self.assertEqual(self.linked_list[0], 1, "First element after the 1st extension should be 1")
        self.assertEqual(self.linked_list[1], 10, "Second element after the 1st extension should be 10")
        self.assertEqual(self.linked_list[2], 100, "Third element after the 1st extension should be 100")
        self.linked_list.add_all(['1', '10', 'one hundred'])
        self.assertEqual(self.linked_list.__len__(), 6, "Length after the 2nd extension should be 6")
        self.assertEqual(self.linked_list[0], 1, "First element after the 2nd extension should be 1")
        self.assertEqual(self.linked_list[1], 10, "Second element after the 2nd extension should be 10")
        self.assertEqual(self.linked_list[2], 100, "Third element after the 2nd extension should be 100")
        self.assertEqual(self.linked_list[3], '1', "Forth element after the 2nd extension should be 1 as string")
        self.assertEqual(self.linked_list[4], '10', "Fifth element after the 2nd extension should be 10 as string")
        self.assertEqual(self.linked_list[5], 'one hundred',
                         "Sixth element after the 2nd extension should be 'one hundred'")
        self.linked_list.add_all([1000, 10000, 'million'], 5)
        self.assertEqual(self.linked_list.__len__(), 9, "Length after the 3rd extension should be 9")
        self.assertEqual(self.linked_list[0], 1, "First element after the 3rd extension should be 1")
        self.assertEqual(self.linked_list[1], 10, "Second element after the 3rd extension should be 10")
        self.assertEqual(self.linked_list[2], 100, "Third element after the 3rd extension should be 100")
        self.assertEqual(self.linked_list[3], '1', "Forth element after the 3rd extension should be 1 as string")
        self.assertEqual(self.linked_list[4], '10', "Fifth element after the 3rd extension should be 10 as string")
        self.assertEqual(self.linked_list[5], 1000, "Sixth element after the 3rd extension should be 1000")
        self.assertEqual(self.linked_list[6], 10000, "Seventh element after the 3rd extension should be 10000")
        self.assertEqual(self.linked_list[7], 'million', "Eighth element after the 3rd extension should be 'million'")
        self.assertEqual(self.linked_list[8], 'one hundred',
                         "Ninth element after the 3rd extension should be 'one hundred'")

    def test_in(self):
        self.linked_list = LinkedList()
        self.linked_list.add(1)
        self.linked_list.add(10)
        self.linked_list.add(100)
        self.assertEqual(1 in self.linked_list, True, "1 is in the list")
        self.assertEqual(0 in self.linked_list, False, "Only 1, 10 and 100 should be in the list")

    def test_pop(self):
        self.linked_list = LinkedList()
        self.linked_list.add(1)
        self.linked_list.add(10)
        self.linked_list.add(100)
        self.linked_list.add(1000)
        self.assertEqual(self.linked_list.__len__(), 4, "Length should be 4")
        self.assertEqual(1 in self.linked_list, True,
                         "After inserting 1 into the list, we have to find it there")
        self.assertEqual(10 in self.linked_list, True,
                         "After inserting 10 into the list, we have to find it there")
        self.assertEqual(100 in self.linked_list, True,
                         "After inserting 100 into the list, we have to find it there")
        self.assertEqual(1000 in self.linked_list, True,
                         "After inserting 1000 into the list, we have to find it there")
        self.assertEqual(self.linked_list.pop(1), 10, "If we pop the second element we should get 10")
        self.assertEqual(self.linked_list.__len__(), 3, "Length after the first pop should be 2")
        self.assertEqual(self.linked_list.pop(), 1000, "If we pop by default we should get 1000")
        self.assertEqual(self.linked_list.__len__(), 2, "Length after the second pop should be 1")
        self.assertEqual(self.linked_list.pop(0), 1, "If we pop the first element we should get 1")
        self.assertEqual(self.linked_list.__len__(), 1, "Length after the third pop should be 0")

    def test_remove_last_occurence(self):
        self.linked_list = LinkedList()
        self.linked_list.add(1)
        self.linked_list.add(10)
        self.linked_list.add(101)
        self.linked_list.add(101)
        self.linked_list.add(10)
        self.linked_list.add(100)
        self.assertEqual(self.linked_list.__len__(), 6, "Length should be 6")
        self.assertEqual(1 in self.linked_list, True,
                         "After addition 1 into the list, we have to find it there")
        self.assertEqual(10 in self.linked_list, True,
                         "After addition 10 into the list, we have to find it there")
        self.assertEqual(100 in self.linked_list, True,
                         "After addition 100 into the list, we have to find it there")
        self.linked_list.remove_last_occurence(1)
        self.assertEqual(self.linked_list.__len__(), 5, "After the first removal the length should be 5")
        self.assertEqual(1 in self.linked_list, False, "After removing 1 we should not find it in our list")
        self.assertEqual(self.linked_list.first(), 10, "After removing 1 we should find the last value of 10, but not 1")
        self.linked_list.remove_last_occurence(100)
        self.assertEqual(self.linked_list.__len__(), 4, "After the second removal the length should be 4")


# проверки все на свете

if __name__ == "__main__":
    items = LinkedList()
    items.add(10)
    items.add(11)
    items.add(12)
    items.add(13)
    items.add(20)
    print(items[1])
    print(items[2])
    try:
        print(items[100])
    except IndexError:
        print("No such index in the list")
    print(items.first())
    print(items.last())
    print(len(items))
    unittest.main()
