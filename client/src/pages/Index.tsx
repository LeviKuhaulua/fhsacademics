import * as React from 'react'; 
import { createRoot } from 'react-dom/client'; 
import '../styles/styles.css';
import Header from '../components/Header'


const Index = () => {
    return(
        <>
            <Header /> 
            <h1 className="text-4xl font-bold">Hello World</h1>
            <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Est ab modi blanditiis dolor aliquid at asperiores fugiat eveniet hic ipsa, beatae itaque. Exercitationem voluptatem harum error recusandae! Consequatur, facere dolore.
            Placeat culpa fugit qui id aut rem, doloribus molestias quos ea totam, beatae, a atque accusamus praesentium nisi quam veniam accusantium magnam doloremque distinctio ducimus tenetur. Necessitatibus ipsam sed vero.
            Delectus quae nam asperiores eveniet harum sed vitae minima exercitationem doloribus, illo odio ex eos commodi optio nesciunt dolore hic dicta numquam corporis voluptatum beatae. Odit, quaerat maxime! Voluptates, veritatis?</p>
        </>
    );
}; 

const root = document.getElementById('root');

createRoot(root).render(<Index />);