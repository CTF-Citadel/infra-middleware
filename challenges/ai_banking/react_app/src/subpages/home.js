import "./home.css";
import bank_1 from '../assets/bank_1.png';
import bank_2 from '../assets/bank_2.png';
import bank_3 from '../assets/bank_3.png';
import bank_4 from '../assets/bank_4.png';
import bank_7 from '../assets/bank_7.png';
import cyberspace_1 from '../assets/cyberspace_1.png';
import cyberspace_2 from '../assets/cyberspace_2.png';
import cyberspace_3 from '../assets/cyberspace_3.png';
import cyberspace_4 from '../assets/cyberspace_4.png';
import cyberspace_5 from '../assets/cyberspace_5.png';
import cyberspace_6 from '../assets/cyberspace_6.png';
import cyberspace_7 from '../assets/cyberspace_7.png';
import cyberspace_8 from '../assets/cyberspace_8.png';
import cyberspace_9 from '../assets/cyberspace_9.png';
import cyberspace_10 from '../assets/cyberspace_10.png';
import cyberspace_11 from '../assets/cyberspace_11.png';
import ImageSlider from '../components/slider.js';
import Glow from "../components/glow";

function Home() {

    const slides = [
      {url: cyberspace_1},
      {url: cyberspace_2},
      {url: cyberspace_3},
      {url: cyberspace_4},
      {url: cyberspace_5},
      {url: cyberspace_6},
      {url: cyberspace_7},
      {url: cyberspace_8},
      {url: cyberspace_9},
      {url: cyberspace_10},
      {url: cyberspace_11},
    ];
  
    const storedStyles = {
      width: '100%',
      height: '400px',
      margin: '0 auto',
    }

    return(
        <>
        <div className="wallpaper">
          <div style={storedStyles}>
            <ImageSlider slides={slides} />
          </div>
        </div>
        <br/><br/>
        <Glow />
        <div className="between"/>
        <div className="section">
            <div className="leftHalf">
                <div className="picture-container">
                    <img src={bank_1} alt="Bank Counter"/>
                </div>
            </div>
            <div className="rightHalf">
              <h1 className="sTitle" >Customer-Centric Approach:</h1>
              <p className="rndm_colors sText">At AI-Banking, our customers are the cornerstone of our existence and success. We have an unwavering commitment to providing you with an exceptional banking experience, tailor-made to suit your individual needs and preferences. Our customer-centric approach guides every aspect of our operations, ensuring that your satisfaction is at the forefront of everything we do. From personalized financial solutions to innovative services, we are dedicated to putting you first and delivering a seamless and rewarding journey through the world of modern banking.</p>
            </div>
        </div>

        <div className="between">
          <div className="line"/>
        </div>

        <div className="section">
          <div className="leftHalf">
            <h1 className="sTitle">Your Financial Success Matters:</h1>
            <p className="rndm_colors">We believe in the power of financial success for our customers and understand that your achievements are a reflection of our efforts. Our AI-powered tools and cutting-edge technology are not just tools; they are instruments designed to empower you on your financial journey. Whether you aspire to save for that dream vacation, plan for retirement, or invest wisely, our team of experts and state-of-the-art algorithms stand ready to provide you with valuable insights and recommendations. At AI-Banking, your financial success is not just a goal; it's our shared triumph.</p>
          </div>
          <div className="rightHalf">
            <div className="picture-container">
              <img src={bank_2} alt="Bank Counter"/>
            </div>
          </div>
        </div>

        <div className="between">
          <div className="line"/>
        </div>

        <div className="section">
          <div className="leftHalf">
            <div className="picture-container">
              <img src={bank_7} alt="Bank Counter"/>
            </div>
          </div>
          <div className="rightHalf">
          <h1 className="sTitle">Responsive Customer Support:</h1>
            <p className="rndm_colors">Time is valuable, and at AI-Banking, we don't take a second of yours for granted. That's why our dedicated support team is available around the clock, day and night, to cater to your needs and resolve any queries or concerns you may have. Our customer support representatives are highly trained and equipped with the knowledge and expertise to assist you promptly and efficiently. We pride ourselves on being responsive, empathetic, and always ready to go the extra mile to ensure your satisfaction. When you choose AI-Banking, you choose a partner who is committed to your peace of mind and convenience.</p>
          </div>
        </div>

        <div className="between">
          <div className="line"/>
        </div>

        <div className="section">
          <div className="leftHalf">
            <h1 className="sTitle">Security is Our Top Priority:</h1>
            <p className="rndm_colors">At AI-Banking, security is not just a feature; it's the foundation on which we build trust with our valued customers. We employ state-of-the-art AI-driven security measures that go beyond industry standards to safeguard your financial information and transactions. From advanced encryption protocols to multi-factor authentication, our security systems are designed to withstand any threat, ensuring your data remains confidential and protected from unauthorized access. With AI-Banking, you can have the confidence and peace of mind to focus on what truly matters – achieving your financial goals.</p>
          </div>
          <div className="rightHalf">
            <div className="picture-container">
                    <img src={bank_3} alt="Bank Counter"/>
                </div>
          </div>
        </div>

        <div className="between">
          <div className="line"/>
        </div>

        <div className="section">
          <div className="leftHalf">
            <div className="picture-container">
              <img src={bank_4} alt="Bank Counter"/>
            </div>
          </div>
          <div className="rightHalf">
          <h1 className="sTitle">Innovation for Your Convenience:</h1>
            <p className="rndm_colors">We live in a fast-paced world where convenience matters more than ever. At AI-Banking, we embrace innovation and leverage the power of AI technology to revolutionize your banking experience. Our user-friendly interfaces and smart tools simplify complex financial tasks, making banking effortless and accessible. From real-time transaction alerts to intelligent expense tracking, our AI-driven features are designed to enhance your financial decision-making and bring simplicity to your daily banking routines. With AI-Banking, you can embrace the future of banking today.</p>
          </div>
        </div>

        <div className="between"/>
        </>
    )
}
  
export default Home;