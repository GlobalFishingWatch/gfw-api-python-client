## v1.2.0 (2025-09-02)

### Feat

- **fourwings**: add methods to create AIS and SAR presence reports
- **fourwings**: support AIS vessel presence dataset in create report API

## v1.1.0 (2025-06-08)

### Feat

- add support for Python 3.11
- **datasets**: implement get SAR fixed infrastructure API endpoint

## v1.0.1 (2025-04-11)

### Feat

- **events**: implement get events and get events stats API endpoints
- **vessels**: implement search and get by ids API endpoints
- **fourwings**: implement report API endpoints and models
- **insights**: implement vessel insights API endpoints and models
- **client**: implement and test Client
- **references**: implement regions API endpoints and models
- **http**: add abstract request method in abstract base class for API endpoints
- **http**: implement and test base endpoints and resource
- **exceptions**: implement and test HTTP exception handling and hierarchy
- **exceptions**: implement and test model validation error hierarchy
- add version metadata file and integrate with commitizen
- **http**: add base HTTP request parameters, body and response models
- **http**: enhance authentication and default headers
- **exceptions**: enhance GFWError with __str__ and __repr__
- **http**: add `HttpClient` and base `GFWError` for error handling
- **core**: introduce `BaseModel` for domain data models

### Refactor

- **fourwings**: rename get_report to create_report
- **exceptions**: define GFWAPIClientError default error message a constant
- **exceptions**: rename `GFWError` to `GFWAPIClientError`
- **http**: rename `HttpClient` to `HTTPClient`
