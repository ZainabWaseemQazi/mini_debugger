interface Props {
  result: any;
}

export default function OutputPanel({ result }: Props) {
  if (!result) return null;

  return (
    <div className="bg-gray-900 text-white p-4 mt-4 rounded">
      <h2 className="text-lg font-bold">Final Code:</h2>
      <pre>{result.final_code}</pre>

      <p>Status: {result.status}</p>
      <p>Success: {result.success ? "Yes" : "No"}</p>
    </div>
  );
}