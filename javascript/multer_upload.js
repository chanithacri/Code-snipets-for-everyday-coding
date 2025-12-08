/**
 * multer_upload: File uploads with Multer.
 * Include minimal usage example at bottom.
 */

export function createUploader({ multerLib, destination = "uploads/", limits = {} }) {
  if (!multerLib) {
    throw new Error("Pass the Multer module as { multerLib } to avoid runtime dependency issues.");
  }
  const multer = multerLib.default || multerLib;
  const upload = multer({ dest: destination, limits });
  return {
    single: (fieldName) => upload.single(fieldName),
    fields: (schema) => upload.fields(schema),
  };
}

/* Usage example:
import express from "express";
import multer from "multer";
import { createUploader } from "./multer_upload.js";

const app = express();
const uploader = createUploader({ multerLib: multer });
app.post("/upload", uploader.single("file"), (req, res) => res.json({ file: req.file }));
*/
