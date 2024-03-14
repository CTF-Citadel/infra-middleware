import "./profile.css";
import { useState, useEffect } from 'react';
import blank_profile from '../assets/blank_profile.png';

function Profile() {
    const [userData, setUserData] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await fetch('/api/data');

                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }

                const data = await response.json();

                setUserData(data);
                setLoading(false);
            } catch (error) {
                setError(error);
                setLoading(false);
            }
        };

        fetchData();
        
        const cookies = document.cookie.split(';');
        for (const cookie of cookies) {
            const [name, value] = cookie.trim().split('=');
            if (name === 'session_token') {
                break;
            } else {
                document.location.href = "/";
            }
        }
    }, []);

    if (loading) {
        return <div>Loading...</div>;
    }

    if (error) {
        return <div>Error: {error.message}</div>;
    }

    return (
        <>
        <div className="section profilePage" style={{ display: 'flex', alignItems: 'center' }}>
            <div className="leftHalf leftTop">
                <h1 className="text">User Data</h1>
                <img src={blank_profile} alt="Bank Counter" className="userprofile"/>
            </div>
            <div className="rightHalf">
                <h2 className="text rightTop">Email:</h2>
                <p className="text">{userData.email}</p>
                <br/>
                <h2 className="text">Balance:</h2>
                <p className="text">{userData.balance}.00€</p>
                <br/>
                <h2 className="text">Notes:</h2>
                <p className="text">{userData.notes}</p>
            </div>
        </div>
        </>
    );
}

export default Profile;
