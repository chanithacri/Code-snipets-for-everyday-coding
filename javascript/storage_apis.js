/**
 * storage_apis: localStorage/sessionStorage helpers.
 * Include minimal usage example at bottom.
 */

export function setValue(storage, key, value) {
  storage.setItem(key, JSON.stringify(value));
}

export function getValue(storage, key, defaultValue = null) {
  const raw = storage.getItem(key);
  if (raw === null || raw === undefined) return defaultValue;
  try {
    return JSON.parse(raw);
  } catch {
    return defaultValue;
  }
}

export function removeValue(storage, key) {
  storage.removeItem(key);
}

/* Usage example:
const memoryStore = new Map();
const adapter = {
  setItem: (k, v) => memoryStore.set(k, v),
  getItem: (k) => memoryStore.get(k) ?? null,
  removeItem: (k) => memoryStore.delete(k),
};

setValue(adapter, "theme", "dark");
const theme = getValue(adapter, "theme");
*/
