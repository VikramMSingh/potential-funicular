import logging  # standard logging module for structured log messages
from collections import Counter  # convenient counter for tallying occurrences
from pathlib import Path  # pathlib for cross-platform path handling
from typing import Optional  # typing helpers (not strictly used here)

# Configure the root logger to write INFO+ messages to 'app.log'
# - filename: output file
# - filemode 'a': append to the file
# - level: minimum level to record
# - format: simple 'LEVEL: message' format
logging.basicConfig(filename='app.log', filemode='a', level=logging.INFO, format="%(levelname)s: %(message)s")
# Create a module-level logger for more targeted logging calls
logger = logging.getLogger(__name__)


def parse_errors(filepath: str, top_n: int = 5):
    """
    Parse a log file and return the top N most frequent error codes.

    Args:
        filepath: path to the log file to parse.
        top_n: number of top error codes to return.

    Returns:
        List of (error_code, count) tuples, sorted by count descending.
    """
    # Convert the input string to a Path object for convenience
    path = Path(filepath)

    # If the file doesn't exist, log an error and raise an exception
    if not path.exists():
        logging.error(f"Log file not found: {filepath}")
        raise FileNotFoundError(f"Log file not found: {filepath}")

    # Counter will track how many times each error code appears
    error_counter: Counter = Counter()

    # Open the file using utf-8 encoding and iterate line by line
    with path.open("r", encoding="utf-8") as f:
        for line_num, line in enumerate(f, start=1):
            # Trim surrounding whitespace/newlines
            line = line.strip()
            # Skip blank lines
            if not line:
                continue

            # Split the line into whitespace-separated fields
            parts = line.split()
            # If there are fewer than 4 fields we consider the line malformed
            if len(parts) < 4:
                # Log a warning including the problematic line and line number
                logger.warning(f"Malformed line {line}, skipping: {line_num}")
                continue

            # According to the expected log format, the 3rd token is the level (e.g., INFO/ERROR)
            level = parts[2]
            # The 4th token is expected to be an error or status code
            code = parts[3]

            # Only count entries where the level equals "ERROR"
            if level == "ERROR":
                error_counter[code] += 1

            # Log progress at INFO level (this will append a log line for each parsed input line)
            # Consider moving or throttling this in production to avoid noisy logs.
            logger.info(f"Parsed {len(error_counter)} unique error codes")

    # Return the top_n most common error codes as (code, count) pairs
    return error_counter.most_common(top_n)


# Script entry point: when run directly, parse 'logs.txt' and print the top results
if __name__ == "__main__":
    results = parse_errors("logs.txt", top_n=10)
    for error_code, count in results:
        # Print to stdout so the user sees results on the console
        print(f"Error Code: {error_code}, Count: {count}")
