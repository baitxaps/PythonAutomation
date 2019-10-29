#! /usr/bin/env python3
# coding: utf-8

from collections import deque
from collections import defaultdict
from collections import OrderedDict
import heapq
import json

def drop_first_last(grades):
    first, *middle, last = grades
    record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
    name, email, *phone_numbers = record

    #*trailing_qtrs, current_qtr = sales_record
    #trailing_avg = sum(trailing_qtrs) / len(trailing_qtrs)
    # return avg_comparison(trailing_avg, current_qtr)

    # return avg(middle)
#drop_first_last(['Dave', 11,11,12,13,14, '847-555-1212'])


def do_foo(x, y): print('foo', x, y)


def do_bar(s): print('bar', s)


def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)


def exec():
    records = [('foo', 1, 2), ('bar', 'hello'), ('foo', 3, 4)]
    for tag, *args in records:
        if tag == 'foo':
            do_foo(*args)
        elif tag == 'bar':
            do_bar(*args)

    line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
    uname, *fields, homedir, sh = line.split(':')
    print(uname, fields, homedir, sh)

    record = ('ACME', 50, 123.45, (12, 18, 2012))
    name, *_, (*_, year) = record
    print(name, year)

    # recursive
    items = [1, 10, 7, 4, 5, 9]
    print(sum(items))

# exec()


def maxDeque():
    # q = deque(maxlen=3)
    # q.append(1)
    # q.append(2)
    # q.append(3)
    # print(q)
    # q.append(4)
    # print(q)
    # q.appendleft(0)
    # print(q)
    # q.popleft()
    # print(q)

    nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
    print(heapq.nlargest(3, nums))
    print(heapq.nsmallest(3, nums))

    portfolio = [
        {'name': 'IBM', 'shares': 100, 'price': 91.1},
        {'name': 'AAPL', 'shares': 50, 'price': 543.22},
        {'name': 'FB', 'shares': 200, 'price': 21.09},
        {'name': 'HPQ', 'shares': 35, 'price': 31.75},
        {'name': 'YHOO', 'shares': 45, 'price': 16.35},
        {'name': 'ACME', 'shares': 75, 'price': 115.65}
    ]
    cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
    expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
    print(cheap)
    print(expensive)

    nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
    heap = list(nums)
    heapq.heapify(heap)
    print(heap)

# 1.5 queue
class PrioritQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        print('正在调用__str__方法，转换为普通字符串')
        return 'Item({!r})'.format(self.name)


def PriorityTest():
    q = PrioritQueue()
    q.push(Item('foo'), 1)
    q.push(Item('bar'), 5)
    q.push(Item('spam'), 4)
    q.push(Item('grok'), 1)
    print(Item('grok'), 1)
    a = (1, 0, Item('foo'))
    b = (5, 1, Item('bar'))
    c = (1, 2, Item('grok'))
    morethan = a < b
    print(morethan)

   # print(repr(q.push(Item('grok'), 1)))
    # print(q)
    # q.pop()
    # print(q)
    # q.pop()
    # print(q)

# 1.6 字典中的键映射多个值
def DefaultdictTest():
    d = defaultdict(list)
    d['a'].append(1)
    d['a'].append(2)
    d['b'].append(4)
    d = defaultdict(set)
    d['a'].add(1)
    d['a'].add(2)
    d['b'].add(4)
    print(d)

    d = {}  # A regular dictionary
    d.setdefault('a', []).append(1)
    d.setdefault('a', []).append(2)
    d.setdefault('b', []).append(4)



# 1.7 字典排序
def OrderedDictTest():
    d = OrderedDict()
    d['grok'] = 4
    d['foo'] = 1
    d['bar'] = 2
    d['spam'] = 3
    # Outputs "foo 1", "bar 2", "spam 3", "grok 4"
    # for key in d:
    #     print(key, d[key])
    # js = json.dumps(d)
    # print(js)

    prices = {'ACME': 45.23,'AAPL': 612.78,'IBM': 205.55,'HPQ': 37.20,'FB': 10.75}
    min_price = min(zip(prices.values(), prices.keys()))
    max_price = max(zip(prices.values(), prices.keys()))
    prices_sorted = sorted(zip(prices.values(), prices.keys()))
    print(min_price,max_price,prices_sorted)

    #print(min(prices)) #key
    #print(min(prices.values())) #value
    print(min(prices, key=lambda k: prices[k])) # Returns 'FB')
    min_value = prices[min(prices, key=lambda k: prices[k])]
    print(min_value)


# 1.9 查找两字典的相同点
def keydictValue():
    a={'x' : 1,'y' : 2,'z' : 3 }
    b={'w' : 10,'x' : 11,'y' : 2 }

    c =  a.keys() & b.keys() # { 'x', 'y' }
    print(c)
    sub = a.keys() - b.keys() # { 'z' }
    print(sub)
    item = a.items() & b.items() # { ('y', 2) }
    print(item)
    # Make a new dictionary with certain keys removed
    c = {key:a[key] for key in a.keys() - {'z', 'w'}} # c is {'x': 1, 'y': 2}
    print(c)




# 1.10 删除序列相同元素并保持顺序
#def deleElem():
def dedupe(items): 
    seen = set()
    for item in items:
        if item not in seen:
            yield item 
            seen.add(item)

def _dedupe_(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item) 
        if val not in seen:
            yield item 
            seen.add(val)            

def dedupeTest():
    a = [1, 5, 2, 1, 9, 1, 5, 10]
    print(list(dedupe(a)))
    a = set(a)
    print(a)

    a = [{'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]
    ts = list(_dedupe_(a, key=lambda d: (d['x'],d['y'])))
    print(ts)
    ts =list(_dedupe_(a, key=lambda d: d['x']))
    print(ts)


# 1.11 命名切片
def Slice():
    record = '....................100 .......513.25 ..........'
    cost = int(record[20:23]) * float(record[31:37])

    SHARES = slice(20, 23)
    PRICE = slice(31, 37)
    cost = int(record[SHARES]) * float(record[PRICE])


if __name__ == '__main__':
    # 注释 cmd +K+C˝
    # 取消注释 cmd+K+U
    # Shift+cmd+F 实现代码的对齐
    # Ctrl+[ 和 Ctrl+] 实现文本的向左移动或者向右移动

    Slice()
    # dedupeTest()
    # keydictValue()
    # OrderedDictTest()
    # PriorityTest()
    # maxDeque()

    # with open(r'/Users/jishuyanfa-ios/Desktop/vcode/cookbook/somefile.txt') as f:
    #     for line, prevlines in search(f, 'python', 5):
    #         for pline in prevlines:
    #             print(pline, end='')
    #             print('-' * 20)
