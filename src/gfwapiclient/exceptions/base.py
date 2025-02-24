"""Global Fishing Watch (GFW) API Python Client - Base Errors."""

__all__ = [
    "GFWError",
]


class GFWError(Exception):
    """Base exception class for errors related to the GFW API client.

    This exception serves as the parent class for all errors raised by the
    `gfwapiclient`, making it useful for broad exception handling.

    Example:
        ```python
        try:
            gfw = GFW(api_token="<PASTE_YOUR_TOKEN_HERE>")
        except gfwapiclient.GFWError as exc:
            print(f"GFW Exception: {exc}")
        ```
    """

    pass
