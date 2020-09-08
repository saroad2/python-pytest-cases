# Authors: Sylvain MARIE <sylvain.marie@se.com>
#          + All contributors to <https://github.com/smarie/python-pytest-cases>
#
# License: 3-clause BSD, <https://github.com/smarie/python-pytest-cases/blob/master/LICENSE>
from .common_pytest_lazy_values import lazy_value
from .common_others import unfold_expected_err, assert_exception, AUTO, AUTO2

from .fixture_core1_unions import fixture_union, NOT_USED, unpack_fixture, ignore_unused
from .fixture_core2 import pytest_fixture_plus, fixture_plus, param_fixtures, param_fixture
from .fixture_parametrize_plus import pytest_parametrize_plus, parametrize_plus, fixture_ref

# additional symbols without the 'plus' suffix
parametrize = parametrize_plus
fixture = fixture_plus

from .case_funcs_legacy import case_name, test_target, case_tags, cases_generator
from .case_parametrizer_legacy import cases_data, CaseDataGetter, get_all_cases_legacy, \
    get_pytest_parametrize_args_legacy, cases_fixture

from .case_funcs_new import case, CaseInfo
from .case_parametrizer_new import parametrize_with_cases, THIS_MODULE, get_all_cases, get_parametrize_args

try:
    # -- Distribution mode --
    # import from _version.py generated by setuptools_scm during release
    from ._version import version as __version__
except ImportError:
    # -- Source mode --
    # use setuptools_scm to get the current version from src using git
    from setuptools_scm import get_version as _gv
    from os import path as _path
    __version__ = _gv(_path.join(_path.dirname(__file__), _path.pardir))

__all__ = [
    '__version__',
    # the submodules
    'common_pytest_lazy_values', 'common_pytest', 'common_others', 'common_mini_six',
    'case_funcs_legacy', 'case_funcs_new',  'case_parametrizer_legacy', 'case_parametrizer_new',
    'fixture_core1_unions', 'fixture_core2', 'fixture_parametrize_plus',

    # all symbols imported above
    'unfold_expected_err', 'assert_exception',

    # --fixture core1
    'fixture_union', 'NOT_USED', 'unpack_fixture', 'ignore_unused',
    # -- fixture core2
    'pytest_fixture_plus', 'fixture_plus', 'fixture', 'param_fixtures', 'param_fixture',
    # -- fixture parametrize plus
    'pytest_parametrize_plus', 'parametrize_plus', 'parametrize', 'fixture_ref', 'lazy_value',

    # V1 - DEPRECATED symbols
    # --cases_funcs
    'case_name',  'test_target', 'case_tags', 'cases_generator',
    # --main params
    'cases_data', 'CaseDataGetter', 'get_all_cases_legacy',
    'get_pytest_parametrize_args_legacy', 'cases_fixture',

    # V2 symbols
    'AUTO', 'AUTO2',
    # case functions
    'case', 'CaseInfo', 'get_all_cases',
    # test functions
    'parametrize_with_cases', 'THIS_MODULE', 'get_parametrize_args'
]

try:  # python 3.5+ type hints
    from pytest_cases.case_funcs_legacy import CaseData, Given, ExpectedNormal, ExpectedError, MultipleStepsCaseData
    __all__ += ['CaseData', 'Given', 'ExpectedNormal', 'ExpectedError', 'MultipleStepsCaseData']
except ImportError:
    pass
