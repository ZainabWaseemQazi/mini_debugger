import axios from "axios";

const API = axios.create({
  baseURL: "http://localhost:8000",
});

export const reviewCode = async (code: string) => {
  const response = await API.post("/review_debug", { code });
  return response.data;
};