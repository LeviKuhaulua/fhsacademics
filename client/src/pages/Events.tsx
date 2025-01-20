import * as React from 'react';
import { createRoot } from 'react-dom/client';
import '../styles/styles.css';
import Navbar from '../components/Navbar';

const Events = () => {
    return(
        <>
            <Navbar />
            <h1>This is the Events page</h1>
        </>
    );
}

const root = document.getElementById('root');

createRoot(root).render(<Events />);