/**
 * node_fs: Node.js file read/write.
 * Include minimal usage example at bottom.
 */

import fs from "fs/promises";

export async function writeText(path, content) {
  await fs.writeFile(path, content, "utf8");
  return path;
}

export async function readText(path) {
  return fs.readFile(path, "utf8");
}

export async function appendLine(path, line) {
  await fs.appendFile(path, `${line}\n`, "utf8");
}

/* Usage example:
await writeText("demo.txt", "Hello");
await appendLine("demo.txt", "World");
const text = await readText("demo.txt");
*/
