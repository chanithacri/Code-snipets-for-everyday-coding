/**
 * websocket_basic: WebSocket client/server stubs.
 * Include minimal usage example at bottom.
 */

export function createClient(WebSocketImpl, url, { onMessage, onOpen, onError } = {}) {
  const WS = WebSocketImpl || (typeof WebSocket !== "undefined" ? WebSocket : null);
  if (!WS) {
    throw new Error("Provide a WebSocket constructor");
  }
  const socket = new WS(url);
  if (onOpen) socket.addEventListener("open", onOpen);
  if (onMessage) socket.addEventListener("message", onMessage);
  if (onError) socket.addEventListener("error", onError);
  return socket;
}

/* Usage example:
import WebSocket from "ws";
createClient(WebSocket, "wss://echo.websocket.events", { onMessage: (ev) => console.log(ev.data) });
*/
