"""Tests for the small utility functions."""
import os
import stat
import sys
from pathlib import Path
import numpy as np
import pytest

# Add the project root to sys.path
sys.path.append(str(Path(__file__).parents[1]))

from simdesign.utils import misc, stats  # noqa


def test_dot():
    """dot computes the scalar product and rejects different lengths."""
    assert misc.dot([1.0, 2.0, 3.0], [4.0, 5.0, 6.0]) == pytest.approx(32.0)
    with pytest.raises(ValueError):
        misc.dot([1.0, 2.0], [1.0])


def test_update_nested_dict():
    """Nested dicts are merged key by key."""
    d = {'a': 1, 'b': {'c': 2, 'd': 3}}
    out = misc.update_nested_dict(d, {'b': {'c': 20}, 'e': 5})
    assert out == {'a': 1, 'b': {'c': 20, 'd': 3}, 'e': 5}


def test_signif():
    """signif rounds to significant digits."""
    np.testing.assert_allclose(misc.signif(np.array([123.456, 0.012345]), 3),
                               [123.0, 0.0123])


def test_round_list_and_numpy_types():
    """round_list rounds numbers, keeps strings and converts numpy types."""
    out = misc.round_list(['Elastic', np.float64(1.123456789), np.int64(3)],
                          precision=4)
    assert out == ['Elastic', 1.1235, 3]
    assert all(type(v) in (str, float, int) for v in out)


def test_check_parameters():
    """Missing required parameters raise an error."""
    misc.check_parameters({'a': 1, 'b': 2}, ('a', 'b'))
    with pytest.raises(Exception):
        misc.check_parameters({'a': 1}, ('a', 'b'))


@pytest.mark.parametrize('value, expected', [
    (True, True), (0, False), ('Yes', True), ('off', False),
    ('TRUE', True), (np.bool_(False), False)])
def test_to_bool(value, expected):
    """Booleans, 0/1 and yes/no style strings are converted."""
    assert misc._to_bool('flag', value) is expected


@pytest.mark.parametrize('value', ['maybe', 2, None])
def test_to_bool_invalid(value):
    """Other values raise an error."""
    with pytest.raises(ValueError):
        misc._to_bool('flag', value)


def test_make_and_remove_dir_with_read_only_file(tmp_path):
    """remove_dir also removes read-only files."""
    folder = tmp_path / 'out' / 'sub'
    misc.make_dir(folder)
    assert folder.is_dir()
    file = folder / 'locked.txt'
    file.write_text('x')
    os.chmod(file, stat.S_IREAD)
    misc.remove_dir(tmp_path / 'out')
    assert not (tmp_path / 'out').exists()


def test_random_truncated_lognormal_within_bounds():
    """Samples of the truncated lognormal distribution stay in bounds."""
    np.random.seed(1)
    x = stats.random_truncated_lognormal(
        1000, np.array([np.log(30.0)]), np.array([0.2]),
        np.array([20.0]), np.array([40.0]))
    x = np.asarray(x)
    assert x.size == 1000
    assert np.all((x >= 20.0) & (x <= 40.0))


def test_truncated_lognormal_inverse_cdf_is_monotonic():
    """The inverse CDF increases with the probability and maps 0 and 1 to
    the bounds."""
    cdf = np.linspace(0.0, 1.0, 11)
    x = np.asarray(stats.truncated_lognormal_cdf_inv(
        cdf, np.log(30.0), 0.2, 20.0, 40.0)).ravel()
    assert np.all(np.diff(x) >= 0)
    assert x[0] == pytest.approx(20.0)
    assert x[-1] == pytest.approx(40.0)


def test_random_choice_and_uniform():
    """Choices come from the options; uniform samples stay in bounds."""
    np.random.seed(2)
    picks = stats.random_choice(['a', 'b', 'c'], 200, [0.5, 0.5, 0.0])
    assert set(np.asarray(picks)) <= {'a', 'b'}
    u = np.asarray(stats.random_uniform(200, 1.0, 2.0))
    assert np.all((u >= 1.0) & (u <= 2.0))


def test_random_multivariate_normal_shape():
    """Correlated normal samples have one column per variable."""
    np.random.seed(3)
    k0 = np.array([[1.0, 0.5], [0.5, 1.0]])
    x = np.asarray(stats.random_multivariate_normal(
        np.array([0.0, 1.0]), k0, 500))
    assert x.shape == (500, 2)
    assert abs(np.mean(x[:, 1]) - 1.0) < 0.2
