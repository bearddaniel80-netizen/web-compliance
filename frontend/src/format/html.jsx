import React from "react";
import ReactDOM from "react-dom/client";
import TestHtml from "../components/container/TestPageHtml";
import Navigation from "../components/menu/nav/Navigation";
import { navigationConfig } from "../navigation";

ReactDOM.createRoot(
  document.getElementById("nav")
).render(
  <React.StrictMode>
    <Navigation model={navigationConfig}/>
  </React.StrictMode>
);

ReactDOM.createRoot(
  document.getElementById("root")
).render(
  <React.StrictMode>
    <TestHtml mode="html"/>
  </React.StrictMode>
);