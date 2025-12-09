/**
 * dotenv_usage: dotenv setup for env vars.
 * Include minimal usage example at bottom.
 */

import fs from "fs";

export function loadEnv(path = ".env") {
  if (!fs.existsSync(path)) {
    return {};
  }
  const content = fs.readFileSync(path, "utf8");
  const env = {};
  for (const line of content.split(/\r?\n/)) {
    if (!line || line.startsWith("#")) continue;
    const [key, ...rest] = line.split("=");
    env[key.trim()] = rest.join("=").trim();
  }
  Object.assign(process.env, env);
  return env;
}

/* Usage example:
// .env
// API_KEY=secret

loadEnv();
console.log(process.env.API_KEY);
*/
