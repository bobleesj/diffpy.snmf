import pytest
import numpy as np
from diffpy.snmf.subroutines import objective_function, get_stretched_component

to = [
    ([[[1, 2], [3, 4]], [[5, 6], [7, 8]], 1e11, [[1, 2], [3, 4]], [[1, 2], [3, 4]], 1], 2.574e14),
    ([[[11, 2], [31, 4]], [[5, 63], [7, 18]], .001, [[21, 2], [3, 4]], [[11, 22], [3, 40]], 1], 650.4576),
    ([[[1, 2], [3, 4]], [[5, 6], [7, 8]], 1e11, [[1, 2], [3, 4]], [[1, 2], [3, 4]], 0], 2.574e14),

]


@pytest.mark.parametrize("to", to)
def test_objective_function(to):
    actual = objective_function(to[0][0], to[0][1], to[0][2], to[0][3], to[0][4], to[0][5])
    expected = to[1]
    assert actual == pytest.approx(expected)


tgso = [
    ([.25, [6.55, .357, 8.49, 9.33, 6.78, 7.57, 7.43, 3.92, 6.55, 1.71], 10], [6.55, 6.78, 6.55, 0, 0, 0, 0, 0, 0, 0]),
    ([1.25, [-11.47, -10.688, -8.095, -29.44, 14.38], 5], [-11.47, -10.8444, -9.1322, -16.633, -20.6760]),
    ([.88, [-11.47, -10.688, -8.095, -29.44, 14.38], 5], [-11.47, -10.3344, -13.9164, -11.5136, 6.5364]),
    ([.88, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10], [1, 2.1364, 3.2727, 4.4091, 5.5455, 6.6818, 7.8182, 8.9545, 9.0909, 0])

]


@pytest.mark.parametrize("tgso", tgso)
def test_get_stretched_component(tgso):
    actual = get_stretched_component(tgso[0][0], tgso[0][1], tgso[0][2])
    expected = tgso[1]
    np.testing.assert_allclose(actual, expected)
