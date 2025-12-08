/**
 * nodemailer_send: Send email with Nodemailer.
 * Include minimal usage example at bottom.
 */

export async function sendMail({ nodemailerLib, transportConfig, message }) {
  if (!nodemailerLib) {
    throw new Error("Pass nodemailer as { nodemailerLib } to avoid a hard dependency here");
  }
  const nodemailer = nodemailerLib.default || nodemailerLib;
  const transporter = nodemailer.createTransport(transportConfig);
  return transporter.sendMail(message);
}

/* Usage example:
import nodemailer from "nodemailer";
import { sendMail } from "./nodemailer_send.js";

await sendMail({
  nodemailerLib: nodemailer,
  transportConfig: { sendmail: true },
  message: { from: "demo@example.com", to: "you@example.com", subject: "Hi", text: "Hello" },
});
*/
