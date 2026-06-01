def meetingRooms(intervals: list[list[int]]) -> bool:
    if not intervals:
        return True
    intervals.sort(key=lambda x: x[0])
    first = intervals[0]
    for i in intervals[1:]:
        if first[1] > i[0]:
            return False
    return True

if __name__ == "__main__":
    tests = [
        ([], True),
        ([[0, 30], [5, 10], [15, 20]], False),
        ([[7, 10], [2, 4]], True),
        ([[1, 5], [2, 6], [4, 8], [9, 10]], False),
        ([[0, 5], [5, 10]], True),  # end == start should allow reuse of room
    ]

    for intervals, expected in tests:
        res = meetingRooms([list(i) for i in intervals])
        print(f"{intervals} -> {res} (expected {expected})")
        assert res == expected
    