
from stocksense.main import StockSenseTest

def test_stocksense(tmp):
    with StockSenseTest() as app:
        res = app.run()
        print(res)
        raise Exception

def test_command1(tmp):
    argv = ['command1']
    with StockSenseTest(argv=argv) as app:
        app.run()
