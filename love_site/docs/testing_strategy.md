# Automated Testing Strategy - love_site

## Overview

The testing strategy for `love_site` adopts a rigorous pyramidal approach, structured in three hierarchical levels: unit tests, integration tests, and application tests. This architecture ensures complete coverage of critical functionalities while maintaining optimal execution performance. The implementation relies on pytest as the main framework, with native integration of Python testing best practices.

## Test Levels

### 1. Unit Tests (`tests/unit/`)

**Objective**: Validate isolated business logic.

**Coverage**:
- Service functions (loading and personalizing messages)
- Error handling (missing files, invalid JSON)
- Placeholder replacement

**Examples**:
```python
def test_personalize_messages():
    messages = [{"id": 1, "text": "Hello {lover}"}]
    result = personalize_messages(messages, "Alice", "Bob")
    assert result[0]['text'] == "Hello Alice"
```

**Best Practices**:
- Use mocks for external dependencies (files, I/O)
- Test edge cases and errors
- Maintain > 90% coverage for services

### 2. Integration Tests (`tests/integration/`)

**Objective**: Validate interaction between components.

**Coverage**:
- Flask routes and template rendering
- Service/route integration
- Form handling and personalization

**Examples**:
```python
def test_index_post_with_data(client):
    data = {'lover_name': 'Marie', 'sender_name': 'Pierre'}
    resp = client.post('/', data=data)
    assert b'Marie' in resp.data
```

**Best Practices**:
- Use Flask test client
- Test POST and GET data
- Verify rendered HTML content

### 3. Application Tests (`tests/application/`)

**Objective**: Validate overall application behavior.

**Coverage**:
- Flask app creation and configuration
- Blueprint registration
- Static file access
- Complete template rendering

**Examples**:
```python
def test_app_creation():
    app = create_app(Config)
    assert app.config['TESTING'] is False
```

**Best Practices**:
- Test configuration
- Verify component integration
- Regression tests for major changes

## Quality Metrics

### Code Coverage
- **Target**: > 80% global
- **Services**: > 90%
- **Routes**: > 70%
- **Application**: > 60%

### Execution
- **Time**: < 30 seconds for all tests
- **Frequency**: At every commit (pre-push)
- **CI/CD**: Mandatory continuous integration

## Tools and Frameworks

### pytest
- Main testing framework
- Fixtures for reusability
- Parametrization for similar tests
- Plugins: coverage, pytest-watch

### Configuration
```toml
[tool.pytest]
addopts = "-q"
```

### Mocking
- `unittest.mock` for external dependencies
- Unit test isolation
- Error simulation (missing files, etc.)

## Tests by Functionality

### Customizable Messages
- ✅ Valid/invalid JSON loading
- ✅ Placeholder replacement
- ✅ Default values

### Routes and Forms
- ✅ GET/POST on /
- ✅ Data validation
- ✅ Conditional rendering (form/messages)

### Animations and Frontend
- ❌ Automated tests difficult (would require Selenium/Playwright)
- ✅ Documented manual tests
- ✅ Static asset verification

### Responsive Design
- ❌ CSS tests difficult to automate
- ✅ Manual tests on different devices
- ✅ HTML/CSS validation via external tools

## Test Workflow

### Development
1. Write unit tests first (TDD)
2. Implement the functionality
3. Integration tests
4. Application tests
5. Verify coverage

### CI/CD
```yaml
# GitHub Actions example
- name: Run tests
  run: uv run pytest --cov=app --cov-report=xml
- name: Upload coverage
  uses: codecov/codecov-action@v3
```

### Test Debugging
- Use `--pdb` for debugging
- Check Flask logs in test mode
- Isolate failing tests

## Test Maintenance

### Adding New Features
- Create tests before implementation
- Update existing tests if necessary
- Maintain coverage

### Refactoring
- Tests protect against regressions
- Refactor tests if code changes
- Remove obsolete tests

### Performance
- Optimize slow fixtures
- Use mocks to avoid I/O
- Parallelize if necessary

This strategy ensures the reliability and maintainability of the romantic site, allowing for safe evolutions and confident deployments.
