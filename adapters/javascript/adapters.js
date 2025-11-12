// Framework-agnostic adapters for logging & config
export class NoopLogger {
  debug(){}
  info(){}
  warn(){}
  error(){}
}
export function envConfig(key, defaultValue=undefined) {
  if (typeof process !== 'undefined' && process.env && key in process.env) {
    return process.env[key];
  }
  return defaultValue;
}
