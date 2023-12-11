import { css } from "@emotion/css";

const setScreenSize = () => {
  let vh = window.innerHeight * 0.01;
  let vw = window.innerWidth * 0.01;
  document.documentElement.style.setProperty("--vh", `${vh}px`);
  document.documentElement.style.setProperty("--vw", `${vw}px`);
  console.log("hi");
};
setScreenSize();
addEventListener("resize", setScreenSize);

const GlobalStyle = css`
  :root {
    --white: #ffffff;
    --black: #000000;
  }

  * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
    border: 0;
    background: unset;
    color: inherit;
    font-family: inherit;
    font-size: inherit;
    font-weight: inherit;
    vertical-align: middle;
    text-decoration-line: none;
  }

  body {
    font-size: var(--fs-base);
  }

  #root {
    width: 100vw;
    height: 100vh;
    position: relative;
    display: flex;
    flex-direction: column;
    justify-content: center;
  }
`;

export default GlobalStyle;
