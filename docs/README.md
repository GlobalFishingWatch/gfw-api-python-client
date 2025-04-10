# Documentation

## What's this?

This directory contains the source code for Global Fishing Watch API Client documentation (under `source/`) and `build scripts`. The documentation uses Sphinx, reStructuredText and Markdown. We use `furo` as the documentation theme.

## Building the documentation

Install Sphinx and other dependencies (i.e. theme etc.) needed for the documentation. Navigate to the project's `root` directory and run:

```bash
make install
```

Build the documentation using the following command:

```bash
make docs
```

The generated documentation will be placed in the `docs/build` directory. Open `docs/build/index.html` in your web browser to view it.

## Helpful documentation commands

Build, watch and serve documentation with live reload in the browser:

```bash
make servedocs
```

Clean the documentation build:

```bash
make -C docs clean
```

Test and check the links found in the documentation:

```bash
make -C docs linkcheck
```

Test and check the links found in the documentation:

```bash
make -C docs
```

## Documentation on GitHub Pages

The Global Fishing Watch API Client Documentation is hosted on GitHub Pages. The latest version can be accessed at https://globalfishingwatch.github.io/gfw-api-python-client/.
