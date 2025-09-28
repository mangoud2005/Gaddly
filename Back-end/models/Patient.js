const mongoose = require("mongoose");

const patientSchema = new mongoose.Schema({
    name: { type: String, required: true },
    idNumber: { type: String, required: true },
    medicalNumber: { type: String, required: true },
    age: { type: Number, required: true },
    clinic: { type: String, required: true },
    diagnosis: { type: String, required: true },
    medicine: { type: String, required: true },
    regimen: { type: String, required: true },
    duration: { type: String, required: true },
    critical: {
        sixMonthsSinceDiagnosis: { type: Boolean, required: true },
        dosageChanged: { type: Boolean, required: true }
    },
    prescription: { type: String } // file path
    }, { timestamps: true });

module.exports = mongoose.model("Patient", patientSchema);
