from Design.MinStack import MinStack
def test_min_stack():
    sol = MinStack()
    sol.push(-2)
    sol.push(0)
    sol.push(-2)
    sol.pop()

    assert sol.top() == 0
    assert sol.getMin() == -2

test_min_stack()

