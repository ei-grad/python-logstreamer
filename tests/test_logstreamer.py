from logstreamer import Logstreamer


def make_log(path, rows):
    with open(path, 'w') as f:
        for i in rows:
            f.write(i)
            f.write('\n')


def test_callable_target():
    rows = []
    make_log('single_row.log', ["row"])
    logstreamer = Logstreamer('single_row.log', rows.append)
    logstreamer.run()
    assert rows == ['row']
