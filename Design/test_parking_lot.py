from Design.parkingLot import ParkingLot
def test_parking_lot():
    lot = ParkingLot([2,2])

    print("Running parking lot tests ..")
    t1 = lot.parking("aaa", 10)
    assert t1.floor_idx == 0
    assert lot.get_floor_count(0) == 1

test_parking_lot()