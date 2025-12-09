/**
 * debounce_throttle: Debounce and throttle utilities.
 * Include minimal usage example at bottom.
 */

export function debounce(fn, delayMs = 100) {
  let timer;
  return (...args) => {
    clearTimeout(timer);
    timer = setTimeout(() => fn(...args), delayMs);
  };
}

export function throttle(fn, intervalMs = 100) {
  let lastCall = 0;
  let timeout;
  return (...args) => {
    const now = Date.now();
    const remaining = intervalMs - (now - lastCall);
    if (remaining <= 0) {
      lastCall = now;
      fn(...args);
    } else if (!timeout) {
      timeout = setTimeout(() => {
        lastCall = Date.now();
        timeout = null;
        fn(...args);
      }, remaining);
    }
  };
}

/* Usage example:
const log = debounce((v) => console.log("debounced", v), 200);
const throttled = throttle(() => console.log("tick"), 500);
*/
