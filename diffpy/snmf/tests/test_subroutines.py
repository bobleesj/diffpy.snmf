import pytest
import numpy as np
from diffpy.snmf.subroutines import objective_function, get_stretched_component, reconstruct_data, get_residual_matrix

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
    ([.88, [-11.47, -10.688, -8.095, -29.44, 14.38], 5], [-11.47, -10.3344, -13.9164, -11.5136, 0]),
    (
        [.88, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10],
        [1, 2.1364, 3.2727, 4.4091, 5.5455, 6.6818, 7.8182, 8.9545, 0, 0]),
    ([.55,
      [-2.9384, -1.4623, -2.0913, 4.6304, -1.2127, 1.4737, -0.3791, 1.7506, -1.5068, -2.7625, .9617, -.3494, -.3862,
       2.7960], 14], [-2.9384, -1.9769, 0.9121, .6314, .8622, -2.4239, -.2302, 1.9281, 0, 0, 0, 0, 0, 0]),
    ([.987, [0, .25, .5, .75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5], 11],
     [0, .2533, .5066, .7599, 1.0132, 1.2665, 1.5198, 1.7730, 2.0263, 2.2796, 0]),
    ([-0.4, [-1, -2, -3, -4, -5, -6, -7, -8, -9], 9], [-1, 0, 0, 0, 0, 0, 0, 0, 0])

]


@pytest.mark.parametrize("tgso", tgso)
def test_get_stretched_component(tgso):
    actual = get_stretched_component(tgso[0][0], tgso[0][1], tgso[0][2])
    expected = tgso[1]
    np.testing.assert_allclose(actual, expected, rtol=1e-03)


# tuwm = [()
#
# ]
#
#
# @pytest.mark.parametrize(tuwm,'tuwm')
# def test_update_weights_matrix(tuwm):
#     assert False


tgrm = [
    ([[[1, 2], [3, 4]], [[.25], [.75]], [[.9], [.7]], [[11, 22], [33, 44]], 1, 2, 2], [[-9.25, -22], [-30.6190, -44]]),
    ([[[1, 2], [3, 4]], [[1], [1]], [[1], [1]], [[11, 22], [33, 44]], 1, 2, 2], [[-8, -22], [-26, -44]])
    # positive whole numbers
    # negative whole numbers
    # single component
    # positive float
    # negative floats

]


@pytest.mark.parametrize('tgrm', tgrm)
def test_get_residual_matrix(tgrm):
    actual = get_residual_matrix(tgrm[0][0], tgrm[0][1], tgrm[0][2], tgrm[0][3], tgrm[0][4], tgrm[0][5], tgrm[0][6])
    expected = tgrm[1]
    np.testing.assert_allclose(actual, expected)


trd = [
    ([np.array([[.5], [.5]]), np.array([[1, 2], [3, 4]]), np.array([[.25], [.75]]), 2, 1, 2],
     np.array([[.25, 1.5], [0, 0]])),
    ([[[.9], [.7]], [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]], [[.25], [.75]], 2, 1, 5],
     [[.25, 1.5], [.8056, 3.6429], [1.3611, 5.7857], [1.9167, 5.3571], [1.25, 0]]),
    ([[[.5, .7], [.5, .8]], [[1.1, 2.2], [3.3, 4.4]], [[.25, .5], [.75, .5]], 2, 2, 2], [[.275, .55, 1.65, 1.1], [0, .9429, 0, 1.65]])

]


@pytest.mark.parametrize('trd', trd)
def test_reconstruct_data(trd):
    actual = reconstruct_data(trd[0][0], trd[0][1], trd[0][2], trd[0][3], trd[0][4], trd[0][5])
    expected = trd[1]
    np.testing.assert_allclose(actual, expected)
