"""Tests for scaffold of README generator."""

import pytest
from readme_generator.make_scaffold import main
import os
import sys


readme = open("README.md", 'r')
text_readme = readme.read()


def test_main_fn_returns_test_response():
    """Test main() fn, when called, returns testing confirmation."""
    assert main() == "README generated."


def test_generated_readme_has_proj_name():
    """Test Project Name placeholder is in generated README."""
    assert "# Project Title" in text_readme


def test_generated_readme_has_testing_instructions():
    """Testing instructions are in generated README."""
    assert "This application uses pytest as a testing suite. To run tests, run:" in text_readme


def test_generated_readme_has_attribution_to_writeme():
    """Test generated readme includes attribution to our project."""
    assert "*This README was generated using [writeme.](https://github.com/chelseadole/write-me)*" in text_readme


def test_readme_has_serving_info_with_settings():
    """README does not include serving or urls when has_web_framework is false."""
    main()
    assert "Serving Locally" in text_readme
