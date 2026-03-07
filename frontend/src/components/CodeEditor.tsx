import Editor from "@monaco-editor/react";

interface Props {
  code: string;
  setCode: (value: string) => void;
}

export default function CodeEditor({ code, setCode }: Props) {
  return (
    <Editor
      height="70vh"
      defaultLanguage="python"
      value={code}
      onChange={(value) => setCode(value || "")}
      theme="vs-dark"
    />
  );
}