# Contributing Guidelines

Thank you for your interest in contributing to AI-Guard! This document provides guidelines and instructions for contributing to the project.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Workflow](#development-workflow)
- [Pull Request Process](#pull-request-process)
- [Coding Standards](#coding-standards)
- [Testing](#testing)
- [Documentation](#documentation)
- [Issue Reporting](#issue-reporting)
- [Feature Requests](#feature-requests)
- [Communication](#communication)

## Code of Conduct

By participating in this project, you agree to maintain a respectful and inclusive environment for everyone. Please be kind and courteous in all interactions.

Key principles:
- Be respectful of differing viewpoints and experiences
- Accept constructive criticism gracefully
- Focus on what is best for the community and project
- Show empathy towards other community members

## Getting Started

1. **Set up your development environment** following the [Development Setup Guide](setup.md).

2. **Fork the repository** to your GitHub account.

3. **Clone your fork** to your local machine:
   ```bash
   git clone https://github.com/your-username/ai-guard.git
   cd ai-guard
   ```

4. **Add the upstream remote** to keep your fork updated:
   ```bash
   git remote add upstream https://github.com/original-owner/ai-guard.git
   ```

5. **Create a new branch** for your work:
   ```bash
   git checkout -b feature/your-feature-name
   ```

## Development Workflow

1. **Check the roadmap** and [Issues](https://github.com/your-username/ai-guard/issues) to find something to work on.

2. **Keep your branch updated** with the upstream main branch:
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```

3. **Make your changes** in small, logical commits.

4. **Follow the [coding standards](#coding-standards)**.

5. **Run tests** to ensure your changes don't break existing functionality.

6. **Update documentation** as needed.

7. **Create a pull request** when your changes are ready for review.

## Pull Request Process

1. **Update your branch** with the latest changes from the upstream main branch.

2. **Run all tests** to ensure your changes don't break existing functionality.

3. **Push your changes** to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```

4. **Create a pull request** from your branch to the upstream main branch.

5. **Fill out the pull request template** with a clear description of your changes.

6. **Address review feedback** and make necessary changes.

7. **Your pull request will be merged** once it meets all requirements and passes review.

### Pull Request Template

```markdown
## Description
[Provide a brief description of the changes in this PR]

## Related Issue
[Link to the related issue (if applicable)]

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Code refactoring
- [ ] Performance improvement
- [ ] Tests

## Testing
[Describe the testing you have performed]

## Screenshots (if applicable)
[Include screenshots if your change includes visual elements]

## Checklist
- [ ] My code follows the project's coding standards
- [ ] I have added tests that prove my fix/feature works
- [ ] I have updated the documentation accordingly
- [ ] My changes don't introduce any new warnings or errors
```

## Coding Standards

We follow strict coding standards to maintain code quality and consistency:

### Python Style Guide

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide
- Use [Black](https://black.readthedocs.io/) formatter with default settings
- Sort imports with [isort](https://pycqa.github.io/isort/)
- Follow [Google's docstring style](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html)
- Use type hints according to [PEP 484](https://www.python.org/dev/peps/pep-0484/)

### Code Quality Tools

Before submitting a pull request, run these tools on your code:

```bash
# Format code with Black
black ai_guard tests

# Sort imports
isort ai_guard tests

# Check code quality with flake8
flake8 ai_guard tests

# Run type checking
mypy ai_guard
```

### Naming Conventions

- **Variables and functions**: Use `snake_case`
- **Classes**: Use `PascalCase`
- **Constants**: Use `UPPER_SNAKE_CASE`
- **Private methods/variables**: Prefix with underscore (`_private_method`)
- **Module names**: Short, lowercase words (no underscores)

### Git Commit Messages

- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit the first line to 72 characters or less
- Reference issues and pull requests after the first line
- Consider using the [Conventional Commits](https://www.conventionalcommits.org/) format

### Example Commit Message

```
feat: Add multi-angle face verification

Implement verification using embeddings from multiple face angles.
This improves recognition accuracy in challenging conditions.

Closes #123
```

## Testing

All code contributions should include appropriate tests:

### Test Requirements

- Write unit tests for all new functionality
- Ensure existing tests continue to pass
- Aim for high test coverage (at least 80%)
- Include both positive and negative test cases

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage report
pytest --cov=ai_guard

# Run specific test file
pytest tests/test_detection.py
```

## Documentation

Documentation is a crucial part of the project:

### Code Documentation

- All modules, classes, and functions should have docstrings
- Complex algorithms should include explanatory comments
- Use inline comments sparingly and only for non-obvious code

### Project Documentation

- Update relevant documentation when adding or changing features
- Follow the existing documentation style and format
- Create new documentation pages as needed

### Example Docstring

```python
def compare_embeddings(embedding1, embedding2):
    """Compare two face embeddings using cosine similarity.
    
    Args:
        embedding1 (np.ndarray): First face embedding vector.
        embedding2 (np.ndarray): Second face embedding vector.
        
    Returns:
        float: Similarity score between 0 and 1, where higher values
              indicate greater similarity.
              
    Raises:
        ValueError: If the embeddings have different dimensions.
    """
```

## Issue Reporting

If you find a bug or have a suggestion:

1. **Check existing issues** to avoid duplicates.

2. **Create a new issue** using the appropriate template.

3. **Provide detailed information** including:
   - Steps to reproduce (for bugs)
   - Expected behavior
   - Actual behavior
   - Screenshots or logs if applicable
   - System information (OS, Python version, etc.)

## Feature Requests

Feature requests are welcome:

1. **Check the roadmap** to see if your feature is already planned.

2. **Create a new issue** using the feature request template.

3. **Describe the feature** in detail, including:
   - Problem it solves
   - Proposed solution
   - Alternatives considered
   - Potential implementation approach

## Communication

Clear communication is essential for collaboration:

### Channels

- **GitHub Issues**: For bug reports, feature requests, and task tracking
- **Pull Requests**: For code reviews and feature discussions
- **Documentation**: For long-term knowledge sharing

### Guidelines

- Be clear and concise in your communications
- Provide context and background information
- Ask questions when uncertain — it’s better to ask than assume
- Respect differing time zones and availability; contributors may respond asynchronously

---

## 💡 Good First Issues

New to the project? Start with issues labeled [`good first issue`](https://github.com/your-org/ai-guard/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22) or [`help wanted`](https://github.com/your-org/ai-guard/issues?q=is%3Aissue+is%3Aopen+label%3A%22help+wanted%22). These are ideal for onboarding and understanding how the project works.

---

## 🧩 Design & Architecture Contributions

If you're proposing a new feature with architectural impact or contributing to ML pipeline components:

1. Open an issue titled **[Proposal] Your Feature Title**
2. Clearly outline:
   - The problem you’re solving
   - High-level design or model changes
   - Integration points
   - Estimated impact
3. Optionally, include diagrams or flowcharts to support your design

---

## 🧪 Machine Learning Contributions

For those contributing to detection or recognition models:

- Include:
  - Dataset details (source, licenses)
  - Preprocessing pipeline
  - Training logs (accuracy/loss metrics)
  - Evaluation metrics (precision/recall/ROC)
  - Clear explanation of improvements
- Ensure models are versioned and reproducible
- Prefer saving models in `SavedModel` or `TorchScript` format for deployment

---

## 🧾 Licensing & Legal

- By submitting a contribution, you agree to license your code under the [MIT License](LICENSE)
- You must own or have rights to the code you contribute
- Do not submit proprietary or third-party code without explicit permission

---

## 🙌 Acknowledgements

We deeply appreciate your time and effort in helping improve **AI-Guard**. Whether it's your first PR or your fiftieth, your contributions move this project forward and help make ENSAM a safer, smarter campus.

---

🛠 Let's build AI that protects and empowers our academic community!

– The AI-Guard Team
