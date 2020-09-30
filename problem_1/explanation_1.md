I used a dictionary for the cache since hash maps are incredibly fast and run in O(1) time. Each key is unique and can be accessed directly.

I decided to use a queue for the LRU items as the least recently used item would be at the beginning of the queue and I'd be able to dequeue it in O(1) time as well.   