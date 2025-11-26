# How does python work?
Python installation consists of:
    1. Python interpreter (binary executable) + built-in functions
    2. Standard library (modules like os, sys, etc.)
    3. site-packages directory (for third-party packages)

When you run Python files, they're executed by the interpreter binary (python/python3 on Unix, python.exe on Windows).

# What is Virtualization?
Virtualization (via virtual environments) creates an isolated Python environment with:
- References/symlinks to the base Python interpreter
- A separate site-packages directory for project-specific packages
- Activation scripts to switch contexts

# Why Virtualization?
1. **Dependency Isolation**: Different projects can use different versions of the same package
2. **Reproducibility**: Lock dependencies per project
3. **Clean Base Environment**: Avoid cluttering the system Python
4. **Version Testing**: Test code against different package versions safely