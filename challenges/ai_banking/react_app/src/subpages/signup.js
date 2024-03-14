import './signup.js';
import { useState, useEffect } from 'react';

function Signup() {

    const [email, setEmail] = useState('');
    const [password1, setPassword1] = useState('');
    const [password2, setPassword2] = useState('');
    const [errorMessage, setErrorMessage] = useState('');

    useEffect(() => {
        const cookies = document.cookie.split(';');
        for (const cookie of cookies) {
            const [name, value] = cookie.trim().split('=');
            if (name === 'session_token') {
                document.location.href = "/";
                break;
            }
        }
    }, []);

    const handleSuccess = () => {
        console.log('User Successfully created!');
        document.location.href = "/login";
    };

    const handleEmailChange = (e) => {
        setEmail(e.target.value);
    };

    const handlePasswordChange1 = (e) => {
        setPassword1(e.target.value);
    };

    const handlePasswordChange2 = (e) => {
        setPassword2(e.target.value);
    };

    const handleSubmit = async (e) => {
        e.preventDefault();

        const formData = {
            email: email,
            password: password1,
        };

        if (email == '' || password1 == '' || password2 == '') {
            setErrorMessage("Please provide email and password!")
            return
        } else if (password1 != password2) {
            setErrorMessage("Passwords must be the same!")
            return
        }

        try {
            const response = await fetch('/api/signup', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(formData),
                credentials: 'include',
            });

            if (response.ok) {
                handleSuccess();
            } 
        } catch (error) {
            console.error('Error occurred:', error);
        }
    };


    return(
        <>
        <div className='side_section'>
        <div className='spacer'></div>
            <form onSubmit={handleSubmit}>
                <h1>Email:</h1>
                <input className='input' type='email' value={email} onChange={handleEmailChange} placeholder='john.doe@tophack.at' />

                <h1>Password:</h1>
                <input className='input' type='password' value={password1} onChange={handlePasswordChange1} />

                <h1>Repeat Password:</h1>
                <input className='input' type='password' value={password2} onChange={handlePasswordChange2}/>

                <h1 className='errorMsg'>{ errorMessage }</h1>

                <button type='submit' className='submitter'>SignUP</button>
            </form>
        </div>
        </>
    )
}

export default Signup;