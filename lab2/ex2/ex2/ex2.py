state = 'q0'
end_state = 'q3'
text = 'zambeste ca cat'
tranzitii = {
    ("q0", "c"): "q1",
    ("q1", "a"): "q2",
    ("q1", "c"): "q1",
    ("q2", "t"): "q3",
    ("q2", "c"): "q1"
}

for char in text:
    if (state, char) in tranzitii:
        state = tranzitii[(state, char)]
    else:
        state = "q0"
    if state == end_state:
        print("Am gasit 'cat'!")
    