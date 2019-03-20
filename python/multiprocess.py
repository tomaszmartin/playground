import multiprocessing


def test(sample, to_add):
    sample.append(to_add)
    print(f'Process {id(sample)}: {sample}')


# Normally processes doesn't exchange data
x = [1, 2, 3]
proc1 = multiprocessing.Process(target=test, args=(x, 1))
proc2 = multiprocessing.Process(target=test, args=(x, 2))
proc1.start()
proc2.start()
proc1.join()
proc2.join()
# Although each of them have the same ID of the object
# But each in its own memroy space
print(f'Original {id(x)}: {x}')


# Pool are a liitle bit more compact
with multiprocessing.Pool(2) as p:
    p.starmap(test, [(x, 1), (x, 2)])
