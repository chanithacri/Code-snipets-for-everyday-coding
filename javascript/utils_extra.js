// Deep clone/copy object utility
export function deepClone(obj) {
    if (typeof structuredClone === 'function') {
        return structuredClone(obj);
    }
    return JSON.parse(JSON.stringify(obj));
}

// Error boundary/wrapping utility
export function withErrorBoundary(fn, errorHandler = console.error) {
    return (...args) => {
        try {
            return fn(...args);
        } catch (err) {
            errorHandler(err);
            return null;
        }
    };
}

// LocalStorage/sessionStorage helpers
export const storageHelper = {
    set(storage, key, value) {
        try {
            storage.setItem(key, JSON.stringify(value));
        } catch (err) {
            console.error(err);
        }
    },
    get(storage, key) {
        try {
            const val = storage.getItem(key);
            return val ? JSON.parse(val) : null;
        } catch (err) {
            console.error(err);
            return null;
        }
    },
    remove(storage, key) {
        storage.removeItem(key);
    }
};

// Simple fetch/HTTP helper
export async function fetchHelper(url, options = {}) {
    try {
        const response = await fetch(url, options);
        if (!response.ok) throw new Error(`HTTP error ${response.status}`);
        return await response.json();
    } catch (err) {
        console.error(err);
        throw err;
    }
}

// Array/object utilities
export const arrayUtils = {
    deduplicate(arr) {
        return Array.from(new Set(arr));
    },
    chunk(arr, size) {
        const result = [];
        for (let i = 0; i < arr.length; i += size) {
            result.push(arr.slice(i, i + size));
        }
        return result;
    },
    groupBy(arr, keyFn) {
        return arr.reduce((acc, item) => {
            const key = keyFn(item);
            if (!acc[key]) acc[key] = [];
            acc[key].push(item);
            return acc;
        }, {});
    },
    merge(...arrays) {
        return [].concat(...arrays);
    }
};
