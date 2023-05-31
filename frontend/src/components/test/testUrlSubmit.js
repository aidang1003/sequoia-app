import React from "react";
export default function LinkedinUrl() {
  return (
    <div className="container">
      <form action="https://localhost:5000/test" method="POST">
        <div className="textTitle">URL Submit</div>
        <div className="container">
          <input
            placeholder="Enter a linkedin url here"
            type="url"
            name="testlinkedinUrl"
            className="textbox textbox1"
          ></input>
          <button type="submit">Enter</button>
        </div>
      </form>
    </div>
  );
}
