
import pytest
from hypothesis import given, strategies as st

from laundry_service import parse_order, weight_average, payable_charge


# Test 1: Fuzz testing parse_order()
@given(st.one_of(st.text(), st.none()))
def test_parse_order_no_crash(s):
    try:
        parse_order(s)
    except ValueError:
        pass


# Test 2: Fuzz testing weight_average()
@given(st.one_of(st.text(), st.none()))
def test_weight_average_no_crash(s):
    try:
        weight_average(s)
    except ValueError:
        pass


# Test 3: Fuzz testing payable_charge()
@given(st.one_of(st.text(), st.none()))
def test_payable_charge_no_crash(s):
    try:
        payable_charge(s)
    except ValueError:
        pass


# Valid input tests
def test_parse_order_valid():
    assert parse_order("regular:6") == ("Regular", 6.0)


def test_weight_average_valid():
    assert weight_average("3,5,8") == 5


def test_payable_charge_valid():
    assert payable_charge("300|40") == 314.0


# Invalid input tests
def test_parse_order_invalid():
    with pytest.raises(ValueError):
        parse_order("regular:abc")


def test_weight_average_invalid():
    with pytest.raises(ValueError):
        weight_average("3,,8")


def test_payable_charge_invalid():
    with pytest.raises(ValueError):
        payable_charge("300|abc")
