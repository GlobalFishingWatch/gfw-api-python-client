# Git Workflow

This document outlines the Git branching strategy, naming conventions, and development workflow used in the [gfw-api-python-client](https://github.com/GlobalFishingWatch/gfw-api-python-client).

We follow the **[GitFlow workflow](https://nvie.com/posts/a-successful-git-branching-model/)**, which provides a robust and structured approach to managing:

- Feature development
- Bug fixes
- Releases
- Hotfixes

## Branching Strategy

We utilize the **GitFlow** model, which involves the following primary branches:

| Branch         | Purpose                                                              |
|----------------|----------------------------------------------------------------------|
| `main`         | Represents the production-ready state; all releases originate here. |
| `develop`      | The integration branch for ongoing development; features are merged here. |
| `feature/*`    | Branches for developing new features, branched off from `develop`.      |
| `release/*`    | Branches for preparing a new production release, branched off from `develop`. |
| `hotfix/*`     | Branches for critical fixes to the production version, branched off from `main`. |

## Naming Conventions

Branch names should be lowercase and use hyphens to separate words for better readability:

- `feature/vessels-api-endpoints`
- `release/3.0.0`
- `hotfix/fix-vessels-search-params`

Be descriptive and concise when naming your branches.

## Workflow for Feature Development

1.  **Start from `develop`:**

    Ensure your local `develop` branch is up-to-date:

    ```bash
    git checkout develop
    git pull origin develop
    git checkout -b feature/your-feature-name
    ```

    Replace `your-feature-name` with a descriptive name for your feature.

2.  **Work Locally:**

    Develop your feature, committing changes regularly.

3.  **Commit Regularly with Conventional Commits:**

    Use [Conventional Commits](https://www.conventionalcommits.org/) for clear and automated changelogs:

    ```bash
    cz commit
    ```

    Ensure your commit messages accurately reflect the changes.

4.  **Run Local Checks Before Pushing:**

    Verify code style, run linters, and execute tests:

    ```bash
    make format
    make pre-commit
    make test
    ```

    Fix any issues identified by these checks.

5.  **Push Your Branch:**

    Push your local feature branch to the remote repository:

    ```bash
    git push origin feature/your-feature-name
    ```

6.  **Open a Pull Request (PR):**

    -   Target the `develop` branch.
    -   Adhere to the guidelines in [CONTRIBUTING.md](https://github.com/GlobalFishingWatch/gfw-api-python-client/blob/develop/CONTRIBUTING.md).
    -   Provide a clear title and description explaining the purpose and changes of your PR.
    -   Ensure all commits in the PR follow the [Conventional Commits](https://www.conventionalcommits.org/) format (using `cz commit` is recommended).

## Workflow for Releases

1.  **Create a Release Branch:**

    When `develop` is in a stable state for release:

    ```bash
    git checkout develop
    git pull origin develop
    git checkout -b release/your-release-version
    ```

    Replace `your-release-version` with the intended release version (e.g., `3.0.0`).

2.  **Finalize Release Preparations:**

    Perform tasks like updating documentation, finalizing the changelog, running thorough testing, and committing these final release-related changes.

3.  **Bump Version with Commitizen:**

    Use Commitizen to automatically bump the version and create a version commit:

    ```bash
    cz bump --yes
    ```

4.  **Merge into `main` and Tag the Release:**

    ```bash
    git checkout main
    git merge --no-ff release/your-release-version
    git tag -a vyour-release-version -m "Release vyour-release-version"
    git push origin main --tags
    ```

    Replace `your-release-version` in the `tag` command (e.g., `v3.0.0`). Adding a message (`-m`) to the tag is good practice. Pushing tags explicitly is important.

5.  **Merge Back into `develop`:**

    ```bash
    git checkout develop
    git merge --no-ff release/your-release-version
    git push origin develop
    ```

6.  **Clean Up:**

    Consider deleting the release branch after merging.

## Workflow for Hotfixes

1.  **Checkout and Create a Hotfix Branch from `main`:**

    When a critical issue needs immediate attention on the production branch:

    ```bash
    git checkout main
    git pull origin main
    git checkout -b hotfix/your-hotfix-name
    ```

    Replace `your-hotfix-name` with a descriptive name for the fix.

2.  **Fix, Test, and Commit Changes:**

    Implement the necessary fixes and commit them using a [Conventional Commit](https://www.conventionalcommits.org/) message with the `fix` type:

    ```bash
    cz commit
    # or
    git commit -m "fix(your-affected-area): address critical issue"
    ```

3.  **Merge into `main` and Tag the Hotfix Release:**

    ```bash
    git checkout main
    git merge --no-ff hotfix/your-hotfix-name
    git tag -a vyour-hotfix-version -m "Hotfix vyour-hotfix-version"
    git push origin main --tags
    ```

    Increment the patch version for hotfixes (e.g., `v3.0.1`).

4.  **Merge Back into `develop`:**

    Ensure the hotfix is also included in the ongoing development branch:

    ```bash
    git checkout develop
    git merge --no-ff hotfix/your-hotfix-name
    git push origin develop
    ```

5.  **Clean Up:**

    Consider deleting the hotfix branch after merging.

## Pull Request Checklist

When submitting a pull request, please ensure it meets the following criteria:

-   [ ] The PR targets the correct base branch (`develop` for features, `main` for hotfixes targeting a specific release).
-   [ ] The title and body provide a clear and concise explanation of **what** the PR does and **why** it's necessary.
-   [ ] All commits follow the [Conventional Commits](https://www.conventionalcommits.org/) specification.
-   [ ] All relevant checks pass locally (`make format`, `make pre-commit`, `make test`, etc.).
-   [ ] Documentation has been updated or created if the PR introduces new features or changes existing behavior.
-   [ ] Tests have been added for new features or bug fixes to ensure they function correctly and prevent regressions.

## Merge vs Rebase

-   **Merge:** Use `git merge --no-ff` to integrate feature, release, and hotfix branches. The `--no-ff` flag ensures that a merge commit is always created, preserving the history of the feature branch. This makes it easier to track when and why a set of changes was merged.
-   **Rebase:** Use `git rebase` **locally** on your feature branches to clean up your commit history before opening a pull request. This can make the PR history cleaner and easier to review. **Do not** rebase branches that have already been pushed to the remote repository and are being collaborated on.
-   **Force Push:** Avoid force-pushing to shared branches (`main`, `develop`, `release`, `hotfix` branches) unless explicitly coordinated with the team and you understand the implications. Force-pushing can rewrite history and cause issues for other collaborators.

By following this Git workflow, we can maintain a clear, organized, and collaborative development process for the `gfw-api-python-client`.
