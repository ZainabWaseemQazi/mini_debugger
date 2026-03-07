import { useState } from "react";
import CodeEditor from "./components/CodeEditor";
import OutputPanel from "./components/OutputPanel";
import { reviewCode } from "./services/api";

function App() {
  const [code, setCode] = useState("print('Hello')");
  const [result, setResult] = useState<any>(null);

  const handleSubmit = async () => {
    const response = await reviewCode(code);
    setResult(response);
  };

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">AI Debugger</h1>

      <CodeEditor code={code} setCode={setCode} />

      <button
        onClick={handleSubmit}
        className="bg-blue-600 text-white px-4 py-2 mt-4 rounded"
      >
        Review & Debug
      </button>

      <OutputPanel result={result} />
    </div>
  );
}

export default App;