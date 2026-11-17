# Receipts — Spec v0.1

*Stream Presence. Signed action receipts + binding approval objects for
AI agents. Experiment: 14-day public dogfood from 2026-11-17.*

Design law: boring, standard, implementable in days. No chain, no
token, no new cryptography. JSON + Ed25519 + SHA-256 + HTTPS.

## Signature & encoding

- **Scheme:** Ed25519 (RFC 8032). Identities are `did:key` (multicodec
  `0xed 0x01` + raw public key, base58btc) — the same identity form
  Civis uses, so a receipt issuer can later bind 1:1 to a wallet
  identity with no format change.
- **Canonicalization:** JCS (RFC 8785) canonical JSON of the object
  excluding its `signature` field; the signature is over the canonical
  bytes directly. Signed payloads contain only strings, integers,
  booleans, null, arrays, objects (floats are rejected — canonical
  float forms are where implementations diverge).
- **Encoding:** plain JSON; signatures base64url.

## Receipt (proof of action)

```json
{
  "receipt_version": "0.1",
  "receipt_id": "rcpt_<uuid>",
  "issuer": "did:key:z6Mk…",
  "issuer_label": "scout",
  "action": {
    "type": "scout.card_filed",
    "args_hash": "sha256:<hex of JCS-canonical exact arguments>",
    "args_public": { "…": "present ONLY when the action is already public" },
    "result_hash": "sha256:<hex or null>",
    "artifact_url": "https://… (where a third party can fetch the thing)",
    "occurred_at": "… (when the action happened, if before issuance)"
  },
  "approval": { "approval_id": "appr_<uuid>",
                "approval_target_hash": "sha256:<hex>" },
  "issued_at": "2026-11-17T20:00:00Z",
  "prev_receipt_hash": "sha256:<hex>",
  "signature": "base64url"
}
```

- `args_hash` is always present: an approval-holder can prove their
  copy of the args matches. Literal args are published only when the
  action is already public; otherwise verification is by hash
  disclosure (the counterparty reveals the args, anyone checks the
  hash).
- `result_hash` + `artifact_url` bind the *output* of the action, not
  just a claim that it happened.
- `prev_receipt_hash` chains each issuer's receipts; the whole log is
  additionally hash-chained (below), so deletion or reordering is
  detectable.

## Approval (binding, expiring, revocable)

```json
{
  "approval_version": "0.1",
  "approval_id": "appr_<uuid>",
  "approver": "did:key:z6Mk…",
  "subject": "did:key:z6Mk… (the agent allowed to act)",
  "scope": { "action_type": "experiment.build",
             "constraints": { "machine-checkable": "predicates only" } },
  "object_fingerprint": "sha256:<hex of JCS(scope + target_hash)>",
  "target": { "description": "the exact thing approved",
              "target_hash": "sha256:<hex>" },
  "issued_at": "…", "expires_at": null,
  "expiry_conditions": ["time", "target_changed", "superseded", "revoked"],
  "status": "active",
  "signature": "base64url"
}
```

Three rules, mechanically checked by the verifier:

1. **Exact-args binding** — a receipt under an approval must match the
   approval's scope predicates (action type + constraints).
2. **Expiry-on-change** — the approval carries the target's hash. A
   receipt records the target hash it observed at action time; if the
   thing changed, the hashes differ and the approval is *mechanically*
   expired — no human has to notice.
3. **Revocation = negative receipt** — revoking appends a signed
   revocation object to the same log. The log proves a negative ("this
   approval was dead at time T") instead of an absence proving nothing.

## The log

One append-only JSONL file. Each line is a chain entry
`{seq, ts, prev_hash, entry_hash, kind, object}` with
`entry_hash = SHA-256(prev_hash + JCS(entry minus entry_hash))`
(the Civis ledger pattern). Signed checkpoints over the chain head are
committed to this public git repo — once a checkpoint is in git
history, we cannot silently rewrite our own fleet's receipts either.

## Endpoints

- `POST /v1/receipts` — accepts a fully signed receipt / approval /
  revocation object; the server re-validates registration, signature,
  and chain head before appending. **v1 issuance is fleet-only** —
  unregistered issuers are rejected. (Self-issuance by our fleet goes
  through the same validated append path as the endpoint; there is no
  back door.)
- `GET /v1/verify/{receipt_id}` — public, free forever, no account.
  This page performs the identical recompute in your browser.

## A verification asserts — and does not assert

A VALID verdict asserts: the object is in the log at its chain
position; the signature verifies against the issuer's did:key; the
per-issuer chain is unbroken; and, when bound, the approval existed,
was signed by its approver, covers this issuer and action type, was
not revoked or time-expired, and its target fingerprint matches what
the receipt observed.

It does **not** assert: that the action was wise or safe; that it was
authorized by anyone other than the named approver; that `args_public`
is complete where absent; that the artifact still exists unchanged
beyond its `result_hash`; or any real-world identity behind a did:key
beyond its registry entry.

## Monetization hooks (present, charged at $0)

Issuer registry (the future subscription object), published per-issuer
issuance counts (metering before pricing), and a signed audit-pack
export (receipts + approvals + revocations + checkpoints + a manifest
of what the pack does and does not assert). Verification stays free —
structurally, in writing.
