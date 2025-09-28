const express = require("express");
const multer = require("multer");
const path = require("path");
const Patient = require("../models/Patient");

const router = express.Router();

// Multer config
const storage = multer.diskStorage({
  destination: (req, file, cb) => cb(null, "uploads/"),
  filename: (req, file, cb) =>
    cb(null, Date.now() + path.extname(file.originalname)),
});
const upload = multer({ storage });

// Create patient
router.post("/patients", upload.single("prescription"), async (req, res) => {
  try {
    // Debug logs
    console.log("📥 Incoming form data:", req.body);
    console.log("📂 Uploaded file:", req.file);

    const patient = new Patient({
      name: req.body.name,
      idNumber: req.body.idNumber,
      medicalNumber: req.body.medicalNumber,
      age: req.body.age,
      clinic: req.body.clinic,
      diagnosis: req.body.diagnosis,
      medicine: req.body.medicine,
      regimen: req.body.regimen,
      duration: req.body.duration,
      critical: {
        sixMonthsSinceDiagnosis: req.body.sixMonthsSinceDiagnosis === "true",
        dosageChanged: req.body.dosageChanged === "true",
      },
      prescription: req.file ? req.file.path : null,
    });

    await patient.save();
    res.status(201).json({ message: "Patient saved", patient });
  } catch (err) {
    console.error("❌ Error saving patient:", err);
    res
      .status(500)
      .json({ message: "Error saving patient", error: err.message });
  }
});

module.exports = router;
