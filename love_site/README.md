# love_site

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/flask-3.1+-red.svg)](https://flask.palletsprojects.com/)
[![uv](https://img.shields.io/badge/dependency--manager-uv-green.svg)](https://github.com/astral-sh/uv)

An elegant web application developed in Python/Flask to create personalized romantic gifts. The application offers an immersive emotional experience with smooth animations and professional responsive design.

## Installation and Launch

### Prerequisites
- Python 3.8+
- uv (dependency manager)

### Installation
```bash
# Clone the repository
git clone <repository-url>
cd love_site

# Install dependencies with uv
uv sync
```

### Launch
```bash
# Start the server
uv run python app/main.py

# Or if necessary with explicit PYTHONPATH
PYTHONPATH=. uv run python app/main.py

# Alternative with Flask CLI
uv run flask run
```

Open `http://localhost:5000` in your browser.

## Usage

1. **Home page**: Fill the form with:
   - Loved one's first name (optional)
   - Sender's first name (default: Djochrist)

2. **Create the gift**: Click "Create the gift"

3. **Enjoy**: Let yourself be carried away by the animated love messages

4. **Navigation**: Use Previous/Next buttons or keyboard arrows

## Customization

### Love Messages
Modify `app/data/messages.json` to change the messages:
```json
{
  "messages": [
    { "id": 1, "text": "My customized message with {lover} and {sender}" }
  ]
}
```

### Styles and Colors
Edit `app/static/css/style.css` to customize the appearance.

### Animations
Adjust parameters in `app/static/js/hearts.js` and `app/static/js/animation.js`.

## Tests

### Run all tests
```bash
uv run pytest
```

### Specific tests
```bash
# Unit tests
uv run pytest tests/unit/

# Integration tests
uv run pytest tests/integration/

# Application tests
uv run pytest tests/application/

# With coverage
uv run pytest --cov=app --cov-report=html
```

## Project Structure

```
love_site/
├── app/
│   ├── __init__.py          # Flask factory
│   ├── main.py              # Entry point
│   ├── config.py            # Configuration
│   ├── routes/home.py       # Main route
│   ├── services/messages.py # Message logic
│   ├── data/messages.json   # Love messages
│   ├── templates/           # Jinja2 HTML
│   └── static/              # CSS, JS, assets
├── tests/                   # Automated tests
│   ├── unit/                # Unit tests
│   ├── integration/         # Integration tests
│   └── application/         # Application tests
├── docs/                    # Documentation
│   ├── architecture.md      # Technical architecture
│   ├── workflow.md          # Dev workflow
│   └── testing_strategy.md  # Testing strategy
├── pyproject.toml           # uv dependencies
└── README.md
```

## Documentation

Check `docs/` for:
- [Technical Architecture](docs/architecture.md)
- [Development Workflow](docs/workflow.md)
- [Testing Strategy](docs/testing_strategy.md)

## Technologies

- **Backend**: Python 3.8+, Flask 3.0+
- **Frontend**: HTML5, CSS3, JavaScript ES6
- **Tests**: pytest
- **Dependency management**: uv
- **Templates**: Jinja2

## Contribution

1. Fork the project
2. Create a `feature/my-feature` branch
3. Commit your changes
4. Push and create a Pull Request
5. Tests pass? Merge!

## License

This project is a gift of love — share it freely with the people you love.

## Improvement Ideas

- Add personalized photos
- Romantic sounds (optional)
- Different themes (Christmas, birthday...)
- PDF export of the gift
- Social media sharing

---

**Made with love for romantic moments**
