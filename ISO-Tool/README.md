# BizXtreme ISO-Tool integration

BizXtreme source can be processed by ISO-Tool from a local checkout or authorized remote repository.

## Entry points

- `analyze-source`
- `build-compiled-images`
- `import-boot-image`
- `build-iso`
- `validate-image`

## Boot/image import

The GUI can inspect `.iso`, `.img`, and `.bin` files and stage a bounded boot-sector region. Imported bytes are inert and are never executed automatically.

## Offline recovery

Local source operation requires no Internet connection. Remote acquisition can periodically monitor connectivity and retry network operations after the connection returns. Status and retry activity are shown in the live details panel.

## Runtime errors

Recoverable compiler, assembler, scanner, or optional packaging failures are isolated, logged, recorded as failed/skipped, and followed by the next independent job. Fatal safety, staging, authorization, or image-integrity conditions can still stop publication.

## Application details

The Python, WPF C#, and VC++ Win32 front ends expose a live operation-details section with stage, job, error/recovery, network state, status, and cumulative progress.

The canonical ISO-Tool implementation is maintained in `amerhwitat/nlp/ISO-Tool/`.
