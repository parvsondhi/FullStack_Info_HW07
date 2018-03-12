# FullStack_Info_HW07
FullStack_Info_HW07 - Mega Lab

## Initial Setup

After initially cloning the repository you need to do the following steps.

### 1. Install Dependencies
To create a development environment and install a dependencies run the following commands.

```
pip install virtualenv
virtualenv --python=python3 .fswd
source .fswd/bin/activate
pip install -r requirements.txt
```

#### Activate Environment
You can alwyas activate the environment by running `source .fswd/bin/activate` and deactivate it by running `deactivate`.

#### Update Dependecies
To update the dependencies of the project, run `pip freeze > requirements.txt`.

### 2. Add dotenv file
A `.env` file stores environment variables which should not be pushed to the git repository.
Therefore you have to manually create it set it up.
From the root of the repository run

```
cp .env.example .env
```

Then open the `.env` file in a text editor of your choice and fill / modify the required variables.

### 3. Create/Update Database
To create or update the database schema run the following commands from within the python interactive shell (activate it by running `python`).

```
import app
app._create_database()
```

## How to contribute

1. Select an issue from the project board and assign it to yourself.
2. Move the issue from *To do* column to the *In progress column*.
3. Create a new feature branch named *Feature/<title of issue>* from the develop branch.
4. Implement the specific using the feature branch.
5. Once finished, use source tree to merge develop into your feature branch locally. Check whether everything works as expected.
6. Open a pull request to merge ther feature branch back to develop and wait for the code review to approve it.
6. Once approved merge the feature branch into develop.


