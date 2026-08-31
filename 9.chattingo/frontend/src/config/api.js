// Use same-origin by default; Caddy will proxy /auth and /api to backend
export const BASE_API_URL = process.env.REACT_APP_API_URL || "http://localhost:8080";
