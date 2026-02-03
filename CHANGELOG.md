# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning]().

## [0.0.4] - (2026-02-02) - Milestone 4 - Final Submission

### Added
- Introduced a comprehensive project tutorial written in Quarto, including worked examples and updated figures.
- Added a project retrospective page and integrated it into the documentation site.
- Added docstrings to all test files.
- Added inline code comments to the plotting script to improve readability.

### Changed
- Refactored the public API to follow snake_case naming conventions for all functions and tests.
- Renamed functions to follow snake_case conventions:
    - LatLongBinning → lat_long_binning
    - LatLongDistance → lat_long_distance
    - PlotBinnedLatLong → plot_binned_lat_long- Updated and regenerated reference documentation to reflect API changes.
- Updated the README with clearer usage examples and documentation links.
- Updated pyproject.toml to reflect project configuration changes.

### Improved
- Expanded and adjusted the test suite to achieve 100% test coverage.

## [0.0.3] - (2026-01-25) - Milestone 3

### Added
- Introduced package versioning and release management.
- Added GitHub Actions workflows for testing and building.
- Enabled automated testing across multiple Python versions.
- Added deployment workflows for publishing to TestPyPI.
- Created and published a Quarto documentation site.

### Changed
- Improved documentation structure and organization.
- Updated docstrings to include clearer error handling and usage descriptions.
- Refined deployment and CI configuration for reliability.

## [0.0.2] - (2026-01-17) - Milestone 2

### Added
- Completed and tested the PlotBinnedLatLong functionality.
- Added configurable bin width and height parameters.
- Expanded unit test coverage for core functionality.

### Changed
- Improved API consistency through refactoring and function renaming.
- Clarified and expanded project dependencies.
- Enhanced README documentation with setup and testing instructions.

### Fixed
- Removed Python cache files and unnecessary artifacts from version control.
- Cleaned up repository structure and internal comments.

## [0.0.1] - (2026-01-10) - Milestone 1

### Added
- Implemented core geospatial functionality, including LatLongDistance, LatLongBinning, PlotBinnedLatLong.
- Added foundational binning logic for latitude–longitude data.
- Established the initial project structure and package organization.
- Created initial documentation, including README and usage examples.
- Applied open-source licensing.

