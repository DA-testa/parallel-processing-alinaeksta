# python3

import heapq

def parallel_processing(n, m, data):
    output = []
    heap = [(0, i) for i in range(n)]
    time = [0] * n

    for i in range(m):
        processing = data[i]
        end, index = heapq.heappop(heap)
        output.append((index, time[index]))
        time[index] = end + processing
        heapq.heappush(heap, (time[index], index))

    return output

def main():
    line1 = list(map(int, input().split()))
    n = line1[0]
    m = line1[1]
    data = list(map(int, input().split()))
    result = parallel_processing(n, m, data)
    
    for index, time in result:
        print(index, time)
      
if __name__ == "__main__":
    main()
