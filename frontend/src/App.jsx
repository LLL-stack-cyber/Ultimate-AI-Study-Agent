import { useState } from "react";

export default function App() {
  const [syllabus, setSyllabus] = useState(null);
  const [papers, setPapers] = useState([]);

  return (
    <div style={{fontFamily:"Arial",padding:"40px"}}>
      <h1>🧠 Ultimate AI Study Agent</h1>
      <p>Your personal AI exam planner</p>

      <hr/>

      <h2>Upload Syllabus</h2>
      <input
        type="file"
        accept=".pdf"
        onChange={(e)=>setSyllabus(e.target.files[0])}
      />

      {syllabus && (
        <p>Uploaded: {syllabus.name}</p>
      )}

      <hr/>

      <h2>Upload Previous Question Papers</h2>

      <input
        type="file"
        accept=".pdf"
        multiple
        onChange={(e)=>setPapers([...e.target.files])}
      />

      {papers.length>0 && (
        <div>
          <h3>Uploaded Papers</h3>
          {papers.map((p,i)=>(
            <p key={i}>{p.name}</p>
          ))}
        </div>
      )}

      <hr/>

      <button
        style={{
          padding:"15px",
          fontSize:"16px",
          background:"#007bff",
          color:"white",
          border:"none",
          borderRadius:"6px"
        }}
      >
        Generate Study Plan
      </button>

      <button
        style={{
          padding:"15px",
          marginLeft:"10px",
          fontSize:"16px",
          background:"#28a745",
          color:"white",
          border:"none",
          borderRadius:"6px"
        }}
      >
        Generate Question Paper
      </button>
    </div>
  );
}