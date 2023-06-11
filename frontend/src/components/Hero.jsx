import React from 'react'
import "../CSS/hero.css"

function Hero() {
  return (
    <div id='hero'>
        <div className="text-content">
            <h1 id="tagline">
                TO SUCCEED YOU MUST READ
            </h1>
            <h3 id="sub-tagline">
                Don't have time to read, read summaries or even listen to them
            </h3>
        </div>

        <div className="hero-books">
            <div className="hero-book book-1"><img src={"https://m.media-amazon.com/images/I/51-nXsSRfZL.jpg"} alt="" /></div>
            <div className="hero-book book-2"><img src={"https://m.media-amazon.com/images/I/51-nXsSRfZL.jpg"} alt="" /></div>
            <div className="hero-book book-3"><img src={"https://m.media-amazon.com/images/I/51-nXsSRfZL.jpg"} alt="" /></div>
            <div className="hero-book book-3"><img src={"https://m.media-amazon.com/images/I/51-nXsSRfZL.jpg"} alt="" /></div>
            <div className="hero-book book-3"><img src={"https://m.media-amazon.com/images/I/51-nXsSRfZL.jpg"} alt="" /></div>
            <div className="hero-book book-3"><img src={"https://m.media-amazon.com/images/I/51-nXsSRfZL.jpg"} alt="" /></div>
        </div>
    </div>
  )
}

export default Hero