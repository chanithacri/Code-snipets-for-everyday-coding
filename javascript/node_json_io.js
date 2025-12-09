/**
 * node_json_io: Read/write JSON in Node.
 * Include minimal usage example at bottom.
 */

import fs from "fs/promises";

export async function readJson(path) {
  const content = await fs.readFile(path, "utf8");
  return JSON.parse(content);
}

export async function writeJson(path, value, pretty = true) {
  const spacing = pretty ? 2 : 0;
  const payload = JSON.stringify(value, null, spacing);
  await fs.writeFile(path, payload, "utf8");
  return path;
}

/* Usage example:
await writeJson("config.json", { feature: true });
const config = await readJson("config.json");
*/
