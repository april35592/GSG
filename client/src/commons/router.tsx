import { createBrowserRouter } from "react-router-dom";

import Root from "@pages/root";
import Home from "@pages/Home";
import NotFound from "@pages/NotFound";

const router = createBrowserRouter([
  {
    path: "/",
    element: <Root />,
    errorElement: <NotFound />,
    children: [
      {
        path: "",
        element: <Home />,
      },
    ],
  },
]);

export default router;
