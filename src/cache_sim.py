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
        pass # To be implemented

    def run_optff(self):
        pass # Partner 2 will implement this

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
    print(f"Loaded cache with capacity {k} and {m} requests.")

if __name__ == "__main__":
    main()