export type AIDiscipline = 'ml' | 'dl' | 'rl' | 'symbolic_ai' | 'computer_vision' | 'nlp';

export interface AIJob {
  schema: 'CHIMERA-AI-JOB-1';
  discipline: AIDiscipline;
  task: string;
  dataKind: string;
  framework?: string;
  parameters?: Record<string, unknown>;
  provenance?: Record<string, unknown>;
}

export function validateAIJob(job: AIJob): AIJob {
  if (!job.task.trim() || !job.dataKind.trim()) throw new Error('task and dataKind are required');
  return job;
}
