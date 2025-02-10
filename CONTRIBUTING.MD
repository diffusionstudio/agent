# Contributing to Video Composer Agent

Thanks for your interest in contributing! Here's how to get started.

## Development Setup

1. Fork and clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/video-composer-agent.git
cd video-composer-agent
```

2. Install dependencies with uv
```bash
pip install uv
uv sync
```

3. Set up pre-commit hooks
```bash
uv pip install pre-commit
pre-commit install
```

## Code Style

We use several tools to ensure code quality:

- [Ruff](https://github.com/astral-sh/ruff) for linting and formatting
- Pre-commit hooks for automated checks
- YAML/TOML validation
- Automatic dependency updates with uv

The pre-commit hooks will run automatically when you commit. You can also run them manually:
```bash
pre-commit run --all-files
```

## Pull Request Process

1. Create a new branch for your feature
```bash
git checkout -b feature/your-feature-name
```

2. Make your changes and commit them
```bash
git add .
git commit -m "feat: your descriptive commit message"
```

3. Push to your fork and create a Pull Request

4. Ensure your PR:
   - Passes all pre-commit checks
   - Includes relevant tests if adding new functionality
   - Updates documentation as needed
   - Has a clear description of the changes

## Environment Variables

1. Copy `.env.example` to `.env`
```bash
cp .env.example .env
```

2. Add your API keys and other required variables
3. Never commit your `.env` file

## Need Help?

- Join our [Discord](https://discord.com/invite/zPQJrNGuFB)
- Check existing issues and PRs
- Create an issue for discussion
