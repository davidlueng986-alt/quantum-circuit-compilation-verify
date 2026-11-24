# Quantum Circuit Compilation — Verification

Public GitHub Actions verification infrastructure for the Google Quantum AI Verifiable Quantum Circuit Compilation competition.

## Scope

- Reproduce official baseline scores and run unmodified official verifiers for `invsqrt`, `dqi`, and `dfthcsos`.
- Host verification workflow definitions and environment setup only.
- No research, circuit generation, parameter search, leaderboard submissions, or scheduled runs.

## Separation

The separate private `quantum-circuit-compilation-compute` repository is the research workspace. Do not commit competition datasets, reference circuits, candidate circuits, credentials, private research code, or unredacted logs to this public repository. Competition data must only be downloaded by authorized participants under the competition rules. Public Actions logs and artifacts are publicly accessible; never upload restricted inputs or outputs, and expose only explicitly approved summary information.

## Status

Repository initialized. Verification workflows and environment setup are not yet configured or tested.

Official sources: [Competition](https://www.kaggle.com/competitions/google-verifiable-quantum-circuit-compilation), [Rules](https://www.kaggle.com/competitions/google-verifiable-quantum-circuit-compilation/rules), [Qualtran/Kickmix](https://github.com/quantumlib/Qualtran/tree/main/kickmix).
