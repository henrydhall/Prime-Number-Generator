import pytest
import prime_generator as pg

def test_all():
    assert pg.naive_prime_finder() == pg.prime_finder_2_0()
    assert pg.prime_finder_2_0() == pg.prime_finder_2_1()
    assert pg.prime_finder_2_1() == pg.prime_finder_2_2()
    assert len(pg.prime_finder_2_1()) == 168
    assert len(pg.prime_finder_2_2(1000000)) == 78498

if __name__ == '__main__':
    print(pg.naive_prime_finder(100))
    print(pg.prime_finder_2_0(100))
    test_all()