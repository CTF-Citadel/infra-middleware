import './rndm.css';

function FAQ() {
  
    return(
        <div className='side_section'>
            <h2 className='rndm_colors'>General Questions:</h2>
            <h3 className='rndm_colors'>Q: Is AI-Banking a real banking institution?<br/>A: No, AI-Banking is a fictitious web app created for demonstration purposes only. It does not represent a real banking institution.</h3>
            <br/>
            <h3 className='rndm_colors'>Q: Can I use AI-Banking for actual financial transactions?<br/>A: No, AI-Banking is a simulation and should not be used for actual financial transactions.</h3>
            <br/>
            <h2 className='rndm_colors'>Account Questions:</h2>
            <h3 className='rndm_colors'>Q: How do I create an account?<br/>A: To create an account, simply click on the "Sign Up" button and follow the instructions to provide the required information.</h3>
            <br/>
            <h3 className='rndm_colors'>Q: Can I have multiple accounts on AI-Banking?<br/>A: Yes, AI-Banking currently supports finite accounts per user.</h3>
            <br/>
            <h2 className='rndm_colors'>Security Questions:</h2>
            <h3 className='rndm_colors'>Q: How is my personal information protected?<br/>A: AI-Banking takes your privacy and security seriously. We implement various measures to protect your personal information and ensure secure data transmission.</h3>
            <h3 className='rndm_colors'>Q: What should I do if I suspect unauthorized access to my account?<br/>A: If you suspect unauthorized access to your account, please contact our support team immediately. We will investigate the issue and take appropriate actions to secure your account.</h3>
            <br/>
            <h2 className='rndm_colors'>Transaction Questions:</h2>
            <h3 className='rndm_colors'>Q: How long does it take for a transaction to be processed?<br/>A: Transaction processing times may vary depending on the nature of the transaction. Generally, transactions are processed within a few business days.</h3>
            <h3 className='rndm_colors'>Q: Are there any transaction limits on AI-Banking?<br/>A: AI-Banking may impose certain transaction limits for security and regulatory compliance reasons. Please refer to our terms of service for more information on transaction limits.</h3>
        </div>
    )
}
  
export default FAQ;