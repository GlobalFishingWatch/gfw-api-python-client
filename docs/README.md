# Global Fishing Watch API Client Documentation

## What's this?

This directory contains the source code for Global Fishing Watch API Client documentation (under `source/`) and `build scripts`. The documentation uses Sphinx, reStructuredText and Markdown. We use `furo` as the documentation theme.

## Building the documentation

Install Sphinx and other dependencies (i.e. theme etc.) needed for the documentation. From the project `root` directory, use:

```bash
make install
```

Build the documentation like this:

```bash
make docs
```

The built documentation will be placed in the `docs/build` directory. Open
`docs/build/index.html` to view the documentation.

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

For more commands run:

```bash
make -C docs
```

## Documentation on Github Pages

The Global Fishing Watch API Client Documentation is hosted on Github Pages, and the latest version can be found at https://globalfishingwatch.github.io/gfw-api-python-client/.
