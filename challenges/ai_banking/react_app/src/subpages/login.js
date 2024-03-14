import './login.css';
import { useState, useEffect } from 'react';

function Login() {

    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
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
        console.log('Login successful!');
        const cookies = document.cookie.split(';');
        for (const cookie of cookies) {
            const [name, value] = cookie.trim().split('=');
            if (name === 'session_token') {
                document.location.href = "/";
                break;
            }
        }
    };

    const handleEmailChange = (e) => {
        setEmail(e.target.value);
    };

    const handlePasswordChange = (e) => {
        setPassword(e.target.value);
    };

    const handleSubmit = async (e) => {
        e.preventDefault();

        const formData = {
            email: email,
            password: password,
        };

        if (email == "" || password == "") {
            return;
        }

        try {
            const response = await fetch('/api/login', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(formData),
                credentials: 'include',
            });

            if (response.ok) {
                handleSuccess();
            } else {
                setErrorMessage('Email or Password is wrong.');
            }
        } catch (error) {
            console.error('Error occurred:', error);
        }
    };

    return(
        <div className='side_section'>

            <div className='spacer'></div>
            <form onSubmit={handleSubmit}>
                <h1>Email:</h1>
                <input className='input' type='email' value={email} onChange={handleEmailChange} placeholder='john.doe@tophack.at' />

                <h1>Password:</h1>
                <input className='input' type='password' value={password} onChange={handlePasswordChange} />

                <h1 className='errorMsg'>{ errorMessage }</h1>

                <button type='submit' className='submitter'>Login</button>
            </form>
        </div>
    )
}

export default Login;