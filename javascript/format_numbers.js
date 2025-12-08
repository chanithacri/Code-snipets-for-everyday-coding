/**
 * format_numbers: Format currency and numbers Intl API.
 * Include minimal usage example at bottom.
 */

export function formatCurrency(value, currency = "USD", locale = "en-US") {
  return new Intl.NumberFormat(locale, { style: "currency", currency }).format(value);
}

export function formatNumber(value, locale = "en-US", options = {}) {
  return new Intl.NumberFormat(locale, options).format(value);
}

/* Usage example:
formatCurrency(12.5, "EUR");
formatNumber(12345.678, "en-US", { maximumFractionDigits: 1 });
*/
