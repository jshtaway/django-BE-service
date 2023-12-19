# TDD

This repository follows the Test-Driven Development (TDD) approach.

Test-Driven Development is a software development process that emphasizes writing automated tests before writing the actual code. It follows a cycle of writing a failing test, and then writing the functional code to test and design specifications.

By using TDD, this repository aims to ensure that the code is thoroughly tested and that new features or changes do not introduce regressions. It promotes a more robust and maintainable codebase.

# Continuous Integration

This project utilizes GitHub Actions, a continuous integration and delivery platform, to automate the testing and validation of the codebase. The tests are written using pytest-bdd, a behavior-driven development framework for Python.

GitHub Actions allows for the seamless integration of pytest-bdd into the development workflow. It automatically runs the tests whenever changes are pushed to the repository, ensuring that the codebase remains in a consistent and working state.

To view the workflow configuration and learn more about how the tests are executed, please refer to the [`.github/workflows/checks.yml`](/.github/workflows/checks.yml) file.

# django-BE-service

This project is a backend service written in Django. It provides functionality for reading, adding, and removing recipes. Users can create accounts to manage their recipes. The project also supports image storage for recipes.

The project is hosted using Docker on AWS, which allows for easy deployment and scalability. The data is stored in a PostgreSQL database, ensuring reliability and data integrity.

To get started with the project, please refer to the installation and setup instructions in the [documentation](/docs/INSTALLATION.md).

For more information on how to use the API and interact with the backend service, please refer to the [API documentation](/docs/API.md).

If you encounter any issues or have any questions, please feel free to open an issue in the [issue tracker](https://github.com/your-username/django-BE-service/issues).

Happy cooking!

