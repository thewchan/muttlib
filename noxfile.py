"""Entrypoint for nox."""
import nox


@nox.session(reuse_venv=True)
def tests(session):
    """Run all tests."""
    session.install(".[all]")
    cmd = ["pytest", "-n", "auto"]
    if session.posargs:
        cmd.extend(session.posargs)
    session.run(*cmd)


@nox.session(reuse_venv=True)
def cop(session):
    """Run all pre-commit hooks."""
    session.install(".[dev,test]")
    session.run("pre-commit", "install", "-c", ".pre-commit-config-nox.yaml")
    session.run(
        "pre-commit",
        "run",
        "--show-diff-on-failure",
        "--all-files",
        "-c",
        ".pre-commit-config-nox.yaml",
    )


@nox.session(reuse_venv=True)
def bandit(session):
    """Run all pre-commit hooks."""
    session.install("bandit")
    session.run("bandit", "-r", "muttlib/", "-ll", "-c", "bandit.yaml")
