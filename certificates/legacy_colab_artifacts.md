# Legacy Colab PB Artifacts

This directory contains historical Colab/RoundingSat artifacts from the
attempt to certify the five hard S6 obstruction cases by pseudo-Boolean
residual-clique instances.

## Current Interpretation

These files are useful as audit trail, but they are not paper-grade
certificates.

The saved solver runs confirm that the generated OPB instances can be read
and attacked by RoundingSat, but the relevant runs ended as timeout/UNKNOWN.
They should therefore be treated as negative exploration, not as proofs.

## Bundles

- `s6_pb_colab_bundle.zip`: original bundle with the expected `pb_instances/`
  layout.
- `s6_pb_colab_bundle_v2.zip` and `s6_pb_colab_bundle_v3.zip`: restart bundles
  where OPB files were placed at the archive root. This caused the Colab
  layout issue where `pb_instances` was missing.
- `s6_pb_colab_bundle_017_20260524.zip` and
  `s6_pb_colab_bundle_restart_20260524.zip`: targeted restart bundles for
  later 017/019 testing.

## Saved Result Folders

- `s6_pb_colab_results/`
- `s6_pb_colab_results 17/`

These contain logs from Colab runs. They are retained for reproducibility of
the failed PB-certificate attempt, but they do not close any case.

## Status of the Five Hard Cases

The five remaining non-paper-grade S6 obstruction cases are:

- `001`
- `013`
- `017`
- `019`
- `020`

Their current best interpretation is:

- exact-cover/packing side says they are non-tilers;
- residual-clique search finds defect-one maximum near-packings;
- low-dimensional ordered-triple marginals show integer holes;
- no compact human certificate has been extracted yet.

For the paper, these should be cited only as audit-level laboratory status data
unless a verifiable proof certificate is later added.
