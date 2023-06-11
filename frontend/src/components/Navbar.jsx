import React from 'react'
import "../CSS/navbar.css"

function Navbar() {
  return (
    <div id='navbar'>
        <div id="logo"><img src={require("../assets/logo.png")} alt="" /></div>
        <div id="contract"><img src={require("../assets/menu-collapse.png")} alt="" /></div>
    </div>
  )
}

export default Navbar