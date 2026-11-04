# NBA Stats CLI

A command-line project dedicated to exploring NBA data using Python and SQL.

## About the Project

This project loads NBA data from the public BALLDONTLIE API into a local SQLite database and allows users to explore the data through SQL queries.

The data includes NBA teams, games, and players. Users can answer questions such as which teams won the most games in a particular regular season, how many points they scored and allowed, and which colleges produced the most NBA lottery picks.

The main goal of this project was to practice and improve my knowledge of Python, SQL, databases, APIs, and Git while working with a subject I enjoy: basketball.

### Key Features

- **Team Rankings:** Ranks NBA teams by total wins, points scored, and points allowed during the regular season.
- **Back-to-Back Analysis (Work in Progress):** Intended to compare team performance in back-to-back games.
- **College Lottery Picks:** Lists the colleges with the most NBA lottery picks.

## Requirements

Before installing the project, make sure you have:

- **Python 3.12 or higher** — Main programming language.
- **Git** — Used to clone and manage the repository.
- **SQLite** — Local database, supported by Python's built-in `sqlite3` module.
- **SQLite CLI (`sqlite3`)** — Required to execute the reference SQL script from the terminal.
- **BALLDONTLIE API Key** — Required to retrieve NBA data. You can obtain a key at [BALLDONTLIE](https://www.balldontlie.io/).

The project also uses `pytest`, `mypy`, and `ruff` for testing and code quality checks. These tools are installed with the development dependencies.

## Installation

Follow these instructions to install and configure the project.

**1. Clone the repository**

```bash
git clone -b CLI_feature https://github.com/fernandofiore310/Nba-Stats-CLI.git
```

**2. Navigate to the project directory**

```bash
cd Nba-Stats-CLI
```

**3. Create a virtual environment (recommended)**

```bash
python -m venv .venv
```

**4. Activate the virtual environment**

On macOS/Linux:

```bash
source .venv/bin/activate
```

On Windows (PowerShell):

```powershell
.venv\Scripts\Activate.ps1
```

**5. Install the project and development dependencies**

Make sure you are using a recent version of pip:

```bash
python -m pip install --upgrade pip
```

Then install the project in editable mode, including the development dependencies defined in `pyproject.toml`:

```bash
python -m pip install --group dev -e .
```

Editable mode allows you to modify the project's source code without reinstalling the package after each change.

**6. Create the `.env` file and configure your API key**

Use the `.env.example` file to create your own `.env` file.

On macOS/Linux:

```bash
cp .env.example .env
```

On Windows (PowerShell):

```powershell
Copy-Item .env.example .env
```

Open the `.env` file and replace the placeholder with your BALLDONTLIE API key:

```env
BALLDONTLIE_API_KEY="your_api_key_here"
```

The environment variable must be named `BALLDONTLIE_API_KEY` for the application to work.

**Important:** Never commit your API key to GitHub. The `.env` file is already included in the project's `.gitignore`.

## Database Setup

Before loading NBA data, the local SQLite database must be prepared.

**Important:** All commands in this README should be executed from the repository's root directory (`Nba-Stats-CLI/`).

**1. Create the data directory**

```bash
mkdir -p data/
```

This directory will store the local SQLite database (`data/nba.db`).

The directory must be created manually because the database is not included in the Git repository. Each user creates and maintains their own local database.

**2. Initialize the database**

The application automatically creates the database tables when the first database connection is established.

The table definitions are stored in `sql/schema.sql`, which is executed by the `connect()` function.

There is no need to run the schema file manually.

For example, the first data-loading command will create the database and its tables:

```bash
nba_stats load teams
```

**3. Load reference data**

The `sql/reference_data.sql` file contains reference information for the 2024 and 2025 seasons, including the last regular-season game date and the NBA Cup Final game ID for each season.

This information is used to correctly filter regular-season games in SQL queries, since the API consider the play-in games and the In-Season Tournament Final as regular season games.

Run the following command after the database has been created:

```bash
sqlite3 data/nba.db < sql/reference_data.sql
```

The reference data can be loaded again without creating duplicate records.

## Loading NBA Data

Once the database is ready, NBA data can be loaded from the BALLDONTLIE API.

The application provides three loading commands: teams, games, and players.

**1. Load NBA teams**

```bash
nba_stats load teams
```

This command retrieves information about the 30 current NBA teams and stores it in the `teams` table.

This is the first loading command you should execute because the other tables reference team IDs.

**2. Load NBA games**

```bash
nba_stats load games --seasons 2024 2025
```

This command retrieves games from the selected NBA seasons and stores them in the `games` table.

The `--seasons` argument is required and accepts one or more season years.

For example, to load only the 2024 season:

```bash
nba_stats load games --seasons 2024
```

**3. Load NBA players**

```bash
nba_stats load players
```

This command retrieves player information, including names, positions, colleges, draft information, and team IDs.

The data is stored in the `players` table.

### Why Does the Loading Order Matter?

The database uses foreign keys to maintain relationships between tables.

Both `games` and `players` reference team IDs stored in the `teams` table.

For this reason, teams must be loaded first to avoid foreign key constraint errors.

The recommended order is:

1. Teams
2. Games
3. Players

### API Rate Limits and Loading Time

The BALLDONTLIE free API is limited to 5 requests per minute.

Because game and player data are returned in multiple pages, loading large datasets can take some time.

Approximate loading times:

| Data | Estimated Time | Explanation |
|------|----------------|-------------|
| Teams | A few seconds | Usually requires only one API request |
| Games | Approximately 5 minutes | Games are retrieved in pages of up to 100 records |
| Players | Several minutes (6197 players total) | Players are retrieved through multiple paginated requests |

These are rough estimates. Actual loading times depend on the number of records, API response times, rate limits, and retries.

The application handles temporary API errors and rate limits using retry logic.

### Running the Loading Commands Again

All three loading operations use SQLite's `ON CONFLICT DO UPDATE` functionality.

This means that running a loading command again will update existing records instead of creating duplicates.

You can safely reload the data when necessary.

## SQL Queries

After loading the database, you can explore NBA statistics through the CLI.

The project currently defines three query commands.

| Query | Description | Command |
|-------|-------------|---------|
| Team Rankings | Ranks teams by wins and shows their total points scored and allowed for each regular season | `nba_stats query wins_and_scoring` |
| Back-to-Back | Intended to analyze team performance in back-to-back games (work in progress) | `nba_stats query back-to-back` |
| College Lottery Picks | Lists the top 20 colleges with the most NBA lottery picks | `nba_stats query colleges_lottery_picks` |

### Example 1: Team Rankings

```bash
nba_stats query wins_and_scoring
```

This query shows the number of wins, total points scored, and total points allowed for each NBA team during the regular season.

It also ranks teams based on their number of wins.

The query uses reference dates to exclude postseason games and the NBA Cup Final.

### Example 2: College Lottery Picks

```bash
nba_stats query colleges_lottery_picks
```

This query ranks colleges based on the number of players selected in the first 14 picks of the NBA Draft.

It returns the 20 colleges with the highest number of lottery picks in the loaded player data.

### Example 3: Back-to-Back Analysis

```bash
nba_stats query back-to-back
```

This query is currently under development and does not yet produce the intended back-to-back analysis.

### Example Output

The CLI displays query results directly in the terminal.

For example, the college lottery picks query returns the following columns:

```text
college | lottery_picks | rank
```

Example output format (illustrative, not actual NBA results):

```text
('Example University A', 12, 1)
('Example University B', 10, 2)
('Example University C', 8, 3)
```

Actual results depend on the data loaded into the local database.

## Testing and Code Quality

The project uses `pytest`, `mypy`, and `ruff` to test the application and maintain code quality.

**1. Run automated tests**

```bash
pytest
```

The tests verify database operations, data loading, data transformations, and SQL query execution.

The test suite uses fake API clients and an in-memory SQLite database.

This means tests do not require network access or interact with the user's real database.

**2. Run static type checking**

```bash
mypy src tests
```

Mypy checks type annotations and helps identify potential type-related errors.

The project uses strict type checking.

**3. Run linting checks**

```bash
ruff check .
```

Ruff analyzes the code and identifies potential linting problems.