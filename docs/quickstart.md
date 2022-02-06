Quickstart Guide
================

Requirements
------------

- The library installed. Instructions to install the libary shown at the [Installation - Getting Started page](https://invalidlenni.de/simple-amari.py/getting-started/installation.md/).
- An Amari API authorization token. Instructions to getting access shown at the [Getting Access - Getting Started page](https://invalidlenni.de/simple-amari.py/getting-started/getting-access.md/).

Example
-------

Comparing Users

```py

    # Imports a package used to run the asyncronous function.
    import asyncio

    # Importing the package
    from amari import AmariClient

    # The function to compare users level
    async def compare_users_level(guild_id, users: list):
        # Initialize the package
        # Make sure to put your api token here
        amari = AmariClient("authorization_token")

        # Fetches the users and sets it to the response users var
        resp_users = (await amari.fetch_users(guild_id, users)).users

        # Closing the connection to the AmariAPI. You need to close the connection after you're done.
        await amari.close()

        # Makes sure 2 users are returned
        if len(resp_users) < 2:
            return False

        # Changes the dictionary of the users to a list of them
        users = [user for user in resp_users.values()]

        # Returns if their levels are the same
        return users[0].level == users[1].level


    # Runs the function using asyncio due to trying to run an async function in a non-async enviroment.
    # Make sure to add the user ids as a string value. The string will be changed in the future to a snowflake value.
    print(asyncio.run(compare_users_level(guild_id, ["user_id", "user_id"])))
```
