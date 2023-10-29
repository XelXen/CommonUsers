# CommonUsers

A tool to retrieve common users among telegram groups/channels/supergroups

## Features

- Retrieve all users from a specified Telegram group.
- Find common users between multiple groups.
- Exclude specified users from the results.

## Prerequisites

- Python 3.6 or above
- Pyrogram library

## Installation

1. Clone the repository: `git clone https://github.com/xelxen/commonusers.git`
2. Install the requirements: `pip install -r requirements.txt`
3. Replace the `api_id` and `api_hash` in `VarFile.py` with your actual Telegram API ID and API hash.

## Usage

1. Run the script: `python main.py`
2. When prompted, enter the ID, link or username of the Telegram group/channel/supergroup.

## Disclaimer

This project is for educational purposes only. It is not our responsibility if it is used for malicious purposes. Please use this script responsibly.

## Note

If you are entering the the group id, make sure that the group/channel is public and if the group is private, you must be a member of it to retrieve the users list. As for channels, you must be an admin to see channel subscribers

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
