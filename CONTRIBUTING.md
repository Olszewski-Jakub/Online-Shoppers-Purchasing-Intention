# Contributing

## Commit messages

Follow [Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/).

```text
type(scope): description

Optional body explaining the reason for the change.

Optional footers, such as Refs: #123
```

The type and description are required; scope, body, and footers are optional.
Separate the body and footers with blank lines.

### Types

Use these types for this project:

| Type | Use for |
| --- | --- |
| `feat` | New functionality |
| `fix` | Bug fixes |
| `docs` | Documentation |
| `refactor` | Code restructuring without changing behavior |
| `perf` | Performance improvements |
| `test` | Tests |
| `build` | Dependencies and build configuration |
| `ci` | Continuous integration |
| `style` | Formatting without behavior changes |
| `chore` | Other maintenance |

### Project conventions

Use lowercase types, concise imperative descriptions (for example, "add" rather
than "added"), and no trailing period. Keep each commit focused on one change.
Choose an optional scope that identifies the affected area, such as `data`,
`model`, or `notebooks`.

```text
feat(model): add logistic regression baseline
fix(data): prevent leakage during preprocessing
docs: document dataset provenance
build(deps): update scikit-learn
chore: add Python gitignore
```

### Breaking changes

Mark incompatible changes with `!` immediately before the colon or an uppercase
`BREAKING CHANGE:` footer. Explain what consumers must change. Both markers may
be used together:

```text
feat(data)!: rename target column to purchased

BREAKING CHANGE: update notebooks to use purchased instead of Revenue.
```
