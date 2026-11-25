# 강의실 예약 시스템 (Room Booking)

바이브코딩 실기 과제 — 강의실 예약·취소·시간표 규칙을 구현한 Python 클래스와 웹 화면입니다.

- **사이트**: https://liuzhiyuan011215-cmyk.github.io/room-booking/
- **과제 문제지**: [PROBLEM.md](PROBLEM.md)
- **구분**: 수업 과제 (개인) · LIU ZHIYUAN

## 기능
| 기능 | 규칙 |
|---|---|
| 예약 `book(room, day, start, end, name)` | 강의실 3곳 × 월~금, 9~21시, 한 번에 3시간 이하, 시간 겹침 불가(끝나는 시각에 바로 시작은 가능), 1인 하루 최대 2건 |
| 취소 `cancel(room, day, start, name)` | 예약한 본인만 취소 가능 |
| 시간표 `get_schedule(room, day)` | 시작 시각 순 정렬 |

## 파일 구성
- `solution.py`: `RoomBooking` 클래스 (채점 대상)
- `check.py`: 샘플 테스트 5개
- `index.html`, `assets/`: 웹 화면 (시간표 보드, 모바일 대응, GitHub Pages 배포)

## 실행
```bash
python check.py        # 샘플 테스트 5개 실행
```
웹은 위 사이트 주소에서 바로 쓰거나 `index.html`을 브라우저로 엽니다.

## 본인 역할
- 문제지 규칙을 AI(Claude)에게 주고 구현하게 한 뒤, `check.py`와 확인표로 결과를 직접 검증
- 웹 디자인 개선(일러스트, 시간표 보드), 모바일 화면 수정(시간 표시, 헤더 여백, 취소 양식)
