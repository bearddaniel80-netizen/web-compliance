import React from "react";
import ReactDOM from "react-dom/client";
import TestDashboard from "./components/container/TestPage";

ReactDOM.createRoot(
  document.getElementById("root")
).render(
  <React.StrictMode>
    <TestDashboard mode="default"/>
  </React.StrictMode>
);