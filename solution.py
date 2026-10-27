# 강의실 예약 시스템 — 아래 클래스를 완성하세요. (클래스·메서드 이름은 바꾸지 마세요)

ROOMS = ("A101", "A102", "B201")
DAYS = ("월", "화", "수", "목", "금")


def _is_int(x):
    # bool은 int의 하위 클래스라서 따로 제외
    return type(x) is int


class RoomBooking:
    def __init__(self):
        self.bookings = []  # (room, day, start, end, name)

    def book(self, room, day, start, end, name):
        if room not in ROOMS or day not in DAYS:
            return False
        if not _is_int(start) or not _is_int(end):
            return False
        if start < 9 or end > 21 or start >= end or end - start > 3:
            return False
        for r, d, s, e, n in self.bookings:
            if r == room and d == day and start < e and s < end:
                return False
        if sum(1 for b in self.bookings if b[1] == day and b[4] == name) >= 2:
            return False
        self.bookings.append((room, day, start, end, name))
        return True

    def cancel(self, room, day, start, name):
        for b in self.bookings:
            if b[0] == room and b[1] == day and _is_int(start) and b[2] == start:
                if b[4] != name:
                    return False
                self.bookings.remove(b)
                return True
        return False

    def get_schedule(self, room, day):
        return sorted((s, e, n) for r, d, s, e, n in self.bookings if r == room and d == day)
