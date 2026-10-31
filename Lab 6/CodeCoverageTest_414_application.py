
import pytest

from laundry_service import extra_weight_charge, order_acceptable, dropoff_status


def test_within_included_weight():
    assert extra_weight_charge("regular", 4, "standard", False) == 0


def test_member_included_weight():
    assert extra_weight_charge("regular", 6, "standard", True) == 0


def test_delicate_extra_weight():
    assert extra_weight_charge("delicate", 5, "standard", False) == 60


def test_bedding_extra_weight():
    assert extra_weight_charge("bedding", 10, "standard", False) == 60


def test_standard_speed():
    assert extra_weight_charge("regular", 7, "standard", False) == 60


def test_express_speed():
    assert extra_weight_charge("regular", 7, "express", False) == 100


def test_large_standard_weight():
    assert extra_weight_charge("regular", 16, "standard", False) == 495


def test_large_express_weight():
    assert extra_weight_charge("regular", 16, "express", False) == 825


def test_unknown_garment():
    with pytest.raises(ValueError, match="unknown garment type"):
        extra_weight_charge("unknown", 5, "standard", False)


def test_negative_weight():
    with pytest.raises(ValueError, match="invalid weight"):
        extra_weight_charge("regular", -1, "standard", False)


def test_order_acceptable():
    assert order_acceptable(10, 20, False) is True


def test_delicate_order_acceptable():
    assert order_acceptable(10, 5, True) is True


def test_heavy_order_rejected():
    assert order_acceptable(26, 20, False) is False


def test_too_many_items():
    assert order_acceptable(10, 41, False) is False


def test_dropoff_accepted():
    assert dropoff_status(90, False, False) == "accepted"


def test_dropoff_late():
    assert dropoff_status(50, False, False) == "late"


def test_dropoff_rejected():
    assert dropoff_status(30, False, False) == "rejected"
