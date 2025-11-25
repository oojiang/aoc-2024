from state import read_input_2

branches = read_input_2('input')

NUM_GATES = 45

zresults = [-1 for _ in range(NUM_GATES)]
carry = [-1 for _ in range(NUM_GATES)]
xor_x_y = [-1 for _ in range(NUM_GATES)]
and_x_y = [-1 for _ in range(NUM_GATES)]
and_carry = [-1 for _ in range(NUM_GATES)]

errors = set()

XOR = 'XOR'
AND = 'AND'
OR = 'OR'
ANY = '?'

COMMAND, OP1, OP2, RESULT = 0, 1, 2, 3

def catalog(n):
    if n not in range(NUM_GATES):
        return
    if n == 0:
        z = find(XOR, x(0), y(0), ANY)
        zresults[n] = z[RESULT]

        c = find(AND, x(0), y(0), ANY)
        carry[n + 1] = c[RESULT]
    else:
        ia = find(XOR, x(n), y(n), ANY)
        xor_x_y[n] = ia[RESULT]

        ib = find(AND, x(n), y(n), ANY)
        and_x_y[n] = ib[RESULT]

        z = find(XOR, xor_x_y[n], carry[n], ANY)
        zresults[n] = z[RESULT]

        if n + 1 in range(NUM_GATES):
            ic = find(AND, xor_x_y[n], carry[n], ANY)
            and_carry[n] = ic[RESULT]

            c = find(OR, and_x_y[n], and_carry[n], ANY)
            carry[n + 1] = c[RESULT]


def matches(branch, command, op1, op2, result):
    command_, op1_, op2_, result_ = branch
    if command != ANY and command != command_:
        return False
    if op1 != ANY and op1 not in (op1_, op2_):
        return False
    if op2 != ANY and op2 not in (op1_, op2_):
        return False
    if result != ANY and result != result_:
        return False
    return True

def find(command, op1, op2, result):
    results = list(filter(
        lambda branch: matches(branch, command, op1, op2, result),
        branches))
    if len(results) == 1:
        return results[0]
    print(command, op1, op2, result, 'FAILED. RETRYING')

    results = list(filter(
        lambda branch: matches(branch, command, op1, op2, ANY),
        branches))
    if len(results) == 1:
        errors.add(results[0][RESULT])
        errors.add(result)
        return results[0]
    print(command, op1, op2, ANY, 'FAILED. RETRYING')

    results = list(filter(
        lambda branch: matches(branch, command, op1, ANY, result),
        branches))
    if len(results) == 1:
        op2_ = set([results[0][OP1], results[0][OP2]]).difference(set([op1])).pop()
        errors.add(op2_)
        errors.add(op2)
        return results[0]
    print(command, op1, ANY, result, 'FAILED. RETRYING')

    results = list(filter(
        lambda branch: matches(branch, command, ANY, op2, result),
        branches))
    if len(results) == 1:
        op1_ = set([results[0][OP1], results[0][OP2]]).difference(set([op2])).pop()
        errors.add(op1_)
        errors.add(op1)
        return results[0]
    print(command, ANY, op2, result, 'FAILED.')
    assert(False)


def x(n):
    return 'x' + str(n).zfill(2)

def y(n):
    return 'y' + str(n).zfill(2)

def z(n):
    return 'z' + str(n).zfill(2)


for n in range(NUM_GATES):
    print('cataloging', n)
    catalog(n)
print(','.join(sorted(errors)))
