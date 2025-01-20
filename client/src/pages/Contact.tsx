import * as React from 'react';
import { createRoot } from 'react-dom/client';
import '../styles/styles.css';
import Navbar from '../components/Navbar';

const Contact = () => {
    return(
        <>
            <Navbar />
            <h1>This is the Contact Page</h1>
        </>
    );
}

const root = document.getElementById('root');

createRoot(root).render(<Contact />);