# Development Guide - love_site

## System Prerequisites

- **Python**: Version 3.8 or higher
- **Dependency manager**: uv (recommended for its speed and reliability)

## Development Environment Configuration

### 1. Source Code Retrieval
```bash
git clone <repository-url>
cd love_site
```

### 2. Dependency Installation
```bash
# Optimized installation with uv
uv sync

# Environment verification (optional)
uv run --isolated python --version
```

### 3. Installation Validation
```bash
# Run tests to verify integrity
uv run pytest
```

## Development Cycle

### Starting Local Server
```bash
# Main command
uv run python app/main.py

# Alternative with Flask CLI
uv run flask run
```

**Access point**: http://localhost:5000

### Iterative Process
1. **Code modification** in the `app/` directory
2. **Automatic testing** of changes via browser
3. **Run tests**: `uv run pytest`
4. **Validation** of code quality

## Automated Testing Strategy

### Complete Execution
```bash
uv run pytest
```

### Specialized Tests
```bash
# Unit tests - isolated business logic
uv run pytest tests/unit/

# Integration tests - component interactions
uv run pytest tests/integration/

# Application tests - global behavior
uv run pytest tests/application/

# Coverage analysis
uv run pytest --cov=app --cov-report=html
```

### Continuous Monitoring (Optional)
```bash
# Installation: uv add --dev pytest-watch
uv run pytest-watch
```

## Version Management and Collaboration

### Branches and Commits
```bash
# Create functional branch
git checkout -b feature/enhancement-description

# Development and validation
git add .
git commit -m "feat: implementation of new functionality

- Detailed description of changes
- Impact on other components
- Added/modified tests"

# Validation before submission
uv run pytest
```

### Pull Request
```bash
# Synchronization
git push origin feature/enhancement-description

# Create PR with complete description
# Include screenshots if applicable
```

## Deployment and Production

### Development Environment
- Local server: `uv run python app/main.py`
- Debug enabled for development

### Production Environment
- **WSGI Server**: Gunicorn or uWSGI recommended
- **Environment Variables**: Secure configuration
- **Logs**: Monitoring and rotation
- **SSL/TLS**: Mandatory encryption

### Containerization (Optional)
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY pyproject.toml .
RUN pip install uv && uv sync --no-dev
COPY . .
EXPOSE 5000
CMD ["uv", "run", "python", "app/main.py"]
```

## Quality Standards and Best Practices

### Code Quality
- **PEP 8**: Strict compliance with Python standards
- **Tests**: Coverage > 80%, TDD preferred
- **Documentation**: Complete docstrings, up-to-date README
- **Commits**: Descriptive and conventional messages

### Testing and Validation
- **Coverage**: Maintain > 80% global
- **Error Cases**: Robust exception handling
- **Mocks**: Isolation of external dependencies
- **Performance**: Load tests if necessary

### Performance and Optimization
- **Static Assets**: Minification and caching
- **HTTP Requests**: Minimization and optimization
- **Database**: Indexing and optimized queries
- **Caching**: Intelligent cache if applicable

## Troubleshooting and Maintenance

### Common Issues

#### Dependencies
```bash
# Complete environment regeneration
uv sync --reinstall

# Cache cleanup
uv cache clean
```

#### Failing Tests
- Verification of relative paths
- Validation of fixtures and mocks
- Consistency of test data

#### Frontend Animations
- Browser developer console
- Cross-browser compatibility
- Validation of asset paths
- JavaScript data transmission: Use `<script>` tags to inject data instead of HTML `data-*` attributes to avoid escaping issues with special characters (apostrophes, quotes)

#### Performance
- Profiling with `cProfile`
- SQL query optimization
- Cache and compression

### Preventive Maintenance
- **Updates**: Dependencies and security
- **Monitoring**: Logs and metrics
- **Backups**: Critical data
- **Documentation**: Continuous update

## External Contribution

### Standard Process
1. **Fork** the main repository
2. **Dedicated feature branch**
3. **Development with tests**
4. **Pull Request** with detailed description
5. **Review** and automated validation
6. **Merge** after approval

### Quality Criteria
- Passing tests and maintained coverage
- Positive code review
- Updated documentation
- Compliance with project standards

This methodology ensures professional, maintainable, and scalable development for love_site.
