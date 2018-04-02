Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.

put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

Follow up:

Could you do both operations in O(1) time complexity?

Example:

    LRUCache cache = new LRUCache( 2 /* capacity */ );
    
    cache.put(1, 1);
    cache.put(2, 2);
    cache.get(1);       // returns 1
    cache.put(3, 3);    // evicts key 2
    cache.get(2);       // returns -1 (not found)
    cache.put(4, 4);    // evicts key 1
    cache.get(1);       // returns -1 (not found)
    cache.get(3);       // returns 3
    cache.get(4);       // returns 4

思路就是设置一个双向链表和一个cache，cache的key对应的就是一个node类的实例

双向链表有一个头（head）和一个尾（tail），这两个头和尾没有意义，他们纯粹是起到一个flag的作用
