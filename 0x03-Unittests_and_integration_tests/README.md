# Python Utility Modules

A collection of Python utility modules providing functionality for nested data access, data processing, and GitHub API interaction.

## Modules

### `utils.py`
Core utility functions and classes for data manipulation and HTTP requests.

### `client.py` 
GitHub API client for interacting with organization data and repositories.

## Features

- **Nested Map Access**: Safe traversal of nested dictionary structures
- **Data Processing**: Filter and analyze dictionary-based datasets
- **HTTP JSON Fetching**: Robust JSON data retrieval from web APIs
- **GitHub API Integration**: Easy access to GitHub organization and repository data

## Installation

### Prerequisites
- Python 3.6 or higher
- `requests` library

### Setup
1. Install the required dependency:
```bash
pip install requests
```

2. Download or clone the modules:
```bash
# If using git
git clone <your-repository-url>
cd <repository-directory>

# Or download the files directly
# - utils.py
# - client.py
```

## Usage

### utils.py

#### `access_nested_map(nested_map, path)`
Safely access values in nested dictionaries using a sequence of keys.

```python
from utils import access_nested_map

# Example usage
data = {
    "user": {
        "profile": {
            "name": "Alice",
            "settings": {"theme": "dark"}
        }
    }
}

# Access nested values
name = access_nested_map(data, ("user", "profile", "name"))
# Returns: "Alice"

theme = access_nested_map(data, ("user", "profile", "settings", "theme"))
# Returns: "dark"
```

#### `DataProcessor` Class
Process and analyze lists of dictionary data.

```python
from utils import DataProcessor

# Sample data
users = [
    {"id": 1, "name": "Alice", "city": "New York", "age": 25},
    {"id": 2, "name": "Bob", "city": "London", "age": 30},
    {"id": 3, "name": "Charlie", "city": "New York", "age": 28},
]

processor = DataProcessor(users)

# Filter by key-value pairs
ny_users = processor.filter_by_key_value("city", "New York")
# Returns: [{"id": 1, "name": "Alice", ...}, {"id": 3, "name": "Charlie", ...}]

# Get all unique keys
keys = processor.get_all_keys()
# Returns: ["age", "city", "id", "name"]
```

#### `get_json(url)`
Fetch JSON data from web APIs.

```python
from utils import get_json

# Fetch data from an API
data = get_json("https://api.github.com/users/octocat")
print(data["login"])  # "octocat"
```

### client.py

#### `GithubOrgClient` Class
Interact with GitHub's public organization API.

```python
from client import GithubOrgClient

# Initialize client for an organization
client = GithubOrgClient("google")

# Get organization information
org_info = client.org()
print(f"Organization: {org_info['name']}")
print(f"Description: {org_info['description']}")
print(f"Public Repos: {org_info['public_repos']}")

# Get list of public repository names
repos = client.public_repos()
print(f"First 5 repositories: {repos[:5]}")
```


