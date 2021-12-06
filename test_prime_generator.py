import pytest
import prime_generator as pg

def test_all():
    assert pg.prime_finder_2_0() == pg.prime_finder_2_1()
    assert pg.naive_prime_finder() == pg.prime_finder_2_0()
    assert len(pg.prime_finder_2_1()) == 168

if __name__ == '__main__':
    test_all()
    print(pg.prime_finder_2_1(100))
    print(pg.prime_finder_2_0(100))