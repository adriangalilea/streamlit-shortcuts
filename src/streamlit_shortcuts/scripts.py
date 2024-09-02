import subprocess
import sys
import os


def run_checks():
    commands = [
        ["black", "src", "tests", "scripts.py", "--exclude", "venv"],
        [
            "flake8",
            "src",
            "tests",
            "scripts.py",
            "--exclude",
            "venv",
            "--config=.flake8",
        ],
        ["pytest", "tests"],
    ]

    for command in commands:
        print(f"Running: {' '.join(command)}")
        result = subprocess.run(command)
        if result.returncode != 0:
            print(f"Command failed: {' '.join(command)}")
            sys.exit(result.returncode)

    print("All checks passed successfully!")


if __name__ == "__main__":
    run_checks()

# Expose the run_checks function
__all__ = ["run_checks"]


def run_checks():
    """Run all checks."""
    commands = [
        "black src tests --exclude venv",
        "flake8 src tests --exclude venv --config=.flake8",
        "pytest tests",
    ]

    for command in commands:
        print(f"Running: {command}")
        result = os.system(command)
        if result != 0:
            print(f"Command failed: {command}")
            sys.exit(1)

    print("All checks passed successfully!")
