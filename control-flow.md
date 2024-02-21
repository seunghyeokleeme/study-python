# control flow tools

## if Statements

- elif: short for 'else if'

## for Statements


## The range() Function

- (시작, 끝, 단계) 
- To iterate over the indices of sequence => range() + len()
- recommend
  - USE enumerate() function
- 반복할 때 원하는 시퀀스의 연속된 항목을 반환하는 객체이지만 실제로 목록을 만들지 않으므로 공간을 절약할 수 있습니다.

## break and continue Statements, and else Clauses on Loop

- while 과 for 루프에는 else clause가 포함 된다.
- 이때 else는 for 에서는 최종 반복 후에 실행된다.
- 그리고 while 루프는 루프 조건이 거짓이 된 후에 실행된다.
- 두 루프에서 break를 만나면 else clause 실행 되지 않는다.

## pass Statements
> usage : 1. no action 2. keep thinking at a more abstract level
- commonly used for creating minimal classes

## match Statements

- rust랑 비슷한것 같다. pattern-matching
- "가드"라고 하는 패턴에 if 절을 추가할 수 있다.
- 가드가 거짓이면 일치 항목은 다음 케이스 블록을 시도
- 가드가 평가되기 전에 **값 캡처가 수행된다는 점 중요하다**

## Default Argument Values

- 기본값은 정의 범위의 함수 정의 시점에서 평가
- 기본값은 한 번만 평가, 변경 가능한 객체일 경우에는 차이!

## Keyword Arguments

- 위치 인수 뒤에 키워드 인수가 있어야 합니다