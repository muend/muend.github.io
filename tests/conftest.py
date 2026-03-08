import os
import pytest


def pytest_configure(config):
    """
    Ensure /app/index.html is accessible for E2E tests.

    The tests use 'file:///app/index.html' – the canonical path used when
    the repository is mounted at /app inside Docker.

    When running outside Docker (local development), this hook attempts to
    create a convenience symlink ``/app -> <repo root>``.  This requires
    write permission to the filesystem root.  If the symlink cannot be
    created (e.g. the user lacks root privileges), a clear warning is printed
    and the tests will fail with a "file not found" error rather than silently
    producing misleading results.

    The recommended way to run the tests without Docker is::

        sudo ln -s $(pwd) /app   # one-time setup
        pytest tests/
    """
    app_path = "/app"
    if not os.path.exists(app_path):
        repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        try:
            os.symlink(repo_root, app_path)
        except (PermissionError, OSError) as exc:
            pytest.warns(
                UserWarning,
                match=r"",
            )
            import warnings
            warnings.warn(
                f"Could not create /app symlink ({exc}). "
                "Tests expect 'file:///app/index.html' to be accessible. "
                "Run inside Docker or create the symlink manually: "
                f"sudo ln -s {repo_root} /app",
                UserWarning,
                stacklevel=1,
            )
