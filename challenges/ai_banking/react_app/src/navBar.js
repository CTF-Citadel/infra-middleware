import "./navBar.css";
import React, { useState, useEffect } from 'react';

function NavBar() {

    const [slideNav, setSlideNav] = useState({ left: "100%" });
    let hasAlerted = false;

    const btnPress = () => {
        if (slideNav.left === "100%") {
            setSlideNav({
                left: "calc(100% - 200px)",
            });
        } else {
            setSlideNav({
                left: "100%",
            });
        }
    };

    function deleteAllCookies() {
        const cookies = document.cookie.split(';');
        for (const cookie of cookies) {
            const [name] = cookie.trim().split('=');
            document.cookie = name + "=; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/";
        }
        window.location.reload();
    }

    function handleScreenSizeChange(event) {
        if (event.matches) {
          if (hasAlerted === false) {
            setSlideNav({
              left: "100%",
            });
          }
          hasAlerted = true;
        } else if (!event.matches) {
          hasAlerted = false;
        }
    }

    useEffect(() => {
        const mediaQuery = window.matchMedia("(min-width: 851px)");
        handleScreenSizeChange(mediaQuery);
        mediaQuery.addEventListener("change", handleScreenSizeChange);
    
        return () => {
          mediaQuery.removeEventListener("change", handleScreenSizeChange);
        };
    }, []);

    return(
        <>
        <div className="navBar">
            <ul className="navList">
                <li className="centered">
                    <a href="/" className="home">AI-Banking</a>
                    <a href="/profile" className="profile" style={{ visibility: document.cookie.includes('session_token') ? "visible" : "hidden" }}>Profile</a>
                </li>
                <li style={{ marginTop: '110px', marginRight: '150px' }}>
                    <div className="loginBtnWrapper">
                        <a href="/login" className="loginBtn" style={{ visibility: document.cookie.includes('session_token') ? "hidden" : "visible" }}>Login</a>
                        <a href="/signup" className="loginBtn" style={{ visibility: document.cookie.includes('session_token') ? "hidden" : "visible" }}>Signup</a>
                    </div>
                    <button className="loginBtn logoutBtn" onClick={deleteAllCookies} style={{ visibility: document.cookie.includes('session_token') ? "visible" : "hidden", marginLeft: 'auto', marginRight: 'auto' }}>Logout</button>
                </li>
            </ul>
            <div className="burgerBtn" onClick={btnPress}>
                <div className="btnLine line1"></div>
                <div className="btnLine line2"></div>
                <div className="btnLine line3"></div>
            </div>
        </div>

        <div className="sliding-object" style={{ ...slideNav, }}>
            <li>
                <a href="/" className="link">Home</a>
            </li>
            <li>
                <a href="/login" className="link">Login</a>
            </li>
            <li>
                <a href="/signup" className="link">Signup</a>
            </li>
        </div>
        </>
    );    
}

export default NavBar;
