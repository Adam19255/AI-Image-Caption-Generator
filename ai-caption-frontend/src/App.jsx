import { useState } from "react";
import ImageUploader from "./components/ImageUploader";
import Controls from "./components/Controls";

export default function App() {
  const [temperature, setTemperature] = useState(1.0);

  return (
    <div className="app">
      <div className="hero">
        <h1>🧠 AI Image Caption Generator</h1>
        <p>Upload an image and let the AI describe it. Adjust the Creativity slider to control randomness.</p>
        <Controls className="controls" temperature={temperature} setTemperature={setTemperature} />
        <ImageUploader temperature={temperature} />
      </div>
    </div>
  );
}
