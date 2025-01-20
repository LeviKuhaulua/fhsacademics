import * as React from 'react';
import { createRoot } from 'react-dom/client';
import '../styles/styles.css';
import Navbar from '../components/Navbar';

const About = () => {
    return(
        <>
            <Navbar />
            <h1>This is the about page</h1>
        </>
    );
}

const root = document.getElementById('root');

createRoot(root).render(<About />);