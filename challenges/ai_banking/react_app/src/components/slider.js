import './slider.css';
import React, {useState, useEffect } from 'react';

const ImageSlider = ({ slides }) => {

    const [currentIndex, setCurrentIndex] = useState(0);

    const sliderStyles = {
        height: '100%',
        position: 'relative',
    }

    const slideStyles = {
        width: '100%',
        height: '100%',
        backgroundPosition: 'center',
        backgroundSize: 'cover',
        backgroundImage: `url(${slides[currentIndex].url })`,
        opacity: 'fadeOpacity', 
        transition: 'opacity 0.3s ease-in-out'
    }

    useEffect(() => {
        const interval = setInterval(() => {
            slidingTimer();
            changeInfo();
          }, 10000); 
      
          return () => clearInterval(interval);
    }, [currentIndex]);

    function slidingTimer() {
        let isLastSlide, newIndex;

        if (currentIndex === (slides.length - 1)) {
            isLastSlide = true;
        } else {
            isLastSlide = false;
        }

        if (isLastSlide === true) {
            newIndex = 0;
        } else {
            newIndex = currentIndex + 1;
        }
        setCurrentIndex(newIndex);
    }

    const [currentTitleIndex, setCurrentTitleIndex] = useState(0);

    const titles = [
        {title: 'Introducing AI-Banking: Your Smart Financial Partner', text: 'Experience a new era of banking with AI-Banking. Our intelligent system is designed to empower you, making banking smarter, faster, and more convenient than ever before.'},
        {title: 'Secure and Seamless Transactions', text: 'Rest assured knowing that your transactions are protected by state-of-the-art AI security measures. Enjoy seamless, frictionless payments and transfers with AI-Banking.'},
        {title: 'AI-Powered Insights for Financial Success', text: 'Unlock valuable insights into your finances with AI-Banking. Our advanced algorithms analyze your spending habits and offer personalized recommendations for financial success.'},
        {title: '24/7 Virtual Assistance', text: 'Say hello to our round-the-clock virtual assistant. From balance inquiries to investment advice, AI-Banking is here to assist you anytime, anywhere.'},
        {title: 'AI-Driven Investment Opportunities', text: 'Discover a world of intelligent investment opportunities with AI-Banking. Let our algorithms guide you towards profitable investments and help you achieve your financial goals.'},
    ]

    function changeInfo() {
        let rndmIndex;

        do {
            rndmIndex = Math.floor(Math.random() * titles.length);
        } while (rndmIndex === currentTitleIndex);

        setCurrentTitleIndex(rndmIndex);
    }

    return (
        <div style={ sliderStyles }>
            <div style={ slideStyles }>
                <div className='wallpaper'>
                    <h1 className='slideTitle'>{titles[currentTitleIndex].title}</h1>
                    <p className='slideText'>{titles[currentTitleIndex].text}</p>
                </div>
            </div>
        </div>
    )
}

export default ImageSlider;