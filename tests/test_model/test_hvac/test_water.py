from PHX.model.enums import hvac
from PHX.model.hvac import water


def test_add_default_PhxHotWaterTankParams(reset_class_counters):
    p1 = water.PhxHotWaterTankParams()
    p2 = water.PhxHotWaterTankParams()

    p3 = p1 + p2

    assert p3 == p2 == p1
    assert p3.solar_losses == p1.solar_losses
    assert p3.storage_loss_rate == p1.storage_loss_rate
    assert p3.standby_losses == p1.standby_losses
    assert p3.input_option == p1.input_option
    assert p3.storage_capacity == p1.storage_capacity
    assert p3.room_temp == p1.room_temp
    assert p3.water_temp == p1.water_temp


def test_add_mixed_PhxHotWaterTankParams(reset_class_counters):
    p1 = water.PhxHotWaterTankParams(
        solar_losses=4,
        storage_loss_rate=2,
        standby_losses=10,
        input_option=hvac.PhxHotWaterInputOptions.SPEC_TOTAL_LOSSES,
        storage_capacity=10,
        room_temp=1,
        water_temp=4,
    )
    p2 = water.PhxHotWaterTankParams(
        solar_losses=4,
        storage_loss_rate=4,
        standby_losses=20,
        input_option=hvac.PhxHotWaterInputOptions.SPEC_TOTAL_LOSSES,
        storage_capacity=20,
        room_temp=2,
        water_temp=8,
    )

    p3 = p1 + p2

    assert p3 != p2 != p1
    assert p3.solar_losses == 4
    assert p3.storage_loss_rate == 3
    assert p3.standby_losses == 15
    assert p3.input_option == p1.input_option
    assert p3.storage_capacity == 15
    assert p3.room_temp == 1.5
    assert p3.water_temp == 6


def test_default_PhxHotWaterTank(reset_class_counters):
    p1 = water.PhxHotWaterTank()
    p2 = water.PhxHotWaterTank()

    assert p1.id_num == 1
    assert p2.id_num == 2


def test_PhxHotWaterTank_quantity(reset_class_counters):
    d1 = water.PhxHotWaterTank()
    d1.quantity = 1
    d2 = water.PhxHotWaterTank()
    d2.quantity = 12

    assert d1 != d2
    assert d1.quantity != d2.quantity


def test_add_default_PhxHotWaterTank(reset_class_counters):
    p1 = water.PhxHotWaterTank()
    p2 = water.PhxHotWaterTank()

    p3 = p1 + p2

    assert p1 != p2 != p3


def test_add_mixed_PhxHotWaterTank(reset_class_counters):
    d1 = water.PhxHotWaterTank()
    d1.quantity = 10
    d1.params = water.PhxHotWaterTankParams(
        solar_losses=4,
        storage_loss_rate=2,
        standby_losses=10,
        input_option=hvac.PhxHotWaterInputOptions.SPEC_TOTAL_LOSSES,
        storage_capacity=10,
        room_temp=1,
        water_temp=4,
    )
    d2 = water.PhxHotWaterTank()
    d2.quantity = 11
    d2.params = water.PhxHotWaterTankParams(
        solar_losses=4,
        storage_loss_rate=4,
        standby_losses=20,
        input_option=hvac.PhxHotWaterInputOptions.SPEC_TOTAL_LOSSES,
        storage_capacity=20,
        room_temp=2,
        water_temp=8,
    )

    d3 = d1 + d2

    assert d3 != d2 != d1
    assert d3.quantity == 21
    assert d3.params.solar_losses == 4
    assert d3.params.storage_loss_rate == 3
    assert d3.params.standby_losses == 15
    assert d3.params.input_option == d1.params.input_option
    assert d3.params.storage_capacity == 15
    assert d3.params.room_temp == 1.5
    assert d3.params.water_temp == 6
