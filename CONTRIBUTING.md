<!-- omit in toc -->
# Contributing Guidance

Thank you for considering contributing to `wiktionary-ja`! 😘

We are happy to have you here. This document consists of some guidelines and instructions for contributing to `wiktionary-ja`.

All types of contributions are encouraged and valued. See the [Table of Contents](#table-of-contents) for different ways to help and details about how this project handles them.

Even if you don't have time, you can still support the project in other ways, such as starring the project, tweeting about it, or telling your friends about it. Every little bit helps!

<!-- omit in toc -->
## Table of Contents

- [Reporting Bugs](#reporting-bugs)
- [Suggesting Enhancements](#suggesting-enhancements)
- [Development](#development)
  - [Making Changes](#making-changes)
- [Coverage](#coverage)
  - [Test Coverage](#test-coverage)
  - [Docstring Coverage](#docstring-coverage)

## Reporting Bugs

We use GitHub issues to track bugs and errors. If you run into an issue with the project, please [open an issue](https://github.com/mkpoli/wiktionary-ja/issues) and provide as much information as possible. This will help us to understand the problem and fix it.

## Suggesting Enhancements

If you have an idea for a new feature or an enhancement to an existing feature, please [open an issue](https://github.com/mkpoli/wiktionary-ja/issues) and describe the feature you would like to see. We will discuss the idea and decide if it is a good fit for the project.

## Development

General steps to contribute to the project:

1. Fork the repository and clone it locally.
2. [Install uv](https://docs.astral.sh/uv/getting-started/installation/) and install the project. (`curl -LsSf https://astral.sh/uv/install.sh | sh` and `uv sync --all-extras --dev`)
3. Make your changes and run `uv run ruff check --fix` and `uv run pytest` to lint, format the code and run the tests.
4. Submit a pull request to the main repository.

### Making Changes

Commit messages need to follow the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) specification. A good commit should be focused and logical changes that address one specific issue. Write commit messages that are clear and concise, detailed information can be added to the commit message body.

## Coverage

### Test Coverage

To check the coverage of the project, run `uv run pytest --cov --cov-report xml`.

### Docstring Coverage
To check the coverage of the project, run `uv run docstr-coverage check`.
