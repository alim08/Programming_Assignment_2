import sys
from collections import deque, OrderedDict, defaultdict

class CacheSimulator:
    def __init__(self, capacity, sequence):
        self.k = capacity
        self.seq = sequence

    def run_fifo(self):
        cache_set = set()
        queue = deque()
        misses = 0

        for req in self.req:
            if req not in cache_set:
                misses += 1
                if len(cache_set) == self.k:
                    evicted = queue.popleft()
                    cache_set.remove(evicted)
                cache_set.add(req)
                queue.append(req)
        
        return misses

    def run_lru(self):
        cache = OrderedDict()
        misses = 0

        for req in self.seq:
            if req in cache:
                cache.move_to_end(req)
            else:
                misses += 1
                if len(cache) == self.k:
                    cache.popitem(last=False)
                cache[req] = True
        
        return misses

    def run_optff(self):
        cache_set = set()
        misses = 0
        
        future_occurrences = defaultdict(deque)
        for i, req in enumerate(self.seq):
            future_occurrences[req].append(i)

        for i, req in enumerate(self.seq):
            future_occurrences[req].popleft()
            
            if req not in cache_set:
                misses += 1
                if len(cache_set) == self.k:
                    farthest_req = None
                    farthest_idx = -1
                    
                    for item in cache_set:
                        if not future_occurrences[item]:
                            farthest_req = item
                            break
                        
                        next_idx = future_occurrences[item][0]
                        if next_idx > farthest_idx:
                            farthest_idx = next_idx
                            farthest_req = item
                            
                    cache_set.remove(farthest_req)
                cache_set.add(req)
                
        return misses

def main():
    if len(sys.argv) < 2:
        print("Usage: python src/cache_sim.py <input_file>")
        sys.exit(1)

    filename = sys.argv[1]
    
    with open(filename, 'r') as f:
        data = f.read().split()
        
    if not data:
        return
        
    k = int(data[0])
    m = int(data[1])
    sequence = [int(x) for x in data[2:2+m]]
    
    sim = CacheSimulator(k, sequence)
    print(f"FIFO  : {sim.run_fifo()}")
    print(f"LRU   : {sim.run_lru()}")
    print(f"OPTFF : {sim.run_optff()}")

if __name__ == "__main__":
    main()