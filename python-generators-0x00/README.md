# ALX_prodev Database Seeding Script

A Python script for creating and populating a MySQL database with user data from CSV files. This script sets up the ALX_prodev database, creates the necessary table structure, and imports data while preventing duplicates.

## Features

- **Database Creation**: Automatically creates the ALX_prodev database if it doesn't exist
- **Table Setup**: Creates a user_data table with proper indexing
- **CSV Import**: Reads user data from CSV files and populates the database
- **Duplicate Prevention**: Checks for existing records before insertion
- **Data Streaming**: Provides a generator function for memory-efficient data retrieval
- **Error Handling**: Comprehensive error handling for database operations

## Prerequisites

### System Requirements
- Python 3.6 or higher
- MySQL Server 5.7 or higher
- MySQL root access (or appropriate user privileges)

### Python Dependencies
```bash
pip install mysql-connector-python
```

## Database Schema

The script creates a `user_data` table with the following structure:

| Column   | Type         | Constraints           |
|----------|-------------|-----------------------|
| user_id  | CHAR(36)     | PRIMARY KEY          |
| name     | VARCHAR(255) | NOT NULL             |
| email    | VARCHAR(255) | NOT NULL             |
| age      | DECIMAL(3,0) | NOT NULL             |

**Indexes:**
- Primary index on `user_id`
- Additional index on `user_id` for optimized queries

## CSV File Format

Your CSV file should have the following headers:
```csv
user_id,name,email,age
```

**Example CSV content:**
```csv
user_id,name,email,age
550e8400-e29b-41d4-a716-446655440000,John Doe,john.doe@example.com,25
550e8400-e29b-41d4-a716-446655440001,Jane Smith,jane.smith@example.com,30
```

