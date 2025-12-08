/**
 * modules: ES modules import/export skeletons.
 * Include minimal usage example at bottom.
 */

export const PI = 3.14159;

export function add(a, b) {
  return a + b;
}

export function greet(name) {
  return `Hello, ${name}!`;
}

const defaultHelper = {
  square: (n) => n * n,
  cube: (n) => n * n * n,
};

export default defaultHelper;

/* Usage example:
import mathHelpers, { add, PI } from "./modules.js";
add(1, 2); // 3
mathHelpers.square(3); // 9
*/
