import React from "react";
export default function LinkedUrl({ setURL }) {
  const handleURLChange = (event) => {
    setURL(event.target.value);
  };
  return (
    <div className="container">
      <form>
        <div className="textTitle">URL Submit</div>
        <div className="container">
          <input
            placeholder="https://linkedin.com"
            type="url"
            name="linkedinUrl"
            className="textbox textbox1"
            onChange={handleURLChange}
          ></input>
        </div>
      </form>
    </div>
  );
}
