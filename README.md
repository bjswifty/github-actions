# Minimal Python Logging App with GitHub Actions Deployment

This is a minimal Python project demonstrating logging and automated redeployment using GitHub Actions.

## Project Structure

- `app.py`: Main Python application that logs a timestamped message using the built-in logging module
- `requirements.txt`: Dependencies file (empty, as only built-in modules are used)
- `.github/workflows/deploy.yml`: GitHub Actions workflow for automated deployment

## Features

- Logs a message with the current UTC datetime using Python's logging module
- Automatically runs on pull request merges to main branch
- Supports configurable cron-based scheduling (currently hourly)
- No external dependencies beyond Python standard library

## Local Development

1. Ensure Python 3.11+ is installed
2. Run the application: `python app.py`

## GitHub Actions Workflow

The workflow triggers on:
- Push to `main` branch (e.g., merged pull requests)
- Hourly schedule (configurable in `.github/workflows/deploy.yml`)

To modify the schedule, edit the `cron` expression in the workflow file. Examples:
- `'0 * * * *'`: Every hour
- `'0 0 * * *'`: Daily at midnight UTC