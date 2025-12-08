/**
 * clipboard_copy: Copy text to clipboard.
 * Include minimal usage example at bottom.
 */

export async function copyText(text, navigatorRef = typeof navigator !== "undefined" ? navigator : null) {
  if (navigatorRef?.clipboard?.writeText) {
    await navigatorRef.clipboard.writeText(text);
    return true;
  }
  throw new Error("Clipboard API not available in this environment");
}

/* Usage example:
await copyText("Hello clipboard");
*/
