Task Instructions for the Agent

A1: Generate Required Data
🔹 Goal: Run datagen.py to generate necessary data files.
🔹 Steps:
        Check if uv is installed. If not, install it.
        Download and execute datagen.py with the user’s email as the only argument.
        Ensure that the generated data files exist before proceeding to other tasks.


A2: Format Markdown File
🔹 Goal: Use prettier to format /data/format.md cleanly and consistently.
🔹 Steps:
        Verify if prettier@3.4.2 is installed. If not, install it.
        Run prettier --write /data/format.md to format the file in place.
        Confirm that the file was updated successfully.

A3: Count Wednesdays in a Date List
🔹 Goal: Count how many dates in /data/dates.txt fall on a Wednesday.
🔹 Steps:

        Read /data/dates.txt, ensuring each line contains a valid date.
        Convert each date to a weekday and count occurrences of Wednesdays.
        Write just the count (a single number) to /data/dates-wednesdays.txt.

A4: Sort Contacts by Name
🔹 Goal: Sort an array of contacts in /data/contacts.json by last_name and then first_name.
🔹 Steps:

        Load the JSON file and parse the array of contacts.
        Sort the contacts alphabetically:
        First by last_name.
        If last names are the same, sort by first_name.
        Save the sorted contacts back to /data/contacts-sorted.json.

A5: Extract Most Recent Log Entries
🔹 Goal: Write the first line of the 10 most recent .log files from /data/logs/ to /data/logs-recent.txt.
🔹 Steps:

        Find all .log files in /data/logs/.
        Sort them by modification date, newest first.
        Read the first line of each file and collect up to 10 lines.
        Write the results to /data/logs-recent.txt, maintaining the order.

A6: Create an Index of Markdown Titles
🔹 Goal: Extract the first H1 (# Heading) from each Markdown file in /data/docs/ and build an index.
🔹 Steps:

        Find all .md files in /data/docs/.
        Read each file and extract the first line that starts with # .
        Store each filename (without /data/docs/ prefix) and its title in a JSON object.
        Save the result as /data/docs/index.json.
        Example output:

        json
        Copy
        Edit
        {
        "README.md": "Home",
        "large-language-models.md": "Large Language Models"
        }


A7: Extract Sender’s Email from an Email File
🔹 Goal: Identify the sender’s email from /data/email.txt using an LLM.
🔹 Steps:

        Read the contents of /data/email.txt.
        Pass the text to an LLM with instructions: "Extract only the sender’s email address."
        Write just the extracted email address to /data/email-sender.txt.


A8: Extract Credit Card Number from an Image
🔹 Goal: Use an LLM to extract a credit card number from an image and save it in a clean format.
🔹 Steps:

        Pass /data/credit-card.png to an LLM that can process images.
        Instruct the LLM to extract the card number and remove spaces.
        Write the cleaned number to /data/credit-card.txt.


A9: Find the Most Similar Comments
🔹 Goal: Use embeddings to find the two most similar comments in /data/comments.txt.
🔹 Steps:

        Read all comments from the file.
        Generate embeddings for each comment.
        Find the most similar pair based on cosine similarity.
        Write both comments (one per line) to /data/comments-similar.txt.


A10: Calculate Total Sales for "Gold" Tickets
🔹 Goal: Find the total revenue from Gold ticket sales in /data/ticket-sales.db.
🔹 Steps:

        Connect to the SQLite database.
        Run the query:
        sql
        Copy
        Edit
        SELECT SUM(units * price) FROM tickets WHERE type = "Gold";
        OR
        SELECT SUM(units * price) FROM tickets WHERE LOWER(type) = "gold";
    Write the total revenue as a single number to /data/ticket-sales-gold.txt.


Final Notes for the Agent:
    Make sure to handle file existence checks before processing.
    Validate outputs after execution.
    log errors or unexpected results for troubleshooting.