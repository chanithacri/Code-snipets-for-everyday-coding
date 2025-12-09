/**
 * event_emitter: Node EventEmitter sample.
 * Include minimal usage example at bottom.
 */

import { EventEmitter } from "events";

export function createCounterEmitter() {
  const emitter = new EventEmitter();
  let count = 0;

  const increment = () => {
    count += 1;
    emitter.emit("increment", count);
  };

  return { emitter, increment };
}

/* Usage example:
const { emitter, increment } = createCounterEmitter();
emitter.on("increment", (value) => console.log("count", value));
increment();
*/
