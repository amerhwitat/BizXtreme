# BizXtreme ISO-Tool integration

BizXtreme source can be processed by the ISO-Tool orchestration model. Long-running build/image operations use fail-forward isolation for independent jobs.

## Runtime errors

A compiler, assembler, scanner, or optional packaging job that throws a runtime/process error is logged, marked failed/skipped, and followed by the next independent job. The final report preserves the failure. Fatal safety, staging, authorization, or image-integrity conditions can still stop the pipeline.

## Application details

The ISO-Tool desktop front ends show a live details section with current stage, job messages, recoverable errors, status, and cumulative progress. The Python, WPF C#, and VC++ Win32 implementations follow the same behavior.

The canonical ISO-Tool implementation is maintained in `amerhwitat/nlp/ISO-Tool/`.
