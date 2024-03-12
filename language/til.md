### type hint

- 파이썬은 동적 타이핑 언어이다. 그러므로 타입을 미리 선언하지 않아도 된다.
- 하지만 타입을 미리 선언하지 않으면 해당 변수의 타입을 고려하지 않은 채로 동적으로 타입을 변경하는 불상사가 일어나므로 타입에 대해서 미리 알려주는 기능이 필요하다.
- 타입 힌트를 작성하면 클라이언트 측에서 해당 타입을 고려하면서 작성하므로 효율적인 의사소통을 할 수 있습니다.

  ```python
  def print_answer(i:int, answer:str) -> None:
    print('___'*i, answer, sep='')

  def recursion(s:str, i:int, m:int) -> None:
    print_answer(i, question)
    if m == i:
      print_answer(i, last_answer)
    else:
      for _ in s:
        print_answer(i, _)
      recursion(s, i+1, m)
  
    return print_answer(i, finish_sentence)
  ```
