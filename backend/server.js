const express = require("express");
const cors = require("cors");

const app = express();
app.use(cors());

app.get("/", (req, res) => {
  res.send("AI Study Agent Server Running");
});

app.listen(5000, () => {
  console.log("AI Study Agent running on port 5000");
});