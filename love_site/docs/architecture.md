# Technical Architecture - love_site

## Overview

`love_site` is a web application specialized in creating personalized romantic gifts. Developed with Flask, it integrates a modular and maintainable architecture, respecting SOLID principles and Python development best practices. The application offers an immersive emotional user experience through sophisticated JavaScript animations and professional responsive design.

## Project Structure

```
love_site/
├── app/                    # Main application code
│   ├── __init__.py         # Flask application factory
│   ├── main.py             # Entry point
│   ├── config.py           # Base configuration
│   ├── routes/             # Route definitions
│   │   └── home.py         # Blueprint for home page
│   ├── services/           # Business logic
│   │   └── messages.py     # Message management service
│   ├── data/               # Static data
│   │   └── messages.json   # Love messages with templates
│   ├── templates/          # Jinja2 templates
│   │   ├── base.html       # Base template
│   │   └── index.html      # Main page
│   └── static/             # Static assets
│       ├── css/
│       │   └── style.css   # Romantic and responsive styles
│       └── js/
│           ├── hearts.js   # Floating hearts animation
│           └── animation.js # Typing animation and carousel
├── tests/                  # Automated tests
│   ├── unit/               # Unit tests
│   ├── integration/        # Integration tests
│   └── application/        # Application tests
├── docs/                   # Documentation
└── pyproject.toml          # Dependency configuration
```

## Architectural Principles

### Separation of Responsibilities
- **Routes**: HTTP request handling and template rendering
- **Services**: Business logic (loading and personalizing messages)
- **Templates**: HTML presentation
- **Static**: Assets (CSS, JS) for interactivity and styling
- **Data**: Static data (JSON messages)

### Customization
- Messages use placeholders (`{lover}`, `{sender}`) replaced dynamically
- Elegant default values for smooth experience
- Simple and intuitive user interface

### Animations
- **Floating hearts**: Generated randomly with romantic colors
- **Progressive text**: Letter-by-letter typing animation with navigation carousel
- **Smooth transitions**: Modern CSS for interactions
- **Data transmission**: Direct injection in JavaScript via `<script>` tags to avoid HTML escaping conflicts

### Responsive Design
- Mobile/desktop adaptation
- Consistent romantic color palette
- Accessibility and performance

## Technologies

- **Backend**: Python 3.8+, Flask
- **Frontend**: HTML5, CSS3, JavaScript ES6
- **Tests**: pytest
- **Dependency management**: uv
- **Templates**: Jinja2

## Security and Best Practices

- User input validation
- Robust error handling
- Modular and testable code
- Comments and documentation
- PEP 8 standards compliance

This architecture allows for easy evolution: adding new routes, customizations, or integration of other romantic features.
