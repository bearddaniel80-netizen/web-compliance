import React from "react";
import ReactDOM from "react-dom/client";
import CarouselMenu from "./components/menu/Carousel";

ReactDOM.createRoot(
  document.getElementById("root")
).render(
  <React.StrictMode>
      <CarouselMenu mode="profile"/>
  </React.StrictMode>
);