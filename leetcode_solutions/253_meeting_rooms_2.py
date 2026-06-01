import heapq

def minMeetingRooms(intervals):
    """
    Given a list of meeting time intervals represented as [start, end],
    return the minimum number of conference rooms required to hold all meetings.

    Approach:
    - Sort intervals by start time.
    - Use a min-heap to keep track of end times of meetings currently using rooms.
      The heap's smallest value is the meeting that frees up earliest.
    - For each meeting in order, if the earliest-ending meeting has ended
      (heap[0] <= current start), reuse that room (pop heap). Push the current
      meeting's end time onto the heap. The heap size at any time is the number
      of rooms in use; the maximum (or final heap size after processing all
      intervals) is the minimum rooms required.

    Complexity:
    - Time: O(n log n) due to sorting and heap operations.
    - Space: O(n) for the heap in the worst case.
    """
    if not intervals:
        return 0

    # Sort meetings by start time
    intervals.sort(key=lambda x: x[0])
    
    # Min-heap to store the end times of ongoing meetings
    min_heap = []
    
    for meeting in intervals:
        # If the room of the earliest finishing meeting is free
        if min_heap and min_heap[0] <= meeting[0]:
            heapq.heappop(min_heap)
            
        # Allocate a new room (push the current meeting's end time)
        heapq.heappush(min_heap, meeting[1])
        
    # The size of the heap is the minimum number of rooms required
    return len(min_heap)

# Basic test cases demonstrating typical and edge scenarios
if __name__ == "__main__":
    tests = [
        ([], 0),
        ([[0, 30], [5, 10], [15, 20]], 2),
        ([[7, 10], [2, 4]], 1),
        ([[1, 5], [2, 6], [4, 8], [9, 10]], 3),
        ([[0, 5], [5, 10]], 1),  # end == start should allow reuse of room
    ]

    for intervals, expected in tests:
        res = minMeetingRooms([list(i) for i in intervals])
        print(f"{intervals} -> {res} (expected {expected})")
        assert res == expected
    print("All tests passed.")
