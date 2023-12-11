import { RouterProvider } from "react-router-dom";
import GlobalStyle from "@commons/GlobalStyle";
import router from "@commons/router";

function App() {
  return (
    <>
      <GlobalStyle />
      <RouterProvider router={router} />
    </>
  );
}

export default App;
