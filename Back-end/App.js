require("dotenv").config();

const express = require("express");
const mongoose = require("mongoose");
const bodyParser = require("body-parser");
const cors = require("cors");

const patientRoutes = require("./routes/patientRoutes");

const app = express();
app.use(cors());
app.use(bodyParser.json());

mongoose.connect(process.env.CONNECTION_STRING, {
    useNewUrlParser: true,
    useUnifiedTopology: true,
})
.then(() => console.log("Connected to DB"))
.catch(err => console.error("DB Connection Error:", err));

// Routes
app.use("/api", patientRoutes);

const PORT =5000;
app.listen(PORT, () => {
    console.log(`🚀 Server running on http://localhost:${PORT}`);
});
