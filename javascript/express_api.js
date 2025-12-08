/**
 * express_api: Express.js REST API skeleton.
 * Include minimal usage example at bottom.
 */

export function createApi(expressLib) {
  if (!expressLib) {
    throw new Error("Pass an express instance to avoid hard dependency in this repo");
  }
  const app = expressLib();
  app.use(expressLib.json());

  app.get("/health", (_req, res) => res.json({ status: "ok" }));
  app.post("/echo", (req, res) => res.json({ received: req.body }));

  return app;
}

/* Usage example:
import express from "express";
import { createApi } from "./express_api.js";

const app = createApi(express);
app.listen(3000, () => console.log("listening"));
*/
