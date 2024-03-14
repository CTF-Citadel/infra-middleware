import "./footer.css";
// import React, {useState, useEffect, useRef} from 'react';
import twitterIcon from './assets/twitter.png';
import facebookIcon from './assets/facebook.png';
import linkedinIcon from './assets/linkedin.png';

function Footer() {

    return(
        <div className="footer">
            <div className="fsection">
                <ul className="flist">
                    <li>
                        <p>Phone:<br/>000 8000 404 454</p>
                    </li>
                    <li>
                        <p>Email:<br/>info@ai-banking.at</p>
                    </li>
                    <li>
                        <p>Address:<br/>Schützenstraße 35, 42659 Solingen, Germany</p>
                    </li>
                </ul>
            </div>
            <div className="fsection">
                <ul className="flist">
                    <li>
                        <a href="/terms">Terms of Service</a>
                    </li>
                    <li>
                        <a href="/privacy">Privacy Policy</a>
                    </li>
                    <li>
                        <a href="/faq">FAQs</a>
                    </li>
                </ul>
            </div>
            <div className="fsection">
                <ul className="flist">
                    <li>
                        <a href="https://facebook.com/"><img class="icon" src={facebookIcon} alt="Facebook"/></a>
                    </li>
                    <li>
                        <a href="https://twitter.com/"><img class="icon" src={twitterIcon} alt="Twitter"/></a>
                    </li>
                    <li>
                        <a href="https://linkedin.com/"><img class="icon" src={linkedinIcon} alt="LinkedIn"/></a>
                    </li>
                </ul>
            </div>
            <div className="fsection">
            <ul className="flist">
                    <li>
                        <a href="/careers">Careers</a>
                    </li>
                    <li>
                        <a href="/press">Press Room</a>
                    </li>
                    <li>
                        <a href="/investor">Investor Relations</a>
                    </li>
                    <li>
                        <br/><br/><br/><br/><br/>
                        <p>© 2023 AI-Banking</p>
                    </li>
                </ul>
            </div>
        </div>
    );    
}

export default Footer;