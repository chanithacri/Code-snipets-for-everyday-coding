/**
 * detect_browser: Detect browser/device basics.
 * Include minimal usage example at bottom.
 */

export function detect(uaString = (typeof navigator !== "undefined" ? navigator.userAgent : "")) {
  const ua = uaString.toLowerCase();
  return {
    isMobile: /iphone|android|ipad/.test(ua),
    isChrome: ua.includes("chrome") && !ua.includes("edge"),
    isFirefox: ua.includes("firefox"),
    isSafari: ua.includes("safari") && !ua.includes("chrome"),
  };
}

/* Usage example:
const info = detect("Mozilla/5.0 (Macintosh; Intel Mac OS X) AppleWebKit Safari/605.1.15");
console.log(info.isSafari);
*/
