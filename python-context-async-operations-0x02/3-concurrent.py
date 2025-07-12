import asyncio
import aiosqlite # For asynchronous SQLite interaction

db_name = "users.db"

# Asynchronous Database Functions
async def async_fetch_users():
    """
    Asynchronously fetches all users from the 'users' table.
    Returns:
        list: A list of tuples, each representing a user row.
    """
    async with aiosqlite.connect(db_name) as db:
        async with db.execute("SELECT * FROM users;") as cursor:
            return await cursor.fetchall()
        

async def async_fetch_older_users():
    """
    Asynchronously fetches users older than a specified age from the 'users' table.
    Args:
        min_age (int): The minimum age for users to be fetched.
    Returns:
        list: A list of tuples, each representing a user row.
    """
    async with aiosqlite.connect(db_name) as db:
        async with db.execute("SELECT * FROM users WHERE age > 40") as cursor:
            return await cursor.fetchall()

async def fetch_concurrently():
    """
    Executes multiple asynchronous database queries concurrently using asyncio.gather().
    Prints the results of each query.
    """
    
    print("--- Starting concurrent fetches ---")
    # Use asyncio.gather to run tasks concurrently
    all_users, older_users = await asyncio.gather(
        async_fetch_users(),
        async_fetch_older_users() # Fetch users older than 40
    )

    return all_users, older_users


