import React, { useState } from "react";

const FileUploadPage = () => {
  const [file, setFile] = useState(null);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleUpload = (e) => {
    e.preventDefault();
    // TODO: Upload file to backend
    alert("File uploaded (placeholder)");
  };

  return (
    <div style={{ maxWidth: 400, margin: "auto", padding: 32 }}>
      <h2>Upload Book File</h2>
      <form onSubmit={handleUpload}>
        <input type="file" accept=".txt,.pdf" onChange={handleFileChange} />
        <button type="submit" disabled={!file}>Upload</button>
      </form>
    </div>
  );
};

export default FileUploadPage; 