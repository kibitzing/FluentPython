==============
Tombola 테스트
==============

Tombola의 모든 구상 서브클래스는 이 테스트를 통과해야 한다.

반복형에서 객체를 생성하고 로딩한다::

    >>> balls = list(range(3))
    >>> globe = ConcreteTombola(balls)
    >>> globe.loaded()
    True
    >>> globe.inspect()
    (0, 1, 2)

공을 꺼내서 수집한다::

    >>> picks = []
    >>> picks.append(globe.pick())
    >>> picks.append(globe.pick())
    >>> picks.append(globe.pick())

상태와 결과를 확인한다::

    >>> globe.loaded()
    False
    >>> sorted(picks) == balls
    True

테스트를 해보았다::

    >>> print("test")
    test
    >>> print("test")
    failure

끝
