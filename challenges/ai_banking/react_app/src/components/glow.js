import './slider.css';
import React, {useState, useEffect } from 'react';

const Glow = () => {

    const message = "AI-Banking Services";

    const letters = message.split("");

    const mainTitle = {
        fontSize: "60px",
        fontWeight: "900",
    }

    const [animation, setAnimation] = useState('');

    useEffect(() => {
        const interval = setInterval(() => {
            titleAnimation();
          }, 1000); 
      
          return () => clearInterval(interval);
    }, []);

    function titleAnimation() {
        // 
    }

    return (
        <div style={ mainTitle }>{ message }</div>
    )
}

export default Glow;