/**
 * random_ids: Generate random IDs and hex colors.
 * Include minimal usage example at bottom.
 */

export function randomId(length = 8) {
  const alphabet = "abcdefghijklmnopqrstuvwxyz0123456789";
  let result = "";
  for (let i = 0; i < length; i += 1) {
    const index = Math.floor(Math.random() * alphabet.length);
    result += alphabet[index];
  }
  return result;
}

export function randomHexColor() {
  const value = Math.floor(Math.random() * 0xffffff);
  return `#${value.toString(16).padStart(6, "0")}`;
}

/* Usage example:
const id = randomId();
const color = randomHexColor();
*/
