import { useState, useRef, useCallback } from "react";
import api from "../api/client";

export default function ImageUploader({ temperature = 1.0, onCaptionGenerated }) {
  const [image, setImage] = useState(null);
  const [preview, setPreview] = useState(null);
  const [caption, setCaption] = useState("");
  const [loading, setLoading] = useState(false);
  const [dragActive, setDragActive] = useState(false);

  const fileInputRef = useRef(null);

  // Trigger hidden file input
  const handleBrowseClick = () => fileInputRef.current.click();

  // When file is chosen (by click or drag)
  const handleFileSelect = (file) => {
    if (!file) return;
    setImage(file);
    setPreview(URL.createObjectURL(file));
  };

  // Handle file input change
  const handleFileChange = (e) => handleFileSelect(e.target.files[0]);

  // Drag-and-drop handlers
  const handleDragOver = (e) => {
    e.preventDefault();
    e.stopPropagation();
    setDragActive(true);
  };

  const handleDragLeave = (e) => {
    e.preventDefault();
    e.stopPropagation();
    setDragActive(false);
  };

  const handleDrop = (e) => {
    e.preventDefault();
    e.stopPropagation();
    setDragActive(false);
    const file = e.dataTransfer.files[0];
    handleFileSelect(file);
  };

  // Upload to backend
  const handleUpload = useCallback(async () => {
    if (!image) return;
    setLoading(true);
    const formData = new FormData();
    formData.append("file", image);

    try {
      const res = await api.post(`/caption/?temperature=${temperature}`, formData);
      const captionText = res.data.caption;
      setCaption(captionText);
      if (onCaptionGenerated) onCaptionGenerated(captionText);
    } catch (error) {
      console.error(error);
      setCaption("Error generating caption.");
    } finally {
      setLoading(false);
    }
  }, [image, temperature, onCaptionGenerated]);

  return (
    <div className="uploader">
      {/* Hidden file input */}
      <input type="file" accept="image/*" ref={fileInputRef} style={{ display: "none" }} onChange={handleFileChange} />

      {/* Upload box with drag-drop */}
      <div
        className={`upload-container ${dragActive ? "active" : ""}`}
        onClick={handleBrowseClick}
        onDragOver={handleDragOver}
        onDragLeave={handleDragLeave}
        onDrop={handleDrop}>
        <div className="left-side">
          <svg viewBox="0 0 24 24" width="64" height="64" fill="none" stroke="#fff">
            <path
              d="M17 19a4 4 0 0 0 0-8h-.02A5.5 5.5 0 0 0 6 10.5c0 .17.01.34.02.5A4 4 0 0 0 6.86 19"
              strokeWidth="2"
              strokeLinecap="round"
              strokeLinejoin="round"
            />
            <path d="M12 14v5m0 0l2-2m-2 2l-2-2" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" />
          </svg>
          <div className="details">
            <h4>{dragActive ? "Drop file here" : "Drag & drop file here"}</h4>
            <p>Limit 200MB • JPG, JPEG, PNG</p>
          </div>
        </div>
        <div className="right-side">
          <button type="button">Browse files</button>
        </div>
      </div>

      {/* Preview + caption */}
      {preview && <h3 className="preview-heading">Preview</h3>}
      {preview && <img src={preview} alt="preview" className="preview" />}
      <button className="generate-button" onClick={handleUpload} disabled={loading || !image}>
        {loading ? "✨ Generating..." : "✨ Generate Caption"}
      </button>
      {caption && (
        <p className="caption">
          <strong>Caption:</strong> {caption}
        </p>
      )}
    </div>
  );
}
