export default function Controls({ temperature, setTemperature }) {
  return (
    <div className="controls">
      <label>Creativity (temperature): {temperature}</label>
      <input
        type="range"
        min="0.1"
        max="2.0"
        step="0.1"
        value={temperature}
        onChange={(e) => setTemperature(e.target.value)}
      />
    </div>
  );
}
