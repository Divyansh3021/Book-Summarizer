import React, { useState } from 'react';
import "../assets/navbar.css" // Import your CSS file

function Navbar() {
  const [menuOpen, setMenuOpen] = useState(false);

  const toggleNavbarMenu = () => {
    setMenuOpen(!menuOpen);
  };

  return (
    <nav className="navbar">
      <div className="navbar-logo">
        <img src="logo.png" alt="Logo" />
      </div>
      <div className={`navbar-menu ${menuOpen ? 'open' : ''}`}>
        <a href="#">Home</a>
        <a href="#">Bookmarks</a>
        <a href="#">Blog</a>
      </div>
      <div className="navbar-menu-toggle" onClick={toggleNavbarMenu}>
        <span></span>
        <span></span>
        <span></span>
      </div>
    </nav>
  );
}

export default Navbar;
