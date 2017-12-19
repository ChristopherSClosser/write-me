"""Test file for ensure scaffolding functionality."""
import os

from unittest import TestCase

from unittest.mock import patch

import pytest

from .make_scaffold import main, overwrite


class TestScaffold(TestCase):
    """Scaffold class for testing inputs and file creation."""

    def test_overwrite_input_no(self):
        """Test overwrite function if no entered."""
        with patch('builtins.input', side_effect=['n', 'no']):
            assert overwrite() == 'README.md.new'

    def test_overwrite_input_yes(self):
        """Test overwrite function if yes entered."""
        with patch('builtins.input', side_effect=['y', 'yes']):
            assert overwrite() == 'README.md'

    def test_main_returns_succcess_text(self):
        """Test success test returned when main is called."""
        with patch('builtins.input', side_effect='y'):
            assert main() == 'README generated.'


# with open('README.md', 'r') as readme:
#   text_readme = readme.read()


# def test_main_fn_returns_test_response():
#     """Test main() fn, when called, returns testing confirmation."""
#     assert main() == "README generated."


# def test_generated_readme_has_proj_name():
#     """Test Project Name placeholder is in generated README."""
#     assert "# Project Title" in text_readme


# def test_generated_readme_has_testing_instructions():
#     """Testing instructions are in generated README."""
#     assert "This application uses pytest as a testing suite. To run tests, run:" in text_readme


# def test_generated_readme_has_attribution_to_writeme():
#     """Test generated readme includes attribution to our project."""
#     assert "*This README was generated using [writeme.](https://github.com/chelseadole/write-me)*" in text_readme


# def test_readme_does_not_have_serving_info_with_settings():
#     """README does not include serving or urls when has_web_framework is false."""
#     main()
#     assert "Serving Locally" not in text_readme
